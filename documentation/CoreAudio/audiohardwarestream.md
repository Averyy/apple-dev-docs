# AudioHardwareStream

**Framework**: Core Audio  
**Kind**: class

Instances of the AudioHardwareStream class encapsulate a single audio stream, which represents a single buffer of data for transferring across the user/kernel boundary. As such, AudioStreams are the gatekeepers of format information. Each has its own format and list of available formats.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
class AudioHardwareStream
```

## Topics

### Initializers
- [init(id: AudioObjectID)](audiohardwarestream/init(id:).md)
### Instance Properties
- [var availablePhysicalFormats: [AudioStreamRangedDescription]](audiohardwarestream/availablephysicalformats.md)
  An array of AudioStreamRangedDescriptions that describe the available data formats for the stream. The physical format refers to the data format in which the hardware for the owning device performs its IO transactions.
- [var availableVirtualFormats: [AudioStreamRangedDescription]](audiohardwarestream/availablevirtualformats.md)
  An array of AudioStreamRangedDescriptions that describe the available data formats for the stream. The virtual format refers to the data format in which all IOProcs for the owning device will perform IO transactions.
- [var direction: AudioHardwareDirection](audiohardwarestream/direction.md)
  An AudioHardwareDirection indicating whether this is an input or output stream.
- [var isActive: Bool](audiohardwarestream/isactive.md)
  A Bool where a value of true indicates that the stream is enabled for IO.
- [var latency: Int](audiohardwarestream/latency.md)
  An Int containing the number of frames of latency in the stream.
- [var physicalFormat: AudioStreamBasicDescription](audiohardwarestream/physicalformat.md)
  An AudioStreamBasicDescription that describes the current data format for the stream. The physical format refers to the data format in which the hardware for the owning device performs its IO transactions.
- [var startingChannel: Int](audiohardwarestream/startingchannel.md)
  An Int that specifies the first element in the owning device that corresponds to element one of this stream.
- [var terminalType: UInt32](audiohardwarestream/terminaltype.md)
  A UInt32 whose value describes the general kind of functionality attached to the stream. Constants for some of the values for this property can be found in the enum in the AudioStream Constants section of AudioHardwareBase.h.
- [var virtualFormat: AudioStreamBasicDescription](audiohardwarestream/virtualformat.md)
  An AudioStreamBasicDescription that describes the current data format for the stream. The virtual format refers to the data format in which all IOProcs for the owning device will perform IO transactions.
### Instance Methods
- [func setIsActive(Bool) throws](audiohardwarestream/setisactive(_:).md)
  Set the isActive property.
- [func setPhysicalFormat(AudioStreamBasicDescription) throws](audiohardwarestream/setphysicalformat(_:).md)
  Set the physicalFormat property.
- [func setVirtualFormat(AudioStreamBasicDescription) throws](audiohardwarestream/setvirtualformat(_:).md)
  Set the virtualFormat property.

## Relationships

### Inherits From
- [AudioHardwareObject](audiohardwareobject.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwarestream)*