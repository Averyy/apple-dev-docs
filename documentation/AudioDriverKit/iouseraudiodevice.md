# IOUserAudioDevice

**Framework**: AudioDriverKit  
**Kind**: class

An audio clock device object that handles the configurations for running I/O.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserAudioDevice;
```

#### Overview

The [`IOUserAudioDevice`](iouseraudiodevice.md) class subclasses [`IOUserAudioClockDevice`](iouseraudioclockdevice.md) and can contain [`IOUserAudioStream`](iouseraudiostream.md) instances that perform I/O for the audio device.

## Topics

### Creating an Audio Device
- [Create](iouseraudiodevice/create.md)
  Allocates and initializes an instance of the audio device class.
- [init](iouseraudiodevice/init.md)
  Initializes an instance of the audio device class.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
### Freeing an Audio Device
- [free](iouseraudiodevice/free.md)
  Frees the audio device.
### Getting Information About the Class
- [GetClassID](iouseraudiodevice/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudiodevice/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
### Performing I/O
- [StartIO](iouseraudiodevice/startio.md)
  Tells the device to start I/O.
- [StopIO](iouseraudiodevice/stopio.md)
  Tells the device to stop I/O.
- [IOUserAudioStartStopFlags](audiodriverkit/iouseraudiostartstopflags.md)
  Values that indicate I/O starts or stops.
### Supporting Device Configuration Changes
- [PerformDeviceConfigurationChange](iouseraudiodevice/performdeviceconfigurationchange.md)
  Tells the device to handle a configuration change.
- [AbortDeviceConfigurationChange](iouseraudiodevice/abortdeviceconfigurationchange.md)
  Tells the device to stop handling a configuration change.
### Supporting Sample Rate Changes
- [HandleChangeSampleRate](iouseraudiodevice/handlechangesamplerate.md)
  Tells the device the sample rate is changing.
- [DeviceSampleRateChanged](iouseraudiostream/devicesampleratechanged.md)
  Updates stream formats, in response to the owning audio device changing its sample rate.
### Working with Audio Streams
- [AddStream](iouseraudiodevice/addstream.md)
  Adds an audio stream to the device.
- [RemoveStream](iouseraudiodevice/removestream.md)
  Removes an audio stream from the device.
- [IOUserAudioStream](iouseraudiostream.md)
  An audio object that performs I/O for an audio device.
### Working with Default Device Behavior
- [SetCanBeDefaultInputDevice](iouseraudiodevice/setcanbedefaultinputdevice.md)
  Sets a Boolean value that indicates if this device can be the host’s default input device.
- [CanBeDefaultInputDevice](iouseraudiodevice/canbedefaultinputdevice.md)
  Returns a Boolean value that indicates if this device can be the host’s default input device.
- [SetCanBeDefaultOutputDevice](iouseraudiodevice/setcanbedefaultoutputdevice.md)
  Sets a Boolean value that indicates if this device can be the host’s default output device.
- [CanBeDefaultOutputDevice](iouseraudiodevice/canbedefaultoutputdevice.md)
  Returns a Boolean value that indicates if this device can be the host’s default output device.
- [SetCanBeDefaultSystemOutputDevice](iouseraudiodevice/setcanbedefaultsystemoutputdevice.md)
  Sets a Boolean value that indicates if this device can be the system’s default output device.
- [CanBeDefaultSystemOutputDevice](iouseraudiodevice/canbedefaultsystemoutputdevice.md)
  Returns a Boolean value that indicates if this device can be the system’s default output device.
### Working with Safety Offset Behvaior
- [SetInputSafetyOffset](iouseraudiodevice/setinputsafetyoffset.md)
  Specifies the input safety offset of the device.
- [GetInputSafetyOffset](iouseraudiodevice/getinputsafetyoffset.md)
  Returns the input safety offset of the device.
- [SetOutputSafetyOffset](iouseraudiodevice/setoutputsafetyoffset.md)
  Specifies the output safety offset of the device.
- [GetOutputSafetyOffset](iouseraudiodevice/getoutputsafetyoffset.md)
  Returns the output safety offset of the device.
### Working with Channel Layouts
- [SetPreferredChannelsForStereo](iouseraudiodevice/setpreferredchannelsforstereo.md)
  Sets the channel indices for the prefered stereo pair.
- [GetPreferredChannelsForStereo](iouseraudiodevice/getpreferredchannelsforstereo.md)
  Returns the channel indices for the prefered stereo pair.
- [SetPreferredInputChannelLayout](iouseraudiodevice/setpreferredinputchannellayout.md)
  Sets the input channel layout, using an array of audio channel label values.
- [SetPreferredOutputChannelLayout](iouseraudiodevice/setpreferredoutputchannellayout.md)
  Sets the output channel layout, using an array of audio channel label values.
- [IOUserAudioChannelLabel](audiodriverkit/iouseraudiochannellabel.md)
  Constants to set the preferred channel layout on an audio device.
### Instance Methods
- [GetCurrentClientIOTime](iouseraudiodevice/getcurrentclientiotime.md)
- [SetIOOperationHandler](iouseraudiodevice/setiooperationhandler.md)
- [SetWantsStreamFormatsRestored](iouseraudiodevice/setwantsstreamformatsrestored.md)

## Relationships

### Inherits From
- [IOUserAudioClockDevice](iouseraudioclockdevice.md)

## See Also

- [IOUserAudioClockDevice](iouseraudioclockdevice.md)
  An audio clock device object, used to synchronize and perform I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice)*