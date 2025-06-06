# subtracting(_:)

**Framework**: Create ML  
**Kind**: method

Returns a new set containing the elements of this set that do not occur in the given set.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func subtracting(_ other: Self) -> Self
```

#### Return Value

A new set.

#### Discussion

In the following example, the `nonNeighbors` set is made up of the elements of the `employees` set that are not elements of `neighbors`:

```None
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani", "Greta"]
let nonNeighbors = employees.subtracting(neighbors)
print(nonNeighbors)
// Prints "["Diana", "Chris", "Alicia"]"
```

## Parameters

- `other`: A set of the same type as the current set.

## See Also

- [func remove(Self.Element) -> Self.Element?](mlactionclassifier/videoaugmentationoptions/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](mlactionclassifier/videoaugmentationoptions/subtract(_:).md)
  Removes the elements of the given set from this set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/videoaugmentationoptions/subtracting(_:))*