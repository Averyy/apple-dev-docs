# reduce(_:_:)

**Framework**: Swift  
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
func reduce<T>(_ initialResult: T, _ nextPartialResult: (T, Result<Success, Failure>.Publisher.Output) -> T) -> Result<T, Failure>.Publisher
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/reduce(_:_:))*