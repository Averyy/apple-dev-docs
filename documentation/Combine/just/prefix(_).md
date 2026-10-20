# prefix(_:)

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
func prefix(_ maxLength: Int) -> Optional<Output>.Publisher
```

## See Also

### Applying sequence operations to elements
- [func dropFirst(Int) -> Optional<Output>.Publisher](./dropfirst%28_%29.md)
- [func drop(while: (Output) -> Bool) -> Optional<Output>.Publisher](./drop%28while%29.md)
- [func append(Output...) -> Publishers.Sequence<[Output], Just<Output>.Failure>](./append%28_%29-7eyqj.md)
- [func append<S>(S) -> Publishers.Sequence<[Output], Just<Output>.Failure>](./append%28_%29-7sxlu.md)
- [func prepend<S>(S) -> Publishers.Sequence<[Output], Just<Output>.Failure>](./prepend%28_%29-39e57.md)
- [func prepend(Output...) -> Publishers.Sequence<[Output], Just<Output>.Failure>](./prepend%28_%29-7fg73.md)
- [func prefix(while: (Output) -> Bool) -> Optional<Output>.Publisher](./prefix%28while%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/prefix(_:))*