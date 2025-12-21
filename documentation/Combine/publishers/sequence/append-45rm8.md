# append(_:)

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
func append<S>(_ elements: S) -> Publishers.Sequence<Elements, Failure> where S : Sequence, Elements.Element == S.Element
```

## See Also

- [func dropFirst(Int) -> Publishers.Sequence<DropFirstSequence<Elements>, Failure>](publishers/sequence/dropfirst(_:).md)
- [func drop(while: (Elements.Element) -> Bool) -> Publishers.Sequence<DropWhileSequence<Elements>, Failure>](publishers/sequence/drop(while:).md)
- [func append(Publishers.Sequence<Elements, Failure>) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/append(_:)-3dj6k.md)
- [func append(Publishers.Sequence<Elements, Failure>.Output...) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/append(_:)-2knh4.md)
- [func prepend<S>(S) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/prepend(_:)-1r564.md)
- [func prepend(Publishers.Sequence<Elements, Failure>) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/prepend(_:)-71f7p.md)
- [func prepend(Publishers.Sequence<Elements, Failure>.Output...) -> Publishers.Sequence<Elements, Failure>](publishers/sequence/prepend(_:)-2ros1.md)
- [func prefix(Int) -> Publishers.Sequence<PrefixSequence<Elements>, Failure>](publishers/sequence/prefix(_:).md)
- [func prefix(while: (Elements.Element) -> Bool) -> Publishers.Sequence<[Elements.Element], Failure>](publishers/sequence/prefix(while:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/append(_:)-45rm8)*