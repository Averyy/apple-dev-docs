# tryContains(where:)

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
func tryContains(where predicate: (Result<Success, Failure>.Publisher.Output) throws -> Bool) -> Result<Bool, any Error>.Publisher
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/trycontains(where:))*