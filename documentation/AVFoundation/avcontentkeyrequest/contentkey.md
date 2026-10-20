# contentKey

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The generated content key.

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
var contentKey: AVContentKey? { get }
```

```objc
@property (readonly, nullable) AVContentKey * contentKey;
```

## See Also

### Inspecting a request
- [var contentKeySpecifier: AVContentKeySpecifier](./contentkeyspecifier.md)
  The requested content key specifier.
- [var options: [String : any Sendable]](./options.md)
  A dictionary of options used to initialize key loading.
- [AVContentKeyRequest.RetryReason](./retryreason.md)
  The reason for asking the client to retry a content key request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/contentkey)*