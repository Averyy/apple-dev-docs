# IOUserAudioBox

**Framework**: AudioDriverKit  
**Kind**: class

A container for other audio objects, typically audio devices and audio clock devices.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserAudioBox;
```

#### Overview

Along with containing other audio objects, [`IOUserAudioBox`](iouseraudiobox.md) publishes identifying information about itself and allows you to enable or disable the box. When disabled, the box’s contents aren’t available.

## Topics

### Creating an Audio Box
- [Create](iouseraudiobox/create.md)
  Allocates and initializes an instance of the audio box class.
- [init](iouseraudiobox/init.md)
  Initializes an instance of the audio box class.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
### Freeing an Audio Box
- [free](iouseraudiobox/free.md)
  Frees the audio box.
### Getting Information About the Class
- [GetClassID](iouseraudiobox/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudiobox/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
### Identifying the Box
- [GetUID](iouseraudiobox/getuid.md)
  Returns the UID of the audio box.
### Managing Box Contents
- [AddDevice](iouseraudiobox/adddevice.md)
  Adds an audio device to the audio box.
- [RemoveDevice](iouseraudiobox/removedevice.md)
  Removes an audio device from the audio box.
- [IOUserAudioDevice](iouseraudiodevice.md)
  An audio clock device object that handles the configurations for running I/O.
- [AddClockDevice](iouseraudiobox/addclockdevice.md)
  Adds an audio clock device to the audio box.
- [RemoveClockDevice](iouseraudiobox/removeclockdevice.md)
  Adds an audio clock device to the audio box.
- [IOUserAudioClockDevice](iouseraudioclockdevice.md)
  An audio clock device object, used to synchronize and perform I/O.
### Managing Protection State
- [SetIsProtected](iouseraudiobox/setisprotected.md)
  Sets a Boolean value that indicates if the box requires authentication before use.
- [IsProtected](iouseraudiobox/isprotected.md)
  Returns a Boolean value that indicates if the box requires authentication before use.
### Managing Acquirability
- [HandleChangeAcquireBox](iouseraudiobox/handlechangeacquirebox.md)
  Informs the box of a change to its acquisition state.
- [SetIsAcquired](iouseraudiobox/setisacquired.md)
  Set the box’s acquisition state.
- [IsAcquired](iouseraudiobox/isacquired.md)
  Returns a Boolean value that indicates the box’s acquisition state.
- [SetIsAcquirable](iouseraudiobox/setisacquirable.md)
  Set the box’s acquirability state.
- [IsAcquirable](iouseraudiobox/isacquirable.md)
  Returns a Boolean value that indicates the box’s acquirabilty state.
- [SetAcquisitionFailure](iouseraudiobox/setacquisitionfailure.md)
  Sets the error code to return when box acquisition fails.
- [GetAcquisitionFailure](iouseraudiobox/getacquisitionfailure.md)
  Returns the error code for use when box acquisition fails.
### Determining Media Support
- [SetHasAudio](iouseraudiobox/sethasaudio.md)
  Sets a Boolean value that indicates the box’s audio support.
- [HasAudio](iouseraudiobox/hasaudio.md)
  Returns a Boolean value that indicates the box’s audio support.
- [SetHasVideo](iouseraudiobox/sethasvideo.md)
  Sets a Boolean value that indicates the box’s video support.
- [HasVideo](iouseraudiobox/hasvideo.md)
  Returns a Boolean value that indicates the box’s video support.
- [SetHasMIDI](iouseraudiobox/sethasmidi.md)
  Sets a Boolean value that indicates the box’s MIDI support.
- [HasMIDI](iouseraudiobox/hasmidi.md)
  Returns a Boolean value that indicates the box’s MIDI support.
### Working with Transport Types
- [SetTransportType](iouseraudiobox/settransporttype.md)
  Sets the box’s transport type.
- [GetTransportType](iouseraudiobox/gettransporttype.md)
  Returns the box’s transport type.
- [IOUserAudioTransportType](audiodriverkit/iouseraudiotransporttype.md)
  The type of transport to deliver audio.

## Relationships

### Inherits From
- [IOUserAudioObject](iouseraudioobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox)*