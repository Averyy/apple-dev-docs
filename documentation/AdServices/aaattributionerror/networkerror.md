# networkError

**Framework**: AdServices  
**Kind**: property

The server is unable to provide a token because the internet isn’t available.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- macOS 11.1+
- visionOS 1.0+

## Declaration

```swift
static var networkError: AAAttributionError.Code { get }
```

#### Discussion

To receive an attribution token, you must have unimpeded internet access. Make sure you’re not using a simulator when generating a token.

## See Also

- [static var internalError: AAAttributionError.Code](aaattributionerror/internalerror.md)
  The server is unable to provide a token because of an internal error.
- [static var platformNotSupported: AAAttributionError.Code](aaattributionerror/platformnotsupported.md)
  The server is unable to provide a token because of an unsupported operating system.
- [AAAttributionError.Code](aaattributionerror/code.md)
  The error code that the parent class issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adservices/aaattributionerror/networkerror)*