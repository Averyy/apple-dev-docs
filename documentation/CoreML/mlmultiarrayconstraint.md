# MLMultiArrayConstraint

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

The shape and data type constraints for a multidimensional array feature.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class MLMultiArrayConstraint
```

```objc
@interface MLMultiArrayConstraint : NSObject
```

## Topics

### Accessing the Constraints
- [var shape: [NSNumber]](./mlmultiarrayconstraint/shape.md)
  The shape of the multi array.
- [var dataType: MLMultiArrayDataType](./mlmultiarrayconstraint/datatype.md)
  The type for the multi array.
- [var shapeConstraint: MLMultiArrayShapeConstraint](./mlmultiarrayconstraint/shapeconstraint.md)
  The constraint on the shape of the multiarray.
- [class MLMultiArrayShapeConstraint](./mlmultiarrayshapeconstraint.md)
  The lists of shapes or ranges of shapes that constrain a multiarray feature.
### Initializers
- [init?(coder: NSCoder)](./mlmultiarrayconstraint/init%28coder%29.md)

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

### Accessing feature constraints
- [var stateConstraint: MLStateConstraint?](./mlfeaturedescription/stateconstraint.md)
  The state feature value constraint.
- [var imageConstraint: MLImageConstraint?](./mlfeaturedescription/imageconstraint.md)
  The size and format constraints for an image feature.
- [class MLImageConstraint](./mlimageconstraint.md)
  The width, height, and pixel format constraints of an image feature.
- [var dictionaryConstraint: MLDictionaryConstraint?](./mlfeaturedescription/dictionaryconstraint.md)
  The constraint for a dictionary feature.
- [class MLDictionaryConstraint](./mldictionaryconstraint.md)
  The constraint on the keys for a dictionary feature.
- [var multiArrayConstraint: MLMultiArrayConstraint?](./mlfeaturedescription/multiarrayconstraint.md)
  The constraints on a multidimensional array feature.
- [var sequenceConstraint: MLSequenceConstraint?](./mlfeaturedescription/sequenceconstraint.md)
  The constraints for a sequence feature.
- [class MLSequenceConstraint](./mlsequenceconstraint.md)
  The constraints for a sequence feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarrayconstraint)*