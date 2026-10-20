# isEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the channel is in an enabled state.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

#### Discussion

By default, a connection enables all audio channels that it exposes. You can set this value to [`false`](../../Swift/false.md) to stop the flow of data for a particular channel.

## See Also

### Configuring a channel
- [var volume: Float](./volume.md)
  The current volume (gain) of the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiochannel/isenabled)*