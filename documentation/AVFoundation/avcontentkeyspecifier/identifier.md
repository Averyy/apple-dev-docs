# identifier

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The container and protocol-specific key identifier.

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
var identifier: any Sendable { get }
```

```objc
@property (readonly) id identifier;
```

## See Also

### Inspecting a specifier
- [var keySystem: AVContentKeySystem](./keysystem.md)
  The key system that generates content keys.
- [var options: [String : any Sendable]](./options.md)
  A dictionary of options with which you initialized the specifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyspecifier/identifier)*