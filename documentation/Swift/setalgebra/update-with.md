# update(with:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Inserts the given element into the set unconditionally.

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
@discardableResult
mutating func update(with newMember: Self.Element) -> Self.Element?
```

#### Return Value

For ordinary sets, an element equal to `newMember` if the set already contained such a member; otherwise, `nil`. In some cases, the returned element may be distinguishable from `newMember` by identity comparison or some other means.

For sets where the set type and element type are the same, like `OptionSet` types, this method returns any intersection between the set and `[newMember]`, or `nil` if the intersection is empty.

#### Discussion

If an element equal to `newMember` is already contained in the set, `newMember` replaces the existing element. In this example, an existing element is inserted into `classDays`, a set of days of the week.

```swift
enum DayOfTheWeek: Int {
    case sunday, monday, tuesday, wednesday, thursday,
        friday, saturday
}

var classDays: Set<DayOfTheWeek> = [.monday, .wednesday, .friday]
print(classDays.update(with: .monday))
// Prints "Optional(.monday)"
```

## Parameters

- `newMember`: An element to insert into the set.

## See Also

- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](setalgebra/insert(_:).md)
  Inserts the given element in the set if it is not already present.
- [func remove(Self.Element) -> Self.Element?](setalgebra/remove(_:).md)
  Removes the given element and any elements subsumed by the given element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra/update(with:))*