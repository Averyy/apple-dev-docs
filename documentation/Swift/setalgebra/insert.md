# insert(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Inserts the given element in the set if it is not already present.

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
mutating func insert(_ newMember: Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)
```

#### Return Value

`(true, newMember)` if `newMember` was not contained in the set. If an element equal to `newMember` was already contained in the set, the method returns `(false, oldMember)`, where `oldMember` is the element that was equal to `newMember`. In some cases, `oldMember` may be distinguishable from `newMember` by identity comparison or some other means.

#### Discussion

If an element equal to `newMember` is already contained in the set, this method has no effect. In this example, a new element is inserted into `classDays`, a set of days of the week. When an existing element is inserted, the `classDays` set does not change.

```swift
enum DayOfTheWeek: Int {
    case sunday, monday, tuesday, wednesday, thursday,
        friday, saturday
}

var classDays: Set<DayOfTheWeek> = [.wednesday, .friday]
print(classDays.insert(.monday))
// Prints "(true, .monday)"
print(classDays)
// Prints "[.friday, .wednesday, .monday]"

print(classDays.insert(.friday))
// Prints "(false, .friday)"
print(classDays)
// Prints "[.friday, .wednesday, .monday]"
```

## Parameters

- `newMember`: An element to insert into the set.

## See Also

- [func update(with: Self.Element) -> Self.Element?](setalgebra/update(with:).md)
  Inserts the given element into the set unconditionally.
- [func remove(Self.Element) -> Self.Element?](setalgebra/remove(_:).md)
  Removes the given element and any elements subsumed by the given element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra/insert(_:))*