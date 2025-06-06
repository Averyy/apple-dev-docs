# subtract(_:)

**Framework**: RealityKit  
**Kind**: method

Removes the elements of the given set from this set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

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

- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](arview/renderoptions-swift.struct/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func update(with: Self.Element) -> Self.Element?](arview/renderoptions-swift.struct/update(with:).md)
  Inserts the given element into the set.
- [func remove(Self.Element) -> Self.Element?](arview/renderoptions-swift.struct/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtracting(Self) -> Self](arview/renderoptions-swift.struct/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/subtract(_:))*