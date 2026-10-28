# localizedString(forStatusCode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSString *) localizedStringForStatusCode:(NSInteger) statusCode;
```

## Return Value

A localized string suitable for displaying to users that describes the specified status code.

## Parameters

- `statusCode`: The HTTP status code. See [RFC 2616](http://www.ietf.org/rfc/rfc2616.txt) for details.

## See Also

### Getting response status codes
- [var statusCode: Int](./statuscode.md)
  The response’s HTTP status code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpurlresponse/localizedstring(forstatuscode:))*