# AVAudioSessionDataSourceDescription

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that defines a data source for an audio input or output, giving information such as the source’s name, location, and orientation.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioSessionDataSourceDescription
```

```objc
@interface AVAudioSessionDataSourceDescription : NSObject
```

## Overview

You obtain data source descriptions from the shared [`AVAudioSession`](./avaudiosession.md) object or the [`AVAudioSessionPortDescription`](./avaudiosessionportdescription.md) objects corresponding to its input and output ports. Only built-in microphone ports on certain devices support the location, orientation, and polar pattern properties. If a port doesn’t support these features, the value of its [`dataSources`](./avaudiosessionportdescription/datasources.md) property is `nil`.

This class is especially useful for differentiating between microphone configurations on devices having more than one built-in microphone. Such devices may also support signal processing features for spatial filtering, or *beamforming*, in which the system makes the device more sensitive to audio signals from a particular direction. See `Data Source Polar Patterns` for more information.

## Topics

### Identifying a data source
- [var dataSourceID: NSNumber](./avaudiosessiondatasourcedescription/datasourceid.md)
  The system-assigned identifier for the data source.
- [var dataSourceName: String](./avaudiosessiondatasourcedescription/datasourcename.md)
  A human-readable name for the data source.
### Retrieving the data source location
- [var location: AVAudioSession.Location?](./avaudiosessiondatasourcedescription/location.md)
  The location of the data source on the device.
- [AVAudioSession.Location](./avaudiosession/location.md)
  Constants that describe the location of the data source on device.
### Retrieving the data source orientation
- [var orientation: AVAudioSession.Orientation?](./avaudiosessiondatasourcedescription/orientation.md)
  The orientation of the data source relative to the device’s natural orientation.
- [AVAudioSession.Orientation](./avaudiosession/orientation.md)
  Constants that indicate the directions in which a data source can point, relative to the device’s natural orientation.
### Configuring microphone directivity
- [var selectedPolarPattern: AVAudioSession.PolarPattern?](./avaudiosessiondatasourcedescription/selectedpolarpattern.md)
  The data source’s active polar pattern.
- [var supportedPolarPatterns: [AVAudioSession.PolarPattern]?](./avaudiosessiondatasourcedescription/supportedpolarpatterns.md)
  The set of directivity configurations supported by the data source.
- [var preferredPolarPattern: AVAudioSession.PolarPattern?](./avaudiosessiondatasourcedescription/preferredpolarpattern.md)
  The preferred directivity configuration for the data source.
- [func setPreferredPolarPattern(AVAudioSession.PolarPattern?) throws](./avaudiosessiondatasourcedescription/setpreferredpolarpattern%28_%29.md)
  Selects the preferred directivity configuration for the data source.
- [AVAudioSession.PolarPattern](./avaudiosession/polarpattern.md)
  Constants that describe the possible polar patterns of the data source on an iOS device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring outputs
- [var outputDataSources: [AVAudioSessionDataSourceDescription]?](./avaudiosession/outputdatasources.md)
  An array of available output data sources for the current audio route.
- [var outputDataSource: AVAudioSessionDataSourceDescription?](./avaudiosession/outputdatasource.md)
  The currently selected output data source.
- [func setOutputDataSource(AVAudioSessionDataSourceDescription?) throws](./avaudiosession/setoutputdatasource%28_%29.md)
  Sets the output data source for an audio session.
- [func overrideOutputAudioPort(AVAudioSession.PortOverride) throws](./avaudiosession/overrideoutputaudioport%28_%29.md)
  Temporarily changes the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondatasourcedescription)*