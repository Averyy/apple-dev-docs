# ignoreOutput()

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
func ignoreOutput() -> Empty<Output, Just<Output>.Failure>
```

## See Also

- [func collect() -> Just<[Output]>](just/collect.md)
- [func reduce<T>(T, (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher](just/reduce(_:_:).md)
- [func tryReduce<T>(T, (T, Output) throws -> T) -> Result<T, any Error>.Publisher](just/tryreduce(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/ignoreoutput())*