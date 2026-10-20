# tryScan(_:_:)

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
func tryScan<T>(_ initialResult: T, _ nextPartialResult: (T, Output) throws -> T) -> Result<T, any Error>.Publisher
```

## See Also

### Mapping elements
- [func map<T>((Output) -> T) -> Just<T>](./map%28_%29.md)
- [func tryMap<T>((Output) throws -> T) -> Result<T, any Error>.Publisher](./trymap%28_%29.md)
- [func mapError<E>((Just<Output>.Failure) -> E) -> Result<Output, E>.Publisher](./maperror%28_%29.md)
- [func scan<T>(T, (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher](./scan%28_,_%29.md)
- [func setFailureType<E>(to: E.Type) -> Result<Output, E>.Publisher](./setfailuretype%28to%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/tryscan(_:_:))*