# error

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The error that caused the player item to fail.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
var error: (any Error)? { get }
```

```objc
@property (readonly, nullable) NSError * error;
```

#### Discussion

The value of this property is an error that describes what caused the player item to no longer be able to be played.

If the receiver’s status is not [`AVPlayerItem.Status.failed`](./status-swift.enum/failed.md), the value of this property is `nil`.

## See Also

### Determining readiness
- [var status: AVPlayerItem.Status](./status-swift.property.md)
  The status of the player item.
- [AVPlayerItem.Status](./status-swift.enum.md)
  The statuses for a player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/error)*