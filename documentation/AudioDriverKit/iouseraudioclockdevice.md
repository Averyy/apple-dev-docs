# IOUserAudioClockDevice

**Framework**: AudioDriverKit  
**Kind**: class

An audio clock device object, used to synchronize and perform I/O.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserAudioClockDevice;
```

## Topics

### Creating a Clock Device
- [Create](iouseraudioclockdevice/create.md)
  Allocates and initializes an instance of the audio clock device class.
- [init](iouseraudioclockdevice/init.md)
  Initializes an instance of the audio clock device class.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
### Freeing a Clock Device
- [free](iouseraudioclockdevice/free.md)
  Frees the clock device.
### Getting Information About the Class
- [GetClassID](iouseraudioclockdevice/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudioclockdevice/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
### Performing I/O
- [StartIO](iouseraudioclockdevice/startio.md)
  Tells the clock device to start I/O.
- [StopIO](iouseraudioclockdevice/stopio.md)
  Tells the clock device to stop I/O.
- [IOUserAudioStartStopFlags](audiodriverkit/iouseraudiostartstopflags.md)
  Values that indicate I/O starts or stops.
### Supporting Device Configuration Changes
- [PerformDeviceConfigurationChange](iouseraudioclockdevice/performdeviceconfigurationchange.md)
  Tells the clock device to handle a configuration change.
- [AbortDeviceConfigurationChange](iouseraudioclockdevice/abortdeviceconfigurationchange.md)
  Tells the clock device to stop handling a configuration change.
### Supporting Sample Rate Changes
- [HandleChangeSampleRate](iouseraudioclockdevice/handlechangesamplerate.md)
  Tells the clock device the sample rate is changing.
### Identifying the Clock Device
- [GetUID](iouseraudioclockdevice/getuid.md)
  Gets the unique identifier of the clock device.
### Working with Clock Domain
- [SetClockDomain](iouseraudioclockdevice/setclockdomain.md)
  Sets the clock domain value of the clock device.
- [GetClockDomain](iouseraudioclockdevice/getclockdomain.md)
  Gets the clock domain value of the clock device.
### Working with Sample Rates
- [SetSampleRate](iouseraudioclockdevice/setsamplerate.md)
  Sets the sample rate for the clock device.
- [GetSampleRate](iouseraudioclockdevice/getsamplerate.md)
  Gets the sample rate of the clock device.
- [SetAvailableSampleRates](iouseraudioclockdevice/setavailablesamplerates.md)
  Sets the available sample rates for the clock device.
- [GetAvailableSampleRates](iouseraudioclockdevice/getavailablesamplerates.md)
  Gets the available sample rates of the clock device.
- [GetNumberAvailableSampleRates](iouseraudioclockdevice/getnumberavailablesamplerates.md)
  Gets the number of available sample rates of the clock device.
### Working with Timing and Latency
- [GetSupportsPrewarming](iouseraudioclockdevice/getsupportsprewarming.md)
  Returns a Boolean value that indicates clock device’s support for prewarming.
- [SetZeroTimeStampPeriod](iouseraudioclockdevice/setzerotimestampperiod.md)
  Sets the zero time stamp of the clock device.
- [GetZeroTimestampPeriod](iouseraudioclockdevice/getzerotimestampperiod.md)
  Gets the zero time stamp of the clock device.
- [SetOutputLatency](iouseraudioclockdevice/setoutputlatency.md)
  Sets the output latency of the clock device.
- [GetOutputLatency](iouseraudioclockdevice/getoutputlatency.md)
  Gets the output latency of the clock device.
- [SetInputLatency](iouseraudioclockdevice/setinputlatency.md)
  Sets the input latency of the clock device.
- [GetInputLatency](iouseraudioclockdevice/getinputlatency.md)
  Get the input latency of the clock device.
### Working with Clock Device State
- [GetDeviceIsRunning](iouseraudioclockdevice/getdeviceisrunning.md)
  Gets a Boolean value that indicates whether the device is running.
- [SetDeviceIsAlive](iouseraudioclockdevice/setdeviceisalive.md)
  Sets a Boolean value to represent whether the device is alive.
- [GetDeviceIsAlive](iouseraudioclockdevice/getdeviceisalive.md)
  Gets a Boolean value that represents whether the device is alive.
- [SetIsHidden](iouseraudioclockdevice/setishidden.md)
  Sets a Boolean value to indicate whether the device is hidden.
- [GetIsHidden](iouseraudioclockdevice/getishidden.md)
  Gets a Boolean value that indicates whether the device is hidden.
### Working with Clock Device Behavior
- [SetClockAlgorithm](iouseraudioclockdevice/setclockalgorithm.md)
  Sets the clock algorithm of the clock device.
- [GetClockAlgorithm](iouseraudioclockdevice/getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [IOUserAudioClockAlgorithm](audiodriverkit/iouseraudioclockalgorithm.md)
  Values that describe clock-smoothing algorithms.
- [SetClockIsStable](iouseraudioclockdevice/setclockisstable.md)
  Sets a Boolean value to represent the clock’s stability.
- [GetClockIsStable](iouseraudioclockdevice/getclockisstable.md)
  Gets a Boolean value that represents the clock’s stability.
### Working with Transport Type
- [SetTransportType](iouseraudioclockdevice/settransporttype.md)
  Sets the transport type of the clock device.
- [GetTransportType](iouseraudioclockdevice/gettransporttype.md)
  Gets the transport type of the clock device.
- [IOUserAudioTransportType](audiodriverkit/iouseraudiotransporttype.md)
  The type of transport to deliver audio.
### Communicating with the Host
- [RequestDeviceConfigurationChange](iouseraudioclockdevice/requestdeviceconfigurationchange.md)
  Instructs the host to initiate a configuration change operation.
### Managing Audio Controls
- [AddControl](iouseraudioclockdevice/addcontrol.md)
  Adds a control to the clock device.
- [RemoveControl](iouseraudioclockdevice/removecontrol.md)
  Removes a control from the clock device.
- [IOUserAudioControl](iouseraudiocontrol.md)
  The base class for audio control objects.
### Accessing Timestamps
- [UpdateCurrentZeroTimestamp](iouseraudioclockdevice/updatecurrentzerotimestamp.md)
  Updates the current timestamp value.
- [GetCurrentZeroTimestamp](iouseraudioclockdevice/getcurrentzerotimestamp.md)
  Gets the current zero timestamp value.
### Accessing Client Status Information
- [GetCurrentClientSampleTime](iouseraudioclockdevice/getcurrentclientsampletime.md)
  Gets the current sample time in the ring buffer that the client has written to or read from.
### Instance Methods
- [GetDeviceTransportState](iouseraudioclockdevice/getdevicetransportstate.md)
- [SetWantsControlsRestored](iouseraudioclockdevice/setwantscontrolsrestored.md)

## Relationships

### Inherits From
- [IOUserAudioObject](iouseraudioobject.md)
### Inherited By
- [IOUserAudioDevice](iouseraudiodevice.md)

## See Also

- [IOUserAudioDevice](iouseraudiodevice.md)
  An audio clock device object that handles the configurations for running I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice)*