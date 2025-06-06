# union(_:)

**Framework**: Create ML  
**Kind**: method

Returns a new option set of the elements contained in this set, in the given set, or in both.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func union(_ other: Self) -> Self
```

#### Return Value

A new option set made up of the elements contained in this set, in `other`, or in both.

#### Discussion

This example uses the `union(_:)` method to add two more shipping options to the default set.

```None
let defaultShipping = ShippingOptions.standard
let memberShipping = defaultShipping.union([.secondDay, .priority])
print(memberShipping.contains(.priority))
// Prints "true"
```

## Parameters

- `other`: An option set.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/videoaugmentationoptions/union(_:))*