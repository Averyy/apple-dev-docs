# Option Set Support

**Framework**: Create ML

Inspect and modify a video augmentation option set with the properties and methods it inherits from standard protocols.

#### Overview

You don’t typically use these properties and methods directly.

[`MLHandActionClassifier.VideoAugmentationOptions`](mlhandactionclassifier/videoaugmentationoptions.md) inherits these symbols from [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) and [`Codable`](https://developer.apple.com/documentation/Swift/Codable). Create a set of video augmentations by creating an array literal with any combination of these type properties:

- `horizontalFlip`
- `randomMove`
- `randomScale`
- `randomShift`
- `frameDrop`
- `timeInterpolate`

## Topics

### Creating an Augmentation
- [init(arrayLiteral: Self.Element...)](mlhandactionclassifier/videoaugmentationoptions/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [init()](mlhandactionclassifier/videoaugmentationoptions/init.md)
  Creates an empty option set.
- [init(rawValue: Int)](mlhandactionclassifier/videoaugmentationoptions/init(rawvalue:).md)
  Creates an option set from an integer.
- [init<S>(S)](mlhandactionclassifier/videoaugmentationoptions/init(_:).md)
  Creates a new set from a finite sequence of items.
### Inspecting an Augmentation
- [var isEmpty: Bool](mlhandactionclassifier/videoaugmentationoptions/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [let rawValue: Int](mlhandactionclassifier/videoaugmentationoptions/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [func contains(Self) -> Bool](mlhandactionclassifier/videoaugmentationoptions/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
### Adding an Augmentation
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](mlhandactionclassifier/videoaugmentationoptions/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func update(with: Self.Element) -> Self.Element?](mlhandactionclassifier/videoaugmentationoptions/update(with:).md)
  Inserts the given element into the set.
### Combining Augmentations
- [func union(Self) -> Self](mlhandactionclassifier/videoaugmentationoptions/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func formUnion(Self)](mlhandactionclassifier/videoaugmentationoptions/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func intersection(Self) -> Self](mlhandactionclassifier/videoaugmentationoptions/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func formIntersection(Self)](mlhandactionclassifier/videoaugmentationoptions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func symmetricDifference(Self) -> Self](mlhandactionclassifier/videoaugmentationoptions/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](mlhandactionclassifier/videoaugmentationoptions/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
### Removing an Augmentation
- [func remove(Self.Element) -> Self.Element?](mlhandactionclassifier/videoaugmentationoptions/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](mlhandactionclassifier/videoaugmentationoptions/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](mlhandactionclassifier/videoaugmentationoptions/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
### Comparing Augmentations
- [func isDisjoint(with: Self) -> Bool](mlhandactionclassifier/videoaugmentationoptions/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isSubset(of: Self) -> Bool](mlhandactionclassifier/videoaugmentationoptions/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isStrictSubset(of: Self) -> Bool](mlhandactionclassifier/videoaugmentationoptions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isSuperset(of: Self) -> Bool](mlhandactionclassifier/videoaugmentationoptions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](mlhandactionclassifier/videoaugmentationoptions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [static func != (Self, Self) -> Bool](mlhandactionclassifier/videoaugmentationoptions/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Encoding and Decoding an Augmentation
- [func encode(to: any Encoder) throws](mlhandactionclassifier/videoaugmentationoptions/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int`.
- [init(from: any Decoder) throws](mlhandactionclassifier/videoaugmentationoptions/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/option-set-support)*