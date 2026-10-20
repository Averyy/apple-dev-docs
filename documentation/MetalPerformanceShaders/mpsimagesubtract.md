# MPSImageSubtract

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A filter that returns the element-wise difference of its two input images.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageSubtract
```

```objc
@interface MPSImageSubtract : MPSImageArithmetic
```

## Topics

### Initializers
- [init(device: any MTLDevice)](./mpsimagesubtract/init%28device%29.md)

## Relationships

### Inherits From
- [MPSImageArithmetic](./mpsimagearithmetic.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Image Arithmetic Filters
- [class MPSImageAdd](./mpsimageadd.md)
  A filter that returns the element-wise sum of its two input images.
- [class MPSImageMultiply](./mpsimagemultiply.md)
  A filter that returns the element-wise product of its two input images.
- [class MPSImageDivide](./mpsimagedivide.md)
  A filter that returns the element-wise quotient of its two input images.
- [class MPSImageArithmetic](./mpsimagearithmetic.md)
  Base class for basic arithmetic nodes


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagesubtract)*