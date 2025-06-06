# MLActionClassifier.VideoAugmentationOptions

**Framework**: Create ML  
**Kind**: struct

The video augmentations for an action classifier training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct VideoAugmentationOptions
```

## Topics

### Designating video augmentation options
- [static let horizontalFlip: MLActionClassifier.VideoAugmentationOptions](mlactionclassifier/videoaugmentationoptions/horizontalflip.md)
  A video augmentation that creates a horizontally flipped copy of a sample video.
### Creating augmentation options
- [init(rawValue: Int)](mlactionclassifier/videoaugmentationoptions/init(rawvalue:).md)
  Creates a video augmentation option set from a raw value.
- [init()](mlactionclassifier/videoaugmentationoptions/init.md)
  Creates an empty option set.
- [init<S>(S)](mlactionclassifier/videoaugmentationoptions/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](mlactionclassifier/videoaugmentationoptions/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
### Inspecting options
- [var isEmpty: Bool](mlactionclassifier/videoaugmentationoptions/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [let rawValue: Int](mlactionclassifier/videoaugmentationoptions/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [func contains(Self) -> Bool](mlactionclassifier/videoaugmentationoptions/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
### Adding options
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](mlactionclassifier/videoaugmentationoptions/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func update(with: Self.Element) -> Self.Element?](mlactionclassifier/videoaugmentationoptions/update(with:).md)
  Inserts the given element into the set.
### Combining options
- [func union(Self) -> Self](mlactionclassifier/videoaugmentationoptions/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func formUnion(Self)](mlactionclassifier/videoaugmentationoptions/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func intersection(Self) -> Self](mlactionclassifier/videoaugmentationoptions/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func formIntersection(Self)](mlactionclassifier/videoaugmentationoptions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func symmetricDifference(Self) -> Self](mlactionclassifier/videoaugmentationoptions/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](mlactionclassifier/videoaugmentationoptions/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
### Removing options
- [func remove(Self.Element) -> Self.Element?](mlactionclassifier/videoaugmentationoptions/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtracting(Self) -> Self](mlactionclassifier/videoaugmentationoptions/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
- [func subtract(Self)](mlactionclassifier/videoaugmentationoptions/subtract(_:).md)
  Removes the elements of the given set from this set.
### Comparing options
- [func isDisjoint(with: Self) -> Bool](mlactionclassifier/videoaugmentationoptions/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isSubset(of: Self) -> Bool](mlactionclassifier/videoaugmentationoptions/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isStrictSubset(of: Self) -> Bool](mlactionclassifier/videoaugmentationoptions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isSuperset(of: Self) -> Bool](mlactionclassifier/videoaugmentationoptions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](mlactionclassifier/videoaugmentationoptions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [static func != (Self, Self) -> Bool](mlactionclassifier/videoaugmentationoptions/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Encoding options
- [init(from: any Decoder) throws](mlactionclassifier/videoaugmentationoptions/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int`.
- [func encode(to: any Encoder) throws](mlactionclassifier/videoaugmentationoptions/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int`.
### Supporting types
- [MLActionClassifier.VideoAugmentationOptions.Element](mlactionclassifier/videoaugmentationoptions/element.md)
  The element type of the option set.
- [MLActionClassifier.VideoAugmentationOptions.ArrayLiteralElement](mlactionclassifier/videoaugmentationoptions/arrayliteralelement.md)
  The type of the elements of an array literal.
- [MLActionClassifier.VideoAugmentationOptions.RawValue](mlactionclassifier/videoaugmentationoptions/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](mlactionclassifier/videoaugmentationoptions/equatable-implementations.md)
- [OptionSet Implementations](mlactionclassifier/videoaugmentationoptions/optionset-implementations.md)
- [RawRepresentable Implementations](mlactionclassifier/videoaugmentationoptions/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](mlactionclassifier/videoaugmentationoptions/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [MLActionClassifier.ModelParameters.ValidationData](mlactionclassifier/modelparameters-swift.struct/validationdata.md)
  The source of a validation dataset for an action classifier.
- [MLActionClassifier.ModelParameters.ModelAlgorithmType](mlactionclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The action classifier training algorithm options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/videoaugmentationoptions)*