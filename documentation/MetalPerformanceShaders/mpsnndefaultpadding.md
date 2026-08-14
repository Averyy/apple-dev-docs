# MPSNNDefaultPadding

**Framework**: Metal Performance Shaders  
**Kind**: class

A class that provides predefined padding policies for common tasks.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNDefaultPadding
```

## Topics

### Initializers
- [convenience init(method: MPSNNPaddingMethod)](mpsnndefaultpadding/init(method:).md)
- [struct MPSNNPaddingMethod](mpsnnpaddingmethod.md)
  Options that define a graph’s padding.
### Instance Methods
- [func label() -> String](mpsnndefaultpadding/label.md)
### Type Methods
- [class func forTensorflowAveragePooling() -> Self](mpsnndefaultpadding/fortensorflowaveragepooling.md)
- [class func forTensorflowAveragePoolingValidOnly() -> Self](mpsnndefaultpadding/fortensorflowaveragepoolingvalidonly.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [MPSNNPadding](mpsnnpadding.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnndefaultpadding)*