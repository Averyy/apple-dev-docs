# tryReduce(_:_:)

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
func tryReduce<T>(_ initialResult: T, _ nextPartialResult: (T, Output) throws -> T) -> Result<T, any Error>.Publisher
```

## See Also

### Reducing elements
- [func collect() -> Just<[Output]>](./collect%28%29.md)
- [func ignoreOutput() -> Empty<Output, Just<Output>.Failure>](./ignoreoutput%28%29.md)
- [func reduce<T>(T, (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher](./reduce%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/tryreduce(_:_:))*