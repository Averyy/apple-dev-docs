# tryAllSatisfy(_:)

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
func tryAllSatisfy(_ predicate: (Output) throws -> Bool) -> Result<Bool, any Error>.Publisher
```

## See Also

- [func contains(Output) -> Just<Bool>](just/contains(_:).md)
- [func contains(where: (Output) -> Bool) -> Just<Bool>](just/contains(where:).md)
- [func tryContains(where: (Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](just/trycontains(where:).md)
- [func allSatisfy((Output) -> Bool) -> Just<Bool>](just/allsatisfy(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/tryallsatisfy(_:))*