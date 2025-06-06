# Pinpointing the Location of Errors

**Framework**: App Store Connect API

Locate the specific source of the error.

#### Overview

Some errors are produced by a specific element of the request. In that case, the [`ErrorResponse`](errorresponse.md) includes `source.parameter` or `source.pointer` values to indicate the exact location of the error. When the location of the error cannot be determined, the error response does not include those parameters. In some cases, the JSON pointer may indicate an element that isn’t in the request entity, but should be.

##### Use the Error Response to Pinpoint Parameter Errors

When an error occurs due to a problem with a parameter, the `source` property contains `source.parameter`, whose value contains the parameter with the error.

``For example, in this request, the `“emaill”` query parameter is misspelled:

```javascript
GET /v1/betaTesters?filter[emaill]=kate-bell%22mac.com
```

The API responds with an error that includes `source.parameter`:

```javascript
HTTP/1.1 400 Bad Request
{
    "errors": [
        {
            "status": "400",
            "id": "5becf2db-2f12-4d6a-9dc2-6ceb33c683b4",
            "title": "A parameter has an invalid value",
            "detail": "'emaill' is not a valid filter type",
            "code": "PARAMETER_ERROR.INVALID",
            "source": {
                "parameter": "filter[emaill]"
             }
        }
    ]
}

```

The `source.parameter` value indicates that the error is located in the `filter[emaill]` parameter.

##### Use the Error Response to Pinpoint Entity Errors

When an error occurs due to a problem with an entity, the `source` property contains a JSON pointer that describes the place in the request entity where the error originates. In some cases, this pointer may indicate an element that is not in the request entity but should be.

For more information about JSON pointers, see the [`RFC 6901`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6901) proposed standards document.

## See Also

- [About the HTTP Status Code](about-the-http-status-code.md)
  Learn how the status code helps you determine if an App Store Connect  API request succeeded or why it failed.
- [Parsing the Error Response Code](parsing-the-error-response-code.md)
  Interpret the error details to troubleshoot API requests and perform programmatic error handling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/pinpointing-the-location-of-errors)*