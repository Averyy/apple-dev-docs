# insert(_:)

**Framework**: Swift  
**Kind**: method

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
mutating func insert<ConcreteElement>(_ newMember: ConcreteElement) -> (inserted: Bool, memberAfterInsert: ConcreteElement) where ConcreteElement : Hashable
```

## See Also

- [func insert(Element) -> (inserted: Bool, memberAfterInsert: Element)](set/insert(_:)-nads.md)
  Inserts the given element in the set if it is not already present.
- [func update(with: Element) -> Element?](set/update(with:)-2n6tk.md)
  Inserts the given element into the set unconditionally.
- [func update<ConcreteElement>(with: ConcreteElement) -> ConcreteElement?](set/update(with:)-7r2g.md)
- [func reserveCapacity(Int)](set/reservecapacity(_:).md)
  Reserves enough space to store the specified number of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/insert(_:)-yar4)*