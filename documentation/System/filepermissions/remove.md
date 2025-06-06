# remove(_:)

**Framework**: System  
**Kind**: method

Removes the given element and all elements subsumed by it.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@discardableResult
mutating func remove(_ member: Self.Element) -> Self.Element?
```

#### Return Value

The intersection of `[member]` and the set, if the intersection was nonempty; otherwise, `nil`.

#### Discussion

In the following example, the `.priority` shipping option is removed from the `options` option set. Attempting to remove the same shipping option a second time results in `nil`, because `options` no longer contains `.priority` as a member.

```swift
var options: ShippingOptions = [.secondDay, .priority]
let priorityOption = options.remove(.priority)
print(priorityOption == .priority)
// Prints "true"

print(options.remove(.priority))
// Prints "nil"
```

In the next example, the `.express` element is passed to `remove(_:)`. Although `.express` is not a member of `options`, `.express` subsumes the remaining `.secondDay` element of the option set. Therefore, `options` is emptied and the intersection between `.express` and `options` is returned.

```swift
let expressOption = options.remove(.express)
print(expressOption == .express)
// Prints "false"
print(expressOption == .secondDay)
// Prints "true"
```

## Parameters

- `member`: The element of the set to remove.

## See Also

- [init()](filepermissions/init.md)
  Creates an empty option set.
- [init<S>(S)](filepermissions/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](filepermissions/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [func contains(Self) -> Bool](filepermissions/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](filepermissions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formIntersection(Self)](filepermissions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](filepermissions/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func formUnion(Self)](filepermissions/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](filepermissions/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](filepermissions/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func isDisjoint(with: Self) -> Bool](filepermissions/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [var isEmpty: Bool](filepermissions/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [func isStrictSubset(of: Self) -> Bool](filepermissions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](filepermissions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](filepermissions/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepermissions/remove(_:))*