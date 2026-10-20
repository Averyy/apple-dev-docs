# MPSNNDefaultPadding

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSNNDefaultPadding : NSObject
```

## Topics

### Initializers
- [convenience init(method: MPSNNPaddingMethod)](./mpsnndefaultpadding/init%28method%29.md)
- [struct MPSNNPaddingMethod](./mpsnnpaddingmethod.md)
  Options that define a graph’s padding.
### Instance Methods
- [func label() -> String](./mpsnndefaultpadding/label%28%29.md)
### Type Methods
- [class func forTensorflowAveragePooling() -> Self](./mpsnndefaultpadding/fortensorflowaveragepooling%28%29.md)
- [class func forTensorflowAveragePoolingValidOnly() -> Self](./mpsnndefaultpadding/fortensorflowaveragepoolingvalidonly%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MPSNNPadding](./mpsnnpadding.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnndefaultpadding)*