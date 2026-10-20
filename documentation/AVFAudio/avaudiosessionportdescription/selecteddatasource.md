# selectedDataSource

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The currently selected audio data source for the port.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var selectedDataSource: AVAudioSessionDataSourceDescription? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVAudioSessionDataSourceDescription * selectedDataSource;
```

#### Discussion

If this property returns `nil`, the port doesn’t support selecting between multiple data sources.

## See Also

### Managing a port’s data sources
- [var dataSources: [AVAudioSessionDataSourceDescription]?](./datasources.md)
  The available data sources for the port.
- [var preferredDataSource: AVAudioSessionDataSourceDescription?](./preferreddatasource.md)
  The preferred audio data source for the port.
- [func setPreferredDataSource(AVAudioSessionDataSourceDescription?) throws](./setpreferreddatasource%28_%29.md)
  Sets the preferred audio data source for the port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription/selecteddatasource)*