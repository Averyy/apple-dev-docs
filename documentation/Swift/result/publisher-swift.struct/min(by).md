# min(by:)

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
func min(by areInIncreasingOrder: (Result<Success, Failure>.Publisher.Output, Result<Success, Failure>.Publisher.Output) -> Bool) -> Result<Result<Success, Failure>.Publisher.Output, Failure>.Publisher
```

Available when `Failure` conforms to `Error`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/min(by:))*