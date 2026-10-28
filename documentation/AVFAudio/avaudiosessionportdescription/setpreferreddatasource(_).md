# setPreferredDataSource(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sets the preferred audio data source for the port.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setPreferredDataSource(_ dataSource: AVAudioSessionDataSourceDescription?) throws
```

```objc
- (BOOL) setPreferredDataSource:(AVAudioSessionDataSourceDescription *) dataSource error:(NSError **) outError;
```

## Discussion

Call this method to request a change to the audio session’s preferred data source. To determine whether the change has taken effect, inspect the [`selectedDataSource`](./selecteddatasource.md) property. (For details, see Configuring standard audio behaviors in the [`AVAudioSession`](../avaudiosession.md) class reference).

If the port is in use, changing this setting is likely to result in a route reconfiguration.

Set a preferred data source only after setting the audio session’s category and mode, and activating the session.

## Parameters

- `dataSource`: The data source to use.

## See Also

### Managing a port’s data sources
- [var dataSources: [AVAudioSessionDataSourceDescription]?](./datasources.md)
  The available data sources for the port.
- [var selectedDataSource: AVAudioSessionDataSourceDescription?](./selecteddatasource.md)
  The currently selected audio data source for the port.
- [var preferredDataSource: AVAudioSessionDataSourceDescription?](./preferreddatasource.md)
  The preferred audio data source for the port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription/setpreferreddatasource(_:))*