# update(with:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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
mutating func update<ConcreteElement>(with newMember: ConcreteElement) -> ConcreteElement? where ConcreteElement : Hashable
```

Available when `Element` is `AnyHashable`.

## See Also

### Adding Elements
- [func insert(Element) -> (inserted: Bool, memberAfterInsert: Element)](./insert%28_%29-nads.md)
  Inserts the given element in the set if it is not already present.
- [func insert<ConcreteElement>(ConcreteElement) -> (inserted: Bool, memberAfterInsert: ConcreteElement)](./insert%28_%29-yar4.md)
- [func update(with: Element) -> Element?](./update%28with%29-2n6tk.md)
  Inserts the given element into the set unconditionally.
- [func reserveCapacity(Int)](./reservecapacity%28_%29.md)
  Reserves enough space to store the specified number of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/update(with:)-7r2g)*