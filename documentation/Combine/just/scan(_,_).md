# scan(_:_:)

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
func scan<T>(_ initialResult: T, _ nextPartialResult: (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher
```

## See Also

### Mapping elements
- [func map<T>((Output) -> T) -> Just<T>](./map%28_%29.md)
- [func tryMap<T>((Output) throws -> T) -> Result<T, any Error>.Publisher](./trymap%28_%29.md)
- [func mapError<E>((Just<Output>.Failure) -> E) -> Result<Output, E>.Publisher](./maperror%28_%29.md)
- [func tryScan<T>(T, (T, Output) throws -> T) -> Result<T, any Error>.Publisher](./tryscan%28_,_%29.md)
- [func setFailureType<E>(to: E.Type) -> Result<Output, E>.Publisher](./setfailuretype%28to%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/scan(_:_:))*