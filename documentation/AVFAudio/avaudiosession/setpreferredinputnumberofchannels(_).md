# setPreferredInputNumberOfChannels(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sets the preferred number of input channels for the current route.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setPreferredInputNumberOfChannels(_ count: Int) throws
```

```objc
- (BOOL) setPreferredInputNumberOfChannels:(NSInteger) count error:(NSError **) outError;
```

## Discussion

This method requests a change to the number of input channels. To determine whether the change has taken effect, query or key-value observe the [`inputNumberOfChannels`](./inputnumberofchannels.md) property.

Requesting input channels less than one or greater than that returned by the [`maximumInputNumberOfChannels`](./maximuminputnumberofchannels.md) results in an error.

Set the preferred number of input channels only after setting the audio session’s category and mode, and activating the session.

## Parameters

- `count`: The number of input channels you want to use.

## See Also

### Setting the number of input channels
- [var preferredInputNumberOfChannels: Int](./preferredinputnumberofchannels.md)
  The preferred number of input channels for the current route.
- [var inputNumberOfChannels: Int](./inputnumberofchannels.md)
  The number of audio input channels for the current route.
- [var maximumInputNumberOfChannels: Int](./maximuminputnumberofchannels.md)
  The maximum number of input channels available for the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setpreferredinputnumberofchannels(_:))*