# dataSources

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) NSArray<AVAudioSessionDataSourceDescription *> * dataSources;
```

#### Discussion

This feature is only supported on certain devices and peripherals; for example, the data sources represent front- and rear-facing microphones on a device.

Some, but not all, USB ports provide a set of data sources. For example, a USB audio interface may allow you to select between a built-in microphone or external microphone input. The output side may allow you to select between headphones or externally powered speakers. The audio session interface represents the input and output sides of the USB interface as two separate ports of type [`usbAudio`](../avaudiosession/port/usbaudio.md).

If this property is `nil`, the port doesn’t support selecting between multiple data sources.

The contents of this array may change if you change the audio session’s mode.

## See Also

### Managing a port’s data sources
- [var selectedDataSource: AVAudioSessionDataSourceDescription?](./selecteddatasource.md)
  The currently selected audio data source for the port.
- [var preferredDataSource: AVAudioSessionDataSourceDescription?](./preferreddatasource.md)
  The preferred audio data source for the port.
- [func setPreferredDataSource(AVAudioSessionDataSourceDescription?) throws](./setpreferreddatasource%28_%29.md)
  Sets the preferred audio data source for the port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription/datasources)*