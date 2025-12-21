# contains(_:)

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
func contains(_ output: Elements.Element) -> Result<Bool, Failure>.Publisher
```

## See Also

- [func contains(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Result<Bool, Failure>.Publisher](publishers/sequence/contains(where:).md)
- [func tryContains(where: (Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](publishers/sequence/trycontains(where:).md)
- [func allSatisfy((Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Result<Bool, Failure>.Publisher](publishers/sequence/allsatisfy(_:).md)
- [func tryAllSatisfy((Publishers.Sequence<Elements, Failure>.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](publishers/sequence/tryallsatisfy(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/contains(_:))*