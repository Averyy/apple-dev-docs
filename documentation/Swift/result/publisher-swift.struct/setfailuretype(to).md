# setFailureType(to:)

**Framework**: Swift  
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
func setFailureType<E>(to failureType: E.Type) -> Result<Result<Success, Failure>.Publisher.Output, E>.Publisher where E : Error
```

Available when `Failure` is `Never`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/setfailuretype(to:))*