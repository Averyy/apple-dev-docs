# formIntersection(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Removes the elements of this set that aren’t also in the given set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func formIntersection(_ other: Self)
```

#### Discussion

In the following example, the elements of the `employees` set that are not also members of the `neighbors` set are removed. In particular, the names `"Alicia"`, `"Chris"`, and `"Diana"` are removed.

```swift
var employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani", "Greta"]
employees.formIntersection(neighbors)
print(employees)
// Prints "["Bethany", "Eric"]"
```

## Parameters

- `other`: A set of the same type as the current set.

## Default Implementations

### SetAlgebra Implementations
- [func formIntersection(Self)](./formintersection%28_%29-9h7lm.md)
  Removes all elements of this option set that are not also present in the given set.

## See Also

### Combining Sets
- [func union(Self) -> Self](./union%28_%29.md)
  Returns a new set with the elements of both this and the given set.
- [func formUnion(Self)](./formunion%28_%29.md)
  Adds the elements of the given set to the set.
- [func intersection(Self) -> Self](./intersection%28_%29.md)
  Returns a new set with the elements that are common to both this set and the given set.
- [func symmetricDifference(Self) -> Self](./symmetricdifference%28_%29.md)
  Returns a new set with the elements that are either in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](./formsymmetricdifference%28_%29.md)
  Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra/formintersection(_:))*