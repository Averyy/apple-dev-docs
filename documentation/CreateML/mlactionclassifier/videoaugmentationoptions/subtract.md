# subtract(_:)

**Framework**: Create ML  
**Kind**: method

Removes the elements of the given set from this set.

**Availability**:
- macOS 10.14+

## Declaration

```swift
mutating func subtract(_ other: Self)
```

#### Discussion

In the following example, the elements of the `employees` set that are also members of the `neighbors` set are removed. In particular, the names `"Bethany"` and `"Eric"` are removed from `employees`.

```None
var employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani", "Greta"]
employees.subtract(neighbors)
print(employees)
// Prints "["Diana", "Chris", "Alicia"]"
```

## Parameters

- `other`: A set of the same type as the current set.

## See Also

- [func remove(Self.Element) -> Self.Element?](mlactionclassifier/videoaugmentationoptions/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtracting(Self) -> Self](mlactionclassifier/videoaugmentationoptions/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/videoaugmentationoptions/subtract(_:))*