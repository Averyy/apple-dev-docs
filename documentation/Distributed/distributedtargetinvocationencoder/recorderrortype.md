# recordErrorType(_:)

**Framework**: Distributed  
**Kind**: method  
**Required**: Yes

Record the error type of the distributed method. This method will not be invoked if the target is not throwing.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
mutating func recordErrorType<E>(_ type: E.Type) throws where E : Error
```

## Parameters

- `type`: The type of error that was declared to be thrown by the invocation target. Currently this can only ever be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedtargetinvocationencoder/recorderrortype(_:))*