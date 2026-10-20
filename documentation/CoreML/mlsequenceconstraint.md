# MLSequenceConstraint

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

The constraints for a sequence feature.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class MLSequenceConstraint
```

```objc
@interface MLSequenceConstraint : NSObject
```

## Topics

### Accessing the constraints
- [var valueDescription: MLFeatureDescription](./mlsequenceconstraint/valuedescription.md)
  The description that all sequence elements must match.
- [var countRange: NSRange](./mlsequenceconstraint/countrange.md)
  The range of values allowed for the sequence’s length.
### Initializers
- [init?(coder: NSCoder)](./mlsequenceconstraint/init%28coder%29.md)

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
- [class MLMultiArrayConstraint](./mlmultiarrayconstraint.md)
  The shape and data type constraints for a multidimensional array feature.
- [var sequenceConstraint: MLSequenceConstraint?](./mlfeaturedescription/sequenceconstraint.md)
  The constraints for a sequence feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlsequenceconstraint)*