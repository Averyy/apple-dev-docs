# init(_:order:)

**Framework**: Foundation  
**Kind**: init

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init<Value>(_ keyPath: any KeyPath<Compared, Value> & Sendable, order: SortOrder = .forward) where Value : Comparable
```

## See Also

- [init<Value, Comparator>(any KeyPath<Compared, Value> & Sendable, comparator: Comparator)](keypathcomparator/init(_:comparator:)-8b13q.md)
- [init<Value, Comparator>(any KeyPath<Compared, Value?> & Sendable, comparator: Comparator)](keypathcomparator/init(_:comparator:)-284rt.md)
- [init<Value, Comparator>(any KeyPath<Compared, Value> & Sendable, comparator: Comparator, order: SortOrder)](keypathcomparator/init(_:comparator:order:)-749jk.md)
- [init<Value, Comparator>(any KeyPath<Compared, Value?> & Sendable, comparator: Comparator, order: SortOrder)](keypathcomparator/init(_:comparator:order:)-3gjxd.md)
- [init<Value>(any KeyPath<Compared, Value?> & Sendable, order: SortOrder)](keypathcomparator/init(_:order:)-4hyoi.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/keypathcomparator/init(_:order:)-6r8gw)*