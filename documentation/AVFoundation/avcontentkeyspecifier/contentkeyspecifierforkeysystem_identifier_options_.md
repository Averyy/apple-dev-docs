# contentKeySpecifierForKeySystem:identifier:options:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

A convenience initializer to create a content key specifier.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```objc
+ (instancetype) contentKeySpecifierForKeySystem:(AVContentKeySystem) keySystem identifier:(id) contentKeyIdentifier options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `keySystem`: The key system to use to generate content keys.
- `contentKeyIdentifier`: The container and protocol-specific key identifier.
- `options`: Additional information necessary to obtain the key. Pass `nil` to indicate no additional options.

## See Also

### Creating a specifier
- [init(forKeySystem: AVContentKeySystem, identifier: Any, options: [String : Any])](./init%28forkeysystem,identifier,options%29.md)
  Creates a content key specifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyspecifier/contentkeyspecifierforkeysystem:identifier:options:)*