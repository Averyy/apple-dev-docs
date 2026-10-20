# options

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A dictionary of options used to initialize key loading.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var options: [String : any Sendable] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,id> * options;
```

## See Also

### Inspecting a request
- [var contentKey: AVContentKey?](./contentkey.md)
  The generated content key.
- [var contentKeySpecifier: AVContentKeySpecifier](./contentkeyspecifier.md)
  The requested content key specifier.
- [AVContentKeyRequest.RetryReason](./retryreason.md)
  The reason for asking the client to retry a content key request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/options)*