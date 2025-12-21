# allSatisfy(_:)

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
func allSatisfy(_ predicate: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Result<Bool, Failure>.Publisher
```

## See Also

- [func contains(Elements.Element) -> Result<Bool, Failure>.Publisher](publishers/sequence/contains(_:).md)
- [func contains(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Result<Bool, Failure>.Publisher](publishers/sequence/contains(where:).md)
- [func tryContains(where: (Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](publishers/sequence/trycontains(where:).md)
- [func tryAllSatisfy((Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](publishers/sequence/tryallsatisfy(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/allsatisfy(_:))*