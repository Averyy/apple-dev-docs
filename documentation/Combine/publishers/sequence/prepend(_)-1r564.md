# prepend(_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

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
func prepend<S>(_ elements: S) -> Publishers.Sequence<Elements, Failure> where S : Sequence, Elements.Element == S.Element
```

Available when `Elements` conforms to `RangeReplaceableCollection` and `Failure` conforms to `Error`.

## See Also

### Applying sequence operations to elements
- [func dropFirst(Int) -> Publishers.Sequence<DropFirstSequence<Elements>, Failure>](./dropfirst%28_%29.md)
- [func drop(while: (Elements.Element) -> Bool) -> Publishers.Sequence<DropWhileSequence<Elements>, Failure>](./drop%28while%29.md)
- [func append<S>(S) -> Publishers.Sequence<Elements, Failure>](./append%28_%29-45rm8.md)
- [func append(Publishers.Sequence<Elements, Failure>) -> Publishers.Sequence<Elements, Failure>](./append%28_%29-3dj6k.md)
- [func append(Publishers.Sequence<Elements, Failure>.Output...) -> Publishers.Sequence<Elements, Failure>](./append%28_%29-2knh4.md)
- [func prepend(Publishers.Sequence<Elements, Failure>) -> Publishers.Sequence<Elements, Failure>](./prepend%28_%29-71f7p.md)
- [func prepend(Publishers.Sequence<Elements, Failure>.Output...) -> Publishers.Sequence<Elements, Failure>](./prepend%28_%29-2ros1.md)
- [func prefix(Int) -> Publishers.Sequence<PrefixSequence<Elements>, Failure>](./prefix%28_%29.md)
- [func prefix(while: (Elements.Element) -> Bool) -> Publishers.Sequence<[Elements.Element], Failure>](./prefix%28while%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/prepend(_:)-1r564)*