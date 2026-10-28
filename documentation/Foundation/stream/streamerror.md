# streamError

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns an `NSError` object representing the stream error.

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
var streamError: (any Error)? { get }
```

```objc
@property (copy, readonly, nullable) NSError * streamError;
```

## Return Value

An `NSError` object representing the stream error, or `nil` if no error has been encountered.

## See Also

### Getting Stream Information
- [var streamStatus: Stream.Status](./streamstatus.md)
  Returns the receiver’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/streamerror)*