# MLImageClassifier.ImageAugmentationOptions

**Framework**: Create ML  
**Kind**: struct

The variations that the training process can use to generate more training data from the training data you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
struct ImageAugmentationOptions
```

#### Overview

Augmentation generates new images from the training data you supply to increase the amount of training data available to the model.

See [`Improving Your Model’s Accuracy`](improving-your-model-s-accuracy.md) for a discussion about when to use augmentation.

## Topics

### Selecting augmentation options
- [static let crop: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/crop.md)
  An option for augmenting training data by creating cropped versions of each image.
- [static let rotation: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/rotation.md)
  An option for augmenting training data by rotating each image.
- [static let blur: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/blur.md)
  An option for augmenting training data by blurring each image.
- [static let exposure: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/exposure.md)
  An option for augmenting training data by lightening or darkening each image.
- [static let noise: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/noise.md)
  An option for augmenting training data by adding random amounts of noise to each image.
- [static let flip: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/flip.md)
  An option for augmenting training data by flipping each image along the horizontal and vertical axes.
### Creating augmentation options
- [init()](mlimageclassifier/imageaugmentationoptions/init.md)
  Creates an empty option set.
- [init(arrayLiteral: Self.Element...)](mlimageclassifier/imageaugmentationoptions/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [init<S>(S)](mlimageclassifier/imageaugmentationoptions/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(rawValue: Int)](mlimageclassifier/imageaugmentationoptions/init(rawvalue:).md)
  Creates an augmentation set with the given raw value.
- [let rawValue: Int](mlimageclassifier/imageaugmentationoptions/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Testing for membership in a set
- [var isEmpty: Bool](mlimageclassifier/imageaugmentationoptions/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [func contains(Self) -> Bool](mlimageclassifier/imageaugmentationoptions/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
### Adding and removing elements
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](mlimageclassifier/imageaugmentationoptions/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func update(with: Self.Element) -> Self.Element?](mlimageclassifier/imageaugmentationoptions/update(with:).md)
  Inserts the given element into the set.
- [func remove(Self.Element) -> Self.Element?](mlimageclassifier/imageaugmentationoptions/remove(_:).md)
  Removes the given element and all elements subsumed by it.
### Combining sets
- [func union(Self) -> Self](mlimageclassifier/imageaugmentationoptions/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func formUnion(Self)](mlimageclassifier/imageaugmentationoptions/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func intersection(Self) -> Self](mlimageclassifier/imageaugmentationoptions/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func formIntersection(Self)](mlimageclassifier/imageaugmentationoptions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func symmetricDifference(Self) -> Self](mlimageclassifier/imageaugmentationoptions/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](mlimageclassifier/imageaugmentationoptions/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func subtract(Self)](mlimageclassifier/imageaugmentationoptions/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](mlimageclassifier/imageaugmentationoptions/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
### Comparing sets
- [func isStrictSubset(of: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isSubset(of: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isStrictSuperset(of: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSuperset(of: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func isDisjoint(with: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
### Testing for equality
- [static func != (Self, Self) -> Bool](mlimageclassifier/imageaugmentationoptions/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Supporting types
- [MLImageClassifier.ImageAugmentationOptions.Element](mlimageclassifier/imageaugmentationoptions/element.md)
  The element type of the option set.
- [MLImageClassifier.ImageAugmentationOptions.RawValue](mlimageclassifier/imageaugmentationoptions/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [MLImageClassifier.ImageAugmentationOptions.ArrayLiteralElement](mlimageclassifier/imageaugmentationoptions/arrayliteralelement.md)
  The type of the elements of an array literal.
### Default Implementations
- [Equatable Implementations](mlimageclassifier/imageaugmentationoptions/equatable-implementations.md)
- [OptionSet Implementations](mlimageclassifier/imageaugmentationoptions/optionset-implementations.md)
- [SetAlgebra Implementations](mlimageclassifier/imageaugmentationoptions/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [MLImageClassifier.FeatureExtractorType](mlimageclassifier/featureextractortype.md)
  The underlying base model that extracts image features for image classifier training session.
- [MLImageClassifier.ModelParameters.ValidationData](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  The source of a validation dataset for an image classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/imageaugmentationoptions)*