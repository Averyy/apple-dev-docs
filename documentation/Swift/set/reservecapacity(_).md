# reserveCapacity(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Reserves enough space to store the specified number of elements.

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
mutating func reserveCapacity(_ minimumCapacity: Int)
```

Available when `Element` conforms to `Hashable`.

## Discussion

If you are adding a known number of elements to a set, use this method to avoid multiple reallocations. This method ensures that the set has unique, mutable, contiguous storage, with space allocated for at least the requested number of elements.

Calling the `reserveCapacity(_:)` method on a set with bridged storage triggers a copy to contiguous storage even if the existing storage has room to store `minimumCapacity` elements.

## Parameters

- `minimumCapacity`: The requested number of elements to store.

## See Also

### Adding Elements
- [func insert(Element) -> (inserted: Bool, memberAfterInsert: Element)](./insert%28_%29-nads.md)
  Inserts the given element in the set if it is not already present.
- [func insert<ConcreteElement>(ConcreteElement) -> (inserted: Bool, memberAfterInsert: ConcreteElement)](./insert%28_%29-yar4.md)
- [func update(with: Element) -> Element?](./update%28with%29-2n6tk.md)
  Inserts the given element into the set unconditionally.
- [func update<ConcreteElement>(with: ConcreteElement) -> ConcreteElement?](./update%28with%29-7r2g.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/reservecapacity(_:))*