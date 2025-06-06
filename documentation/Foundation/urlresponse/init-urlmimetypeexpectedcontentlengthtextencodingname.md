# init(url:mimeType:expectedContentLength:textEncodingName:)

**Framework**: Foundation  
**Kind**: init

Creates an initialized [`URLResponse`](urlresponse.md) object with the URL, MIME type, length, and text encoding set to given values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(url URL: URL, mimeType MIMEType: String?, expectedContentLength length: Int, textEncodingName name: String?)
```

#### Return Value

The initialized URL response.

#### Discussion

This is the designated initializer for [`URLResponse`](urlresponse.md).

## Parameters

- `URL`: The URL for the new object.
- `MIMEType`: The MIME type.
- `length`: The expected content length.This value should be   if the expected length is undetermined
- `name`: The text encoding name. This value may be  .

## See Also

- [init?(url: URL, statusCode: Int, httpVersion: String?, headerFields: [String : String]?)](httpurlresponse/init(url:statuscode:httpversion:headerfields:).md)
  Initializes an HTTP URL response object with a status code, protocol version, and response headers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresponse/init(url:mimetype:expectedcontentlength:textencodingname:))*