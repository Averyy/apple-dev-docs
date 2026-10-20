# MTKTextureLoader.Error

**Framework**: MetalKit  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * MTKTextureLoaderError;
```

## Topics

### Initializers
- [init(rawValue: String)](./error/init%28rawvalue%29.md)
### Keys
- [static let domain: MTKTextureLoader.Error](./error/domain.md)
  The error domain used by `MetalKit` when returning texture loading errors.
- [static let key: MTKTextureLoader.Error](./error/key.md)
  The key used to retrieve an error string from an error object’s [`userInfo`](../../Foundation/nserror/userinfo.md) dictionary.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/error)*