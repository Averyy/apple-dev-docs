# symmetricDifference(_:)

**Framework**: Swift  
**Kind**: method  
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

#### Return Value

A new set.

#### Discussion

In the following example, the `eitherNeighborsOrEmployees` set is made up of the elements of the `employees` and `neighbors` sets that are not in both `employees`  `neighbors`. In particular, the names `"Bethany"` and `"Eric"` do not appear in `eitherNeighborsOrEmployees`.

```swift
let employees: Set = ["Alicia", "Bethany", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani"]
let eitherNeighborsOrEmployees = employees.symmetricDifference(neighbors)
print(eitherNeighborsOrEmployees)
// Prints "["Diana", "Forlani", "Alicia"]"
```

## Parameters

- `other`: A set of the same type as the current set.

## See Also

- [func union(Self) -> Self](setalgebra/union(_:).md)
  Returns a new set with the elements of both this and the given set.
- [func formUnion(Self)](setalgebra/formunion(_:).md)
  Adds the elements of the given set to the set.
- [func intersection(Self) -> Self](setalgebra/intersection(_:).md)
  Returns a new set with the elements that are common to both this set and the given set.
- [func formIntersection(Self)](setalgebra/formintersection(_:).md)
  Removes the elements of this set that aren’t also in the given set.
- [func formSymmetricDifference(Self)](setalgebra/formsymmetricdifference(_:).md)
  Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra/symmetricdifference(_:))*