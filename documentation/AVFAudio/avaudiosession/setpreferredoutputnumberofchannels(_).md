# setPreferredOutputNumberOfChannels(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sets the preferred number of output channels for the current route.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setPreferredOutputNumberOfChannels(_ count: Int) throws
```

```objc
- (BOOL) setPreferredOutputNumberOfChannels:(NSInteger) count error:(NSError **) outError;
```

#### Discussion

This method requests a change to the number of output channels. To determine whether the change has taken effect, use the [`outputNumberOfChannels`](./outputnumberofchannels.md) property. For details, see Configuring standard audio behaviors. Requesting output channels less than one or greater than that returned by the [`maximumOutputNumberOfChannels`](./maximumoutputnumberofchannels.md) results in an error. Only certain devices and peripherals support this feature.

Set the preferred number of output channels only after setting the audio session’s category and mode, and activating the session.

## Parameters

- `count`: The number of output channels you want to use.

## See Also

### Setting the number of output channels
- [var preferredOutputNumberOfChannels: Int](./preferredoutputnumberofchannels.md)
  The preferred number of output channels for the current route.
- [var outputNumberOfChannels: Int](./outputnumberofchannels.md)
  The number of audio output channels.
- [var maximumOutputNumberOfChannels: Int](./maximumoutputnumberofchannels.md)
  The maximum number of output channels available for the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setpreferredoutputnumberofchannels(_:))*