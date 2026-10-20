# MLDictionaryConstraint

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

The constraint on the keys for a dictionary feature.

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
class MLDictionaryConstraint
```

```objc
@interface MLDictionaryConstraint : NSObject
```

## Topics

### Accessing the constraint
- [var keyType: MLFeatureType](./mldictionaryconstraint/keytype.md)
  The key type for the dictionary.
### Initializers
- [init?(coder: NSCoder)](./mldictionaryconstraint/init%28coder%29.md)

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
- [var multiArrayConstraint: MLMultiArrayConstraint?](./mlfeaturedescription/multiarrayconstraint.md)
  The constraints on a multidimensional array feature.
- [class MLMultiArrayConstraint](./mlmultiarrayconstraint.md)
  The shape and data type constraints for a multidimensional array feature.
- [var sequenceConstraint: MLSequenceConstraint?](./mlfeaturedescription/sequenceconstraint.md)
  The constraints for a sequence feature.
- [class MLSequenceConstraint](./mlsequenceconstraint.md)
  The constraints for a sequence feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mldictionaryconstraint)*