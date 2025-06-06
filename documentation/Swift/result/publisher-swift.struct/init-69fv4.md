# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a publisher that immediately terminates upon subscription with the given failure.

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
init(_ failure: Failure)
```

## Parameters

- `failure`: The failure to send when terminating.

## See Also

- [init(Result<Result<Success, Failure>.Publisher.Output, Failure>)](result/publisher-swift.struct/init(_:)-516t.md)
  Creates a publisher that delivers the specified result.
- [init(Result<Success, Failure>.Publisher.Output)](result/publisher-swift.struct/init(_:)-7t2tt.md)
  Creates a publisher that sends the specified output to all subscribers and finishes normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/publisher-swift.struct/init(_:)-69fv4)*