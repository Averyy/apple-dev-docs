# AudioDriverKit

**Framework**: AudioDriverKit  
**Kind**: namespace  
**Role**: Namespace

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
namespace AudioDriverKit;
```

## Topics

### Structures
- [IOUserAudioCustomPropertyInfo](./audiodriverkit-page/iouseraudiocustompropertyinfo.md)
  A description of a custom property’s data types.
- [IOUserAudioObjectPropertyAddress](./audiodriverkit-page/iouseraudioobjectpropertyaddress.md)
  An object that collects the three parts — selector, scope, and element — that identify a specific property.
- [IOUserAudioStreamBasicDescription](./audiodriverkit-page/iouseraudiostreambasicdescription.md)
  A structure that encapsulates all of the information for describing the basic format properties of a stream of audio data.
### Variables
- [IOUserAudioIOOperationBeginRead](./audiodriverkit-page/iouseraudioiooperationbeginread.md)
- [IOUserAudioIOOperationWriteEnd](./audiodriverkit-page/iouseraudioiooperationwriteend.md)
- [IOUserAudioObjectPropertyElementMain](./audiodriverkit-page/iouseraudioobjectpropertyelementmain.md)
  The identifier for an audio object’s main element.
- [kIOUserAudioObjectIDDriver](./audiodriverkit-page/kiouseraudioobjectiddriver.md)
  The audio object ID of the driver.
### Type Aliases
- [IOOperationHandler](./audiodriverkit-page/iooperationhandler.md)
- [IOUserAudioIOOperation](./audiodriverkit-page/iouseraudioiooperation.md)
- [IOUserAudioObjectID](./audiodriverkit-page/iouseraudioobjectid.md)
  An identifier that provides a handle on a specific audio object.
- [IOUserAudioObjectPropertyElement](./audiodriverkit-page/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertySelector](./audiodriverkit-page/iouseraudioobjectpropertyselector.md)
  A four character code which, along with the scope and element, specific piece of information about an audio object.
### Enumerations
- [IOUserAudioChannelLabel](./audiodriverkit-page/iouseraudiochannellabel.md)
  Constants to set the preferred channel layout on an audio device.
- [IOUserAudioClassID](./audiodriverkit-page/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [IOUserAudioClockAlgorithm](./audiodriverkit-page/iouseraudioclockalgorithm.md)
  Values that describe clock-smoothing algorithms.
- [IOUserAudioCustomPropertyDataType](./audiodriverkit-page/iouseraudiocustompropertydatatype.md)
  A data and qualifier type used for custom properties.
- [IOUserAudioDeviceTransportState](./audiodriverkit-page/iouseraudiodevicetransportstate.md)
- [IOUserAudioFormatFlags](./audiodriverkit-page/iouseraudioformatflags.md)
  Flag values that provide more information about the format used by an audio stream basic description.
- [IOUserAudioFormatID](./audiodriverkit-page/iouseraudioformatid.md)
  An enumeration of four character codes used to identify distinct audio data formats.
- [IOUserAudioObjectPropertyScope](./audiodriverkit-page/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.
- [IOUserAudioReservedConfigChangeAction](./audiodriverkit-page/iouseraudioreservedconfigchangeaction.md)
  Identifiers for object state changes that require a configuration change.
- [IOUserAudioStartStopFlags](./audiodriverkit-page/iouseraudiostartstopflags.md)
  Values that indicate I/O starts or stops.
- [IOUserAudioStreamDirection](./audiodriverkit-page/iouseraudiostreamdirection.md)
  A type representing the direction of audio flow.
- [IOUserAudioStreamTerminalType](./audiodriverkit-page/iouseraudiostreamterminaltype.md)
  Constants that describe the terminal type of an audio stream.
- [IOUserAudioTransportType](./audiodriverkit-page/iouseraudiotransporttype.md)
  The type of transport to deliver audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit)*