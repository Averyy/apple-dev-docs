# intersection(_:)

**Framework**: Create ML  
**Kind**: method

Returns a new option set with only the elements contained in both this set and the given set.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func intersection(_ other: Self) -> Self
```

#### Return Value

A new option set with only the elements contained in both this set and `other`.

#### Discussion

This example uses the `intersection(_:)` method to limit the available shipping options to what can be used with a PO Box destination.

```None
// Can only ship standard or priority to PO Boxes
let poboxShipping: ShippingOptions = [.standard, .priority]
let memberShipping: ShippingOptions =
        [.standard, .priority, .secondDay]

let availableOptions = memberShipping.intersection(poboxShipping)
print(availableOptions.contains(.priority))
// Prints "true"
print(availableOptions.contains(.secondDay))
// Prints "false"
```

## Parameters

- `other`: An option set.

## See Also

- [func union(Self) -> Self](mlimageclassifier/imageaugmentationoptions/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func formUnion(Self)](mlimageclassifier/imageaugmentationoptions/formunion(_:).md)
  Inserts the elements of another set into this option set.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/imageaugmentationoptions/intersection(_:))*