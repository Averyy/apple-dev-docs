# MTKTextureLoader.Error

**Framework**: MetalKit  
**Kind**: struct

Errors returned by the texture loader.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct Error
```

## Topics

### Initializers
- [init(rawValue: String)](mtktextureloader/error/init(rawvalue:).md)
### Keys
- [static let domain: MTKTextureLoader.Error](mtktextureloader/error/domain.md)
  The error domain used by `MetalKit` when returning texture loading errors.
- [static let key: MTKTextureLoader.Error](mtktextureloader/error/key.md)
  The key used to retrieve an error string from an error object’s [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/userinfo) dictionary.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/error)*