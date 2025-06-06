# dataSources

**Framework**: AVFAudio  
**Kind**: property

The available data sources for the port.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var dataSources: [AVAudioSessionDataSourceDescription]? { get }
```

#### Discussion

This feature is only supported on certain devices and peripherals; for example, the data sources represent front- and rear-facing microphones on a device.

Some, but not all, USB ports provide a set of data sources. For example, a USB audio interface may allow you to select between a built-in microphone or external microphone input. The output side may allow you to select between headphones or externally powered speakers. The audio session interface represents the input and output sides of the USB interface as two separate ports of type [`usbAudio`](avaudiosession/port/usbaudio.md).

If this property is `nil`, the port doesn’t support selecting between multiple data sources.

The contents of this array may change if you change the audio session’s mode.

## See Also

- [var selectedDataSource: AVAudioSessionDataSourceDescription?](avaudiosessionportdescription/selecteddatasource.md)
  The currently selected audio data source for the port.
- [var preferredDataSource: AVAudioSessionDataSourceDescription?](avaudiosessionportdescription/preferreddatasource.md)
  The preferred audio data source for the port.
- [func setPreferredDataSource(AVAudioSessionDataSourceDescription?) throws](avaudiosessionportdescription/setpreferreddatasource(_:).md)
  Sets the preferred audio data source for the port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription/datasources)*