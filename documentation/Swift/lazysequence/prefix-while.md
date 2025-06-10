# prefix(while:)

**Framework**: Swift  
**Kind**: method

Returns a lazy sequence of the initial consecutive elements that satisfy `predicate`.

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
func prefix(while predicate: @escaping (Self.Elements.Element) -> Bool) -> LazyPrefixWhileSequence<Self.Elements>
```

## Parameters

- `predicate`: A closure that takes an element of the sequence as   its argument and returns   if the element should be included or    otherwise. Once   returns   it will not be   called again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazysequence/prefix(while:))*