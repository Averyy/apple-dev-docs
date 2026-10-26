# MLStateConstraint

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

Constraint of a state feature value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class MLStateConstraint
```

```objc
@interface MLStateConstraint : NSObject
```

## Topics

### Inspecting a state constraint
- [var bufferShape: [Int]](./mlstateconstraint/buffershape-4zb3w.md)
  The shape of the state buffer.
- [var dataType: MLMultiArrayDataType](./mlstateconstraint/datatype.md)
  The data type of scalars in the state buffer.
- [bufferShape](./mlstateconstraint/buffershape-6o5vn.md)
  The shape of the state buffer.
### Initializers
- [init?(coder: NSCoder)](./mlstateconstraint/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Model state
- [class MLState](./mlstate.md)
  Handle to the state buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlstateconstraint)*