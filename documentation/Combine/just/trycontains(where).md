# tryContains(where:)

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
func tryContains(where predicate: (Output) throws -> Bool) -> Result<Bool, any Error>.Publisher
```

## See Also

### Applying matching criteria to elements
- [func contains(Output) -> Just<Bool>](./contains%28_%29.md)
- [func contains(where: (Output) -> Bool) -> Just<Bool>](./contains%28where%29.md)
- [func allSatisfy((Output) -> Bool) -> Just<Bool>](./allsatisfy%28_%29.md)
- [func tryAllSatisfy((Output) throws -> Bool) -> Result<Bool, any Error>.Publisher](./tryallsatisfy%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/trycontains(where:))*