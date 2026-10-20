# tryAllSatisfy(_:)

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
func tryAllSatisfy(_ predicate: (Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher
```

Available when `Elements` conforms to `Sequence` and `Failure` conforms to `Error`.

## See Also

### Applying matching criteria to elements
- [func contains(Elements.Element) -> Result<Bool, Failure>.Publisher](./contains%28_%29.md)
- [func contains(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Result<Bool, Failure>.Publisher](./contains%28where%29.md)
- [func tryContains(where: (Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](./trycontains%28where%29.md)
- [func allSatisfy((Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Result<Bool, Failure>.Publisher](./allsatisfy%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/tryallsatisfy(_:))*