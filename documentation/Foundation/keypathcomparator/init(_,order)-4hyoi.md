# init(_:order:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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
init<Value>(_ keyPath: any KeyPath<Compared, Value?> & Sendable, order: SortOrder = .forward) where Value : Comparable
```

## See Also

### Initializers
- [init<Value, Comparator>(any KeyPath<Compared, Value> & Sendable, comparator: Comparator)](./init%28_,comparator%29-8b13q.md)
- [init<Value, Comparator>(any KeyPath<Compared, Value?> & Sendable, comparator: Comparator)](./init%28_,comparator%29-284rt.md)
- [init<Value, Comparator>(any KeyPath<Compared, Value> & Sendable, comparator: Comparator, order: SortOrder)](./init%28_,comparator,order%29-749jk.md)
- [init<Value, Comparator>(any KeyPath<Compared, Value?> & Sendable, comparator: Comparator, order: SortOrder)](./init%28_,comparator,order%29-3gjxd.md)
- [init<Value>(any KeyPath<Compared, Value> & Sendable, order: SortOrder)](./init%28_,order%29-6r8gw.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/keypathcomparator/init(_:order:)-4hyoi)*