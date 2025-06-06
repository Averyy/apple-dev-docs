# preferredDataSource

**Framework**: AVFAudio  
**Kind**: property

The preferred audio data source for the port.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preferredDataSource: AVAudioSessionDataSourceDescription? { get }
```

#### Discussion

The value of this property indicates the data source selected using the [`setPreferredDataSource(_:)`](avaudiosessionportdescription/setpreferreddatasource(_:).md) method. To see the actual data source, use the [`selectedDataSource`](avaudiosessionportdescription/selecteddatasource.md) property.

If `nil`, the port doesn’t support selecting between multiple data sources, or no preferred data source has been selected.

## See Also

- [var dataSources: [AVAudioSessionDataSourceDescription]?](avaudiosessionportdescription/datasources.md)
  The available data sources for the port.
- [var selectedDataSource: AVAudioSessionDataSourceDescription?](avaudiosessionportdescription/selecteddatasource.md)
  The currently selected audio data source for the port.
- [func setPreferredDataSource(AVAudioSessionDataSourceDescription?) throws](avaudiosessionportdescription/setpreferreddatasource(_:).md)
  Sets the preferred audio data source for the port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription/preferreddatasource)*