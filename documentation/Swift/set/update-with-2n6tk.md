# update(with:)

**Framework**: Swift  
**Kind**: method

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
mutating func update(with newMember: Element) -> Element?
```

#### Return Value

An element equal to `newMember` if the set already contained such a member; otherwise, `nil`. In some cases, the returned element may be distinguishable from `newMember` by identity comparison or some other means.

#### Discussion

If an element equal to `newMember` is already contained in the set, `newMember` replaces the existing element. In this example, an existing element is inserted into `classDays`, a set of days of the week.

```swift
enum DayOfTheWeek: Int {
    case sunday, monday, tuesday, wednesday, thursday,
        friday, saturday
}

var classDays: Set<DayOfTheWeek> = [.monday, .wednesday, .friday]
print(classDays.update(with: .monday))
// Prints "Optional(DayOfTheWeek.monday)"
```

## Parameters

- `newMember`: An element to insert into the set.

## See Also

- [func insert(Element) -> (inserted: Bool, memberAfterInsert: Element)](set/insert(_:)-nads.md)
  Inserts the given element in the set if it is not already present.
- [func insert<ConcreteElement>(ConcreteElement) -> (inserted: Bool, memberAfterInsert: ConcreteElement)](set/insert(_:)-yar4.md)
- [func update<ConcreteElement>(with: ConcreteElement) -> ConcreteElement?](set/update(with:)-7r2g.md)
- [func reserveCapacity(Int)](set/reservecapacity(_:).md)
  Reserves enough space to store the specified number of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/update(with:)-2n6tk)*