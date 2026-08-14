# isEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the channel is in an enabled state.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

By default, a connection enables all audio channels that it exposes. You can set this value to [`false`](https://developer.apple.com/documentation/swift/false) to stop the flow of data for a particular channel.

## See Also

- [var volume: Float](avcaptureaudiochannel/volume.md)
  The current volume (gain) of the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiochannel/isenabled)*