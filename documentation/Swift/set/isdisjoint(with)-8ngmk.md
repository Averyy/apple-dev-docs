# isDisjoint(with:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether this set has no members in common with the given set.

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
func isDisjoint(with other: Set<Element>) -> Bool
```

Available when `Element` conforms to `Hashable`.

## Return Value

`true` if the set has no elements in common with `other`; otherwise, `false`.

## Discussion

In the following example, the `employees` set is disjoint with the `visitors` set because no name appears in both sets.

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let visitors: Set = ["Marcia", "Nathaniel", "Olivia"]
print(employees.isDisjoint(with: visitors))
// Prints "true"
```

## Parameters

- `other`: Another set.

## See Also

### Comparing Sets
- [static func == (Set<Element>, Set<Element>) -> Bool](./eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two sets have equal elements.
- [static func != (borrowing Self, borrowing Self) -> Bool](./noteq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are not equal.
- [func isSubset(of: Set<Element>) -> Bool](./issubset%28of%29-1d7pp.md)
  Returns a Boolean value that indicates whether this set is a subset of the given set.
- [func isSubset<S>(of: S) -> Bool](./issubset%28of%29-6qyo5.md)
  Returns a Boolean value that indicates whether the set is a subset of the given sequence.
- [func isStrictSubset(of: Set<Element>) -> Bool](./isstrictsubset%28of%29-96vc3.md)
  Returns a Boolean value that indicates whether the set is a strict subset of the given sequence.
- [func isStrictSubset<S>(of: S) -> Bool](./isstrictsubset%28of%29-787sx.md)
  Returns a Boolean value that indicates whether the set is a strict subset of the given sequence.
- [func isSuperset(of: Set<Element>) -> Bool](./issuperset%28of%29-9iz62.md)
  Returns a Boolean value that indicates whether this set is a superset of the given set.
- [func isSuperset<S>(of: S) -> Bool](./issuperset%28of%29-90hri.md)
  Returns a Boolean value that indicates whether the set is a superset of the given sequence.
- [func isStrictSuperset(of: Set<Element>) -> Bool](./isstrictsuperset%28of%29-4d27m.md)
  Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [func isStrictSuperset<S>(of: S) -> Bool](./isstrictsuperset%28of%29-58ejg.md)
  Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [func isDisjoint<S>(with: S) -> Bool](./isdisjoint%28with%29-2onid.md)
  Returns a Boolean value that indicates whether the set has no members in common with the given sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/isdisjoint(with:)-8ngmk)*