# About Apple News API Error Messages

**Framework**: Apple News  
**Role**: Article

Understand the error message format for the Apple News API.

#### Overview

In responses, errors are represented as an array of information in a common format. The following example shows a Read Channel 400 error.  If the value of `channel_id` in your Read Channel request is not a UUID, you’ll receive an error such as the following:

```other
HTTP/1.1 400 Bad Request
Date: Wed, 17 Dec 2014 22:06:52 GMT
Content-Type: application/json
Content-Length: 212

{
  "errors": [
    {
      "code": "INVALID_TYPE",
      "keyPath": [
        "channel_id"
      ],
      "value": "not_a_uuid"
    }
  ]
}
```

##### Understanding the keyPath Array

When reporting Apple News Format errors through the API, the component with the error is identified through a `keyPath` array. The `keyPath` array navigates from the root of the JSON document to the problematic object. It identifies keys by name and array items by index.

Consider this test article example:

```json
{
  "title": "Test Article",
  "identifier": "testArticle",
  "version": "1.0",
  "language": "en",
  "layout": {
    "columns": 7,
    "width": 1024,
    "margin": 75,
    "gutter": 20
  },
  "components": [
    {
      "role": "title",
      "format": "html",
      "text": "Article Title"
    },
    {
      "role": "container",
      "components": [
        {
          "role": "heading",
          "text": "Article Subhead"
        },
        {
          "role": "intro",
          "text": "Article introduction."
        },
        {
          "role": "body",
          "layout": "bodyLayout",
          "text": "Second paragraph"
        }
      ]
    }
  ]
}
```

Now consider this error for the above example:

```json
{
  "errors": [
    {
      "code": "INVALID_DOCUMENT",
      "keyPath": [
        "components",
        1,
        "components",
        2,
        "layout"
      ],
      "message": "Component layout with identifier, bodyLayout, not found."
    }
  ]
}

```

In the test article example, to find the problematic component, you would follow these steps:

1. Find the top-level `components` property, whose value is an array.
2. Find the second object (`container`) in the array you found in step 1.
3. Within the `container` component, find the `components` property, whose value is an array.
4. Find the third object (`body`) in the array you found in step 3.
5. Within this `body` component, find the `layout` property. This is where the problem is occurring.

## See Also

### Errors
- [object Warning](https://developer.apple.com/documentation/applenewsapi/warning)
  See the properties of a warning the Apple News API returned.
- [object Error](https://developer.apple.com/documentation/applenewsapi/error)
  See the properties of an error the Apple News API returned.
- [type Code](https://developer.apple.com/documentation/applenewsapi/code)
  See the error codes the Apple News API returned.
- [type Status](https://developer.apple.com/documentation/applenewsapi/status)
  See the HTTP status codes the Apple News API returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/about-apple-news-api-error-messages)*