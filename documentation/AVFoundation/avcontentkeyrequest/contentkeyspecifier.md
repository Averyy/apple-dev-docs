# contentKeySpecifier

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The requested content key specifier.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```swift
var contentKeySpecifier: AVContentKeySpecifier { get }
```

```objc
@property (readonly) AVContentKeySpecifier * contentKeySpecifier;
```

## See Also

### Inspecting a request
- [var contentKey: AVContentKey?](./contentkey.md)
  The generated content key.
- [var options: [String : any Sendable]](./options.md)
  A dictionary of options used to initialize key loading.
- [AVContentKeyRequest.RetryReason](./retryreason.md)
  The reason for asking the client to retry a content key request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/contentkeyspecifier)*