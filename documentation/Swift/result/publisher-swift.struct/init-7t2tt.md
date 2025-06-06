# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a publisher that sends the specified output to all subscribers and finishes normally.

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
init(_ output: Result<Success, Failure>.Publisher.Output)
```

## Parameters

- `output`: The output to deliver to each subscriber.

## See Also

- [init(Result<Result<Success, Failure>.Publisher.Output, Failure>)](result/publisher-swift.struct/init(_:)-516t.md)
  Creates a publisher that delivers the specified result.
- [init(Failure)](result/publisher-swift.struct/init(_:)-69fv4.md)
  Creates a publisher that immediately terminates upon subscription with the given failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/init(_:)-7t2tt)*