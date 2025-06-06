# prefix(_:)

**Framework**: Combine  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func prefix(_ maxLength: Int) -> Optional<Output>.Publisher
```

## See Also

- [func drop<P>(untilOutputFrom: P) -> Publishers.DropUntilOutput<Self, P>](just/drop(untiloutputfrom:).md)
  Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [func dropFirst(Int) -> Optional<Output>.Publisher](just/dropfirst(_:).md)
- [func drop(while: (Output) -> Bool) -> Optional<Output>.Publisher](just/drop(while:).md)
- [func tryDrop(while: (Self.Output) throws -> Bool) -> Publishers.TryDropWhile<Self>](just/trydrop(while:).md)
  Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [func append(Output...) -> Publishers.Sequence<[Output], Just<Output>.Failure>](just/append(_:)-7eyqj.md)
- [func append<S>(S) -> Publishers.Sequence<[Output], Just<Output>.Failure>](just/append(_:)-7sxlu.md)
- [func prepend<S>(S) -> Publishers.Sequence<[Output], Just<Output>.Failure>](just/prepend(_:)-39e57.md)
- [func prepend(Output...) -> Publishers.Sequence<[Output], Just<Output>.Failure>](just/prepend(_:)-7fg73.md)
- [func prefix(while: (Output) -> Bool) -> Optional<Output>.Publisher](just/prefix(while:).md)
- [func tryPrefix(while: (Self.Output) throws -> Bool) -> Publishers.TryPrefixWhile<Self>](just/tryprefix(while:).md)
  Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [func prefix<P>(untilOutputFrom: P) -> Publishers.PrefixUntilOutput<Self, P>](just/prefix(untiloutputfrom:).md)
  Republishes elements until another publisher emits an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/prefix(_:))*