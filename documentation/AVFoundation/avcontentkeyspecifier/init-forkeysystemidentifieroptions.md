# init(forKeySystem:identifier:options:)

**Framework**: AVFoundation  
**Kind**: init

Creates a content key specifier.

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
init(forKeySystem keySystem: AVContentKeySystem, identifier contentKeyIdentifier: Any, options: [String : Any] = [:])
```

## Parameters

- `keySystem`: The key system to use to generate content keys.
- `contentKeyIdentifier`: The container and protocol-specific key identifier.
- `options`: Additional information necessary to obtain the key. Pass   to indicate no additional options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyspecifier/init(forkeysystem:identifier:options:))*