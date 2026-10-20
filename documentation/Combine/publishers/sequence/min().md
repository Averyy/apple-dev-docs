# min()

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
func min() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher
```

Available when `Elements` conforms to `Sequence`, `Failure` is `Never`, and `Elements.Element` conforms to `Comparable`.

## See Also

### Applying mathematical operations on elements
- [func count() -> Just<Int>](./count%28%29-5rrw2.md)
- [func count() -> Result<Int, Failure>.Publisher](./count%28%29-5hb52.md)
- [func count() -> Result<Int, Failure>.Publisher](./count%28%29-b8ct.md)
- [func max() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./max%28%29.md)
- [func max(by: (Publishers.Sequence<Elements, Failure>.Output, Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./max%28by%29.md)
- [func min(by: (Publishers.Sequence<Elements, Failure>.Output, Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./min%28by%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/min())*