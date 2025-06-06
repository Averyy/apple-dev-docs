# Option Set Support

**Framework**: Create ML

****Inspect and modify an image augmentation option set with the properties and methods it inherits from standard protocols.

#### Overview

You don’t typically use these properties and methods directly. [`MLHandPoseClassifier.ImageAugmentationOptions`](mlhandposeclassifier/imageaugmentationoptions.md) inherits these symbols from [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) and [`Codable`](https://developer.apple.com/documentation/Swift/Codable). Create a set of image augmentations by creating an array literal with any combination of these type properties:

- `horizontalFlip`
- `randomMove`
- `randomScale`
- `randomShift`

## Topics

### Creating an Augmentation
- [init(arrayLiteral: Self.Element...)](mlhandposeclassifier/imageaugmentationoptions/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [init()](mlhandposeclassifier/imageaugmentationoptions/init.md)
  Creates an empty option set.
- [init(rawValue: Int)](mlhandposeclassifier/imageaugmentationoptions/init(rawvalue:).md)
  Creates an option set from an integer.
- [init<S>(S)](mlhandposeclassifier/imageaugmentationoptions/init(_:).md)
  Creates a new set from a finite sequence of items.
### Inspecting an Augmentation
- [var isEmpty: Bool](mlhandposeclassifier/imageaugmentationoptions/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [let rawValue: Int](mlhandposeclassifier/imageaugmentationoptions/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [func contains(Self) -> Bool](mlhandposeclassifier/imageaugmentationoptions/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
### Adding an Augmentation
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](mlhandposeclassifier/imageaugmentationoptions/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func update(with: Self.Element) -> Self.Element?](mlhandposeclassifier/imageaugmentationoptions/update(with:).md)
  Inserts the given element into the set.
### Combining Augmentations
- [func union(Self) -> Self](mlhandposeclassifier/imageaugmentationoptions/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func formUnion(Self)](mlhandposeclassifier/imageaugmentationoptions/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func intersection(Self) -> Self](mlhandposeclassifier/imageaugmentationoptions/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func formIntersection(Self)](mlhandposeclassifier/imageaugmentationoptions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func symmetricDifference(Self) -> Self](mlhandposeclassifier/imageaugmentationoptions/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](mlhandposeclassifier/imageaugmentationoptions/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
### Removing an Augmentation
- [func remove(Self.Element) -> Self.Element?](mlhandposeclassifier/imageaugmentationoptions/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](mlhandposeclassifier/imageaugmentationoptions/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](mlhandposeclassifier/imageaugmentationoptions/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
### Comparing Augmentations
- [func isDisjoint(with: Self) -> Bool](mlhandposeclassifier/imageaugmentationoptions/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isSubset(of: Self) -> Bool](mlhandposeclassifier/imageaugmentationoptions/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isStrictSubset(of: Self) -> Bool](mlhandposeclassifier/imageaugmentationoptions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isSuperset(of: Self) -> Bool](mlhandposeclassifier/imageaugmentationoptions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](mlhandposeclassifier/imageaugmentationoptions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [static func != (Self, Self) -> Bool](mlhandposeclassifier/imageaugmentationoptions/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Encoding and Decoding an Augmentation
- [func encode(to: any Encoder) throws](mlhandposeclassifier/imageaugmentationoptions/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int`.
- [init(from: any Decoder) throws](mlhandposeclassifier/imageaugmentationoptions/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int`.

## See Also

- [static let horizontallyFlip: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions/horizontallyflip.md)
  Apply left-right flips to the pose in an image.
- [static let rotate: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions/rotate.md)
  Randomly rotate the pose in an image.
- [static let scale: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions/scale.md)
  Randomly scale the pose in an image.
- [static let translate: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions/translate.md)
  Randomly translate the pose in an image.
- [MLHandPoseClassifier.ImageAugmentationOptions.RawValue](mlhandposeclassifier/imageaugmentationoptions/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [MLHandPoseClassifier.ImageAugmentationOptions.Element](mlhandposeclassifier/imageaugmentationoptions/element.md)
  The element type of the option set.
- [MLHandPoseClassifier.ImageAugmentationOptions.ArrayLiteralElement](mlhandposeclassifier/imageaugmentationoptions/arrayliteralelement.md)
  The type of the elements of an array literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/imageaugmentationoptions-option-set-support)*