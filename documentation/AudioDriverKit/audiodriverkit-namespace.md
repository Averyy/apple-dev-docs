# AudioDriverKit

**Framework**: AudioDriverKit  
**Kind**: namespace

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
namespace AudioDriverKit;
```

## Topics

### Structures
- [IOUserAudioCustomPropertyInfo](audiodriverkit/iouseraudiocustompropertyinfo.md)
  A description of a custom property’s data types.
- [IOUserAudioObjectPropertyAddress](audiodriverkit/iouseraudioobjectpropertyaddress.md)
  An object that collects the three parts — selector, scope, and element — that identify a specific property.
- [IOUserAudioStreamBasicDescription](audiodriverkit/iouseraudiostreambasicdescription.md)
  A structure that encapsulates all of the information for describing the basic format properties of a stream of audio data.
### Variables
- [IOUserAudioIOOperationBeginRead](audiodriverkit/iouseraudioiooperationbeginread.md)
- [IOUserAudioIOOperationWriteEnd](audiodriverkit/iouseraudioiooperationwriteend.md)
- [IOUserAudioObjectPropertyElementMain](audiodriverkit/iouseraudioobjectpropertyelementmain.md)
  The identifier for an audio object’s main element.
- [kIOUserAudioObjectIDDriver](audiodriverkit/kiouseraudioobjectiddriver.md)
  The audio object ID of the driver.
### Type Aliases
- [IOOperationHandler](audiodriverkit/iooperationhandler.md)
- [IOUserAudioIOOperation](audiodriverkit/iouseraudioiooperation.md)
- [IOUserAudioObjectID](audiodriverkit/iouseraudioobjectid.md)
  An identifier that provides a handle on a specific audio object.
- [IOUserAudioObjectPropertyElement](audiodriverkit/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertySelector](audiodriverkit/iouseraudioobjectpropertyselector.md)
  A four character code which, along with the scope and element, specific piece of information about an audio object.
### Enumerations
- [IOUserAudioChannelLabel](audiodriverkit/iouseraudiochannellabel.md)
  Constants to set the preferred channel layout on an audio device.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [IOUserAudioClockAlgorithm](audiodriverkit/iouseraudioclockalgorithm.md)
  Values that describe clock-smoothing algorithms.
- [IOUserAudioCustomPropertyDataType](audiodriverkit/iouseraudiocustompropertydatatype.md)
  A data and qualifier type used for custom properties.
- [IOUserAudioDeviceTransportState](audiodriverkit/iouseraudiodevicetransportstate.md)
- [IOUserAudioFormatFlags](audiodriverkit/iouseraudioformatflags.md)
  Flag values that provide more information about the format used by an audio stream basic description.
- [IOUserAudioFormatID](audiodriverkit/iouseraudioformatid.md)
  An enumeration of four character codes used to identify distinct audio data formats.
- [IOUserAudioObjectPropertyScope](audiodriverkit/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.
- [IOUserAudioReservedConfigChangeAction](audiodriverkit/iouseraudioreservedconfigchangeaction.md)
  Identifiers for object state changes that require a configuration change.
- [IOUserAudioStartStopFlags](audiodriverkit/iouseraudiostartstopflags.md)
  Values that indicate I/O starts or stops.
- [IOUserAudioStreamDirection](audiodriverkit/iouseraudiostreamdirection.md)
  A type representing the direction of audio flow.
- [IOUserAudioStreamTerminalType](audiodriverkit/iouseraudiostreamterminaltype.md)
  Constants that describe the terminal type of an audio stream.
- [IOUserAudioTransportType](audiodriverkit/iouseraudiotransporttype.md)
  The type of transport to deliver audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit)*