# symmetricDifference(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a new set with the elements that are either in this set or in the given set, but not in both.

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
func symmetricDifference(_ other: Self) -> Self
```

## Return Value

A new set.

## Discussion

In the following example, the `eitherNeighborsOrEmployees` set is made up of the elements of the `employees` and `neighbors` sets that are not in both `employees` *and* `neighbors`. In particular, the names `"Bethany"` and `"Eric"` do not appear in `eitherNeighborsOrEmployees`.

```swift
let employees: Set = ["Alicia", "Bethany", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani"]
let eitherNeighborsOrEmployees = employees.symmetricDifference(neighbors)
print(eitherNeighborsOrEmployees)
// Prints "["Diana", "Forlani", "Alicia"]"
```

## Parameters

- `other`: A set of the same type as the current set.

## Default Implementations

### SetAlgebra Implementations
- [func symmetricDifference(Self) -> Self](./symmetricdifference%28_%29-81pzi.md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.

## See Also

### Combining Sets
- [func union(Self) -> Self](./union%28_%29.md)
  Returns a new set with the elements of both this and the given set.
- [func formUnion(Self)](./formunion%28_%29.md)
  Adds the elements of the given set to the set.
- [func intersection(Self) -> Self](./intersection%28_%29.md)
  Returns a new set with the elements that are common to both this set and the given set.
- [func formIntersection(Self)](./formintersection%28_%29.md)
  Removes the elements of this set that aren’t also in the given set.
- [func formSymmetricDifference(Self)](./formsymmetricdifference%28_%29.md)
  Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra/symmetricdifference(_:))*