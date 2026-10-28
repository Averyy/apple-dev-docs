# statusCode

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The response’s HTTP status code.

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
var statusCode: Int { get }
```

```objc
@property (readonly) NSInteger statusCode;
```

## Discussion

See [RFC 2616](http://www.ietf.org/rfc/rfc2616.txt) for details.

## See Also

### Getting response status codes
- [class func localizedString(forStatusCode: Int) -> String](./localizedstring%28forstatuscode%29.md)
  Returns a localized string corresponding to a specified HTTP status code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpurlresponse/statuscode)*