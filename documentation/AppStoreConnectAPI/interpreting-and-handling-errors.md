# Interpreting and Handling Errors

**Framework**: App Store Connect API

Learn how the App Store Connect API returns errors and handle them in your code.

#### Overview

When you send a request to the App Store Connect API, you receive a response that includes an HTTP status code and, in most cases, a response body. To determine your request’s status and handle errors, use the HTTP status code along with the `code` from the [`ErrorResponse`](errorresponse.md). Interpret the error starting with the most general information first.

##### Read the Http Status Code

The HTTP status code informs you if the request succeeded or failed. If it succeeded, the HTTP status code is in the 200 range, and the response body contains the requested data. If the request failed, the HTTP status code is in the 400 or 500 range, and the response body contains information about the error. In many cases, the status code may be all you need to properly handle errors.  See [`About the HTTP Status Code`](about-the-http-status-code.md) for more information.

##### Interpret the Error Response

If the API request failed, the [`ErrorResponse`](errorresponse.md) object contains details to help you troubleshoot the error, and a `code` property to use for programmatic error handling. See [`Parsing the Error Response Code`](parsing-the-error-response-code.md) for more information.

##### Pinpoint the Source of the Error

In some cases, the error information includes a `source` property that precisely locates the problem in your request. See [`Pinpointing the Location of Errors`](pinpointing-the-location-of-errors.md) for more information.

## Topics

### Handling Errors
- [About the HTTP Status Code](about-the-http-status-code.md)
  Learn how the status code helps you determine if an App Store Connect  API request succeeded or why it failed.
- [Parsing the Error Response Code](parsing-the-error-response-code.md)
  Interpret the error details to troubleshoot API requests and perform programmatic error handling.
- [Pinpointing the Location of Errors](pinpointing-the-location-of-errors.md)
  Locate the specific source of the error.
### Objects
- [object ErrorLinks](errorlinks.md)
- [object ErrorResponse](errorresponse.md)
  The error details that an API returns in the response body whenever the API request isn’t successful.
- [object JsonPointer](jsonpointer.md)
  An object that contains the JSON pointer that indicates the location of the error.
- [object Parameter](parameter.md)
  An object that contains the query parameter that produced the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/interpreting-and-handling-errors)*