# stateConstraint

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The state feature value constraint.

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
var stateConstraint: MLStateConstraint? { get }
```

```objc
@property (nonatomic, readonly, nullable) MLStateConstraint * stateConstraint;
```

#### Discussion

The property has a value when `.type == MLFeatureTypeState`.

## See Also

### Accessing feature constraints
- [var imageConstraint: MLImageConstraint?](./imageconstraint.md)
  The size and format constraints for an image feature.
- [class MLImageConstraint](../mlimageconstraint.md)
  The width, height, and pixel format constraints of an image feature.
- [var dictionaryConstraint: MLDictionaryConstraint?](./dictionaryconstraint.md)
  The constraint for a dictionary feature.
- [class MLDictionaryConstraint](../mldictionaryconstraint.md)
  The constraint on the keys for a dictionary feature.
- [var multiArrayConstraint: MLMultiArrayConstraint?](./multiarrayconstraint.md)
  The constraints on a multidimensional array feature.
- [class MLMultiArrayConstraint](../mlmultiarrayconstraint.md)
  The shape and data type constraints for a multidimensional array feature.
- [var sequenceConstraint: MLSequenceConstraint?](./sequenceconstraint.md)
  The constraints for a sequence feature.
- [class MLSequenceConstraint](../mlsequenceconstraint.md)
  The constraints for a sequence feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturedescription/stateconstraint)*