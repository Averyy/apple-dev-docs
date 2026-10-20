# MTKModelError

**Framework**: MetalKit  
**Kind**: struct  
**Role**: Structure

Constants used to declare Model Errors.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MTKModelError
```

```c
typedef NSString * MTKModelError;
```

## Topics

### Initializing a Raw Constant
- [init(rawValue: String)](./mtkmodelerror/init%28rawvalue%29.md)
### Finding Model Error Constants
- [static let domain: MTKModelError](./mtkmodelerror/domain.md)
  The error domain used by MetalKit when returning mesh initialization errors.
- [static let key: MTKModelError](./mtkmodelerror/key.md)
  The key used to retrieve an error string from an error object’s [`userInfo`](../Foundation/nserror/userinfo.md) dictionary.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmodelerror)*