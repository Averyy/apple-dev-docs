# streamStatus

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the receiver’s status.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var streamStatus: Stream.Status { get }
```

```objc
@property (readonly) NSStreamStatus streamStatus;
```

## Return Value

The receiver’s status.

## Discussion

See Constants for a description of the available NSStreamStatus constants.

## See Also

### Getting Stream Information
- [var streamError: (any Error)?](./streamerror.md)
  Returns an `NSError` object representing the stream error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/streamstatus)*