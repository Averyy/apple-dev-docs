# localizedString(forStatusCode:)

**Framework**: Foundation  
**Kind**: method

Returns a localized string corresponding to a specified HTTP status code.

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
class func localizedString(forStatusCode statusCode: Int) -> String
```

#### Return Value

A localized string suitable for displaying to users that describes the specified status code.

## Parameters

- `statusCode`: The HTTP status code. See   for details.

## See Also

- [var statusCode: Int](httpurlresponse/statuscode.md)
  The response’s HTTP status code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpurlresponse/localizedstring(forstatuscode:))*