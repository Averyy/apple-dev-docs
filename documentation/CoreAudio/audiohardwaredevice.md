# AudioHardwareDevice

**Framework**: Core Audio  
**Kind**: class

Instances of the AudioHardwareDevice class encapsulate individual audio devices. An audio device serves as the basic unit of IO. AudioHardwareDevice provides properties and methods to access and manipulate a device’s state and run IO.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
class AudioHardwareDevice
```

## Topics

### Initializers
- [init(id: AudioObjectID)](audiohardwaredevice/init(id:).md)
### Instance Properties
- [var actualSampleRate: Double](audiohardwaredevice/actualsamplerate.md)
  A Double that indicates the current actual sample rate of the device as measured by its timestamps.
- [var bufferFrameSize: Int](audiohardwaredevice/bufferframesize.md)
  An Int whose value indicates the number of frames in the IO buffers.
- [var bufferFrameSizeRange: AudioValueRange](audiohardwaredevice/bufferframesizerange.md)
  An AudioValueRange indicating the minimum and maximum values, inclusive, for bufferFrameSize.
- [var canBeDefaultInputDevice: Bool](audiohardwaredevice/canbedefaultinputdevice.md)
  A Bool where true indicates that the device is a possible selection for default input device.
- [var canBeDefaultOutputDevice: Bool](audiohardwaredevice/canbedefaultoutputdevice.md)
  A Bool where true indicates that the device is a possible selection for default output device.
- [var canBeDefaultSoundEffectsDevice: Bool](audiohardwaredevice/canbedefaultsoundeffectsdevice.md)
  A Bool where true indicates that the device is a possible selection for default sound effects device.
- [var clock: AudioHardwareClock](audiohardwaredevice/clock.md)
  The AudioHardwareClock that is currently serving as the main time base of the device.
- [var configurationApplication: String](audiohardwaredevice/configurationapplication.md)
  A String that contains the bundle ID for an application that provides a GUI for configuring the device. By default, the value of this property is the bundle ID for Audio MIDI Setup.
- [var currentTime: AudioTimeStamp](audiohardwaredevice/currenttime.md)
  An AudioTimeStamp containing the current time from the device.
- [var hogModePID: pid_t](audiohardwaredevice/hogmodepid.md)
  A pid_t indicating the process that currently owns exclusive access to the device or a value of -1 indicating that the device is currently available to all processes.
- [var icon: URL?](audiohardwaredevice/icon.md)
  A URL that directs to an image file that can be used to represent the device visually.
- [var inputSafetyOffset: Int](audiohardwaredevice/inputsafetyoffset.md)
  An Int whose value indicates the number of frames behind the current hardware position that is safe to do IO.
- [var inputStreamConfiguration: [AudioBuffer]](audiohardwaredevice/inputstreamconfiguration.md)
  This property returns the stream configuration of the device in an array of AudioBuffers (with the buffer data set to nil) which describes the list of streams and the number of channels in each stream. This corresponds to what will be passed into the IOProc.
- [var ioCycleUsage: Float](audiohardwaredevice/iocycleusage.md)
  A Float whose range is from 0 to 1. This value indicates how much of the client portion of the IO cycle the process will use.
- [var isHidden: Bool](audiohardwaredevice/ishidden.md)
  A Bool where true indicates that the device is not included in the normal list of devices provided by the system nor can it be the default device. Hidden devices can only be obtained from the system by UID.
- [var isProcessInputMuted: Bool](audiohardwaredevice/isprocessinputmuted.md)
  A Bool where true indicates that the current process’s input audio will be zeroed out by the system.
- [var isProcessOutputMuted: Bool](audiohardwaredevice/isprocessoutputmuted.md)
  A Bool where true indicates that the current process’s output audio will be zeroed out by the system.
- [var isRunningInAProcess: Bool](audiohardwaredevice/isrunninginaprocess.md)
  A Bool where true indicates that the device is running in at least one process on the system and false means that it isn’t running at all.
- [var largestVariableBufferFrameSize: Int](audiohardwaredevice/largestvariablebufferframesize.md)
  An Int that indicates the largest buffer that will be passed and bufferFrameSize if usesVariableBufferFrameSizes is true.
- [var modelUID: String](audiohardwaredevice/modeluid.md)
  A String that contains a persistent identifier for the model of a device. The identifier is unique such that the identifier from two devices are equal if and only if the two devices are the exact same model from the same manufacturer. Further, the identifier has to be the same no matter on what machine the device appears.
- [var outputSafetyOffset: Int](audiohardwaredevice/outputsafetyoffset.md)
  An Int whose value indicates the number for frames ahead of the current hardware position that is safe to do IO.
- [var outputStreamConfiguration: [AudioBuffer]](audiohardwaredevice/outputstreamconfiguration.md)
  This property returns the stream configuration of the device in an array of AudioBuffers (with the buffer data set to nil) which describes the list of streams and the number of channels in each stream. This corresponds to what will be passed into the IOProc.
- [var preferredInputChannelsForStereo: [UInt32]](audiohardwaredevice/preferredinputchannelsforstereo.md)
  An array of two UInt32s, the first for the left channel, the second for the right channel, that indicate the channel numbers to use for stereo input IO on the device.
- [var preferredOutputChannelsForStereo: [UInt32]](audiohardwaredevice/preferredoutputchannelsforstereo.md)
  An array of two UInt32s, the first for the left channel, the second for the right channel, that indicate the channel numbers to use for stereo output IO on the device.
- [var relatedDevices: [AudioHardwareDevice]](audiohardwaredevice/relateddevices.md)
  An array of AudioHardwareDevices for devices related to the device. For IOAudio-based devices, devices are related if they share the same IOAudioDevice object.
- [var streams: [AudioHardwareStream]](audiohardwaredevice/streams.md)
  An array of AudioHardwareStreams that represent the IO streams of the device.
- [var usesVariableBufferFrameSizes: Bool](audiohardwaredevice/usesvariablebufferframesizes.md)
  A Bool where true indicates that the sizes of the buffers passed to an IOProc will vary by a small amount.
- [var workgroup: WorkGroup](audiohardwaredevice/workgroup.md)
  A WorkGroup that represents the thread workgroup the device’s IO thread belongs to.
### Instance Methods
- [func nearestStartTime(atTime: AudioTimeStamp, withFlags: UInt32) throws -> AudioTimeStamp](audiohardwaredevice/neareststarttime(attime:withflags:).md)
  Query the device to get a time equal to or later than the given time that is the best time to start IO.
- [func setBufferFrameSize(Int) throws](audiohardwaredevice/setbufferframesize(_:).md)
  Set the bufferFrameSize property.
- [func setClock(AudioHardwareClock) throws](audiohardwaredevice/setclock(_:).md)
  Set the clock property.
- [func setIOCycleUsage(Float) throws](audiohardwaredevice/setiocycleusage(_:).md)
  Set the ioCycleUsage property.
- [func setIsProcessInputMuted(Bool) throws](audiohardwaredevice/setisprocessinputmuted(_:).md)
  Set the isProcessInputMuted property.
- [func setIsProcessOutputMuted(Bool) throws](audiohardwaredevice/setisprocessoutputmuted(_:).md)
  Set the isProcessOutputMuted property.
- [func setPreferredInputChannelsForStereo([UInt32]) throws](audiohardwaredevice/setpreferredinputchannelsforstereo(_:).md)
  Set the preferredInputChannelsForStereo property.
- [func setPreferredOutputChannelsForStereo([UInt32]) throws](audiohardwaredevice/setpreferredoutputchannelsforstereo(_:).md)
  Set the preferredOutputChannelsForStereo property.
- [func start(IOProcID: AudioDeviceIOProcID?) throws](audiohardwaredevice/start(ioprocid:).md)
  Starts IO for the given AudioDeviceIOProcID.
- [func start(at: AudioTimeStamp, flags: UInt32, IOProcID: AudioDeviceIOProcID?) throws -> AudioTimeStamp?](audiohardwaredevice/start(at:flags:ioprocid:).md)
  Starts IO for the given AudioDeviceIOProcID and aligns the IO cycle of the device with the given time.
- [func stop(IOProcID: AudioDeviceIOProcID?) throws](audiohardwaredevice/stop(ioprocid:).md)
  Stops IO for the given AudioDeviceIOProcID.
- [func toggleHogMode() throws -> pid_t](audiohardwaredevice/togglehogmode.md)
  Toggle exclusive access to the device for the current process. If another process owns exclusive access, that remains unchanged. If the current process owns exclusive access, it is released and made available to all processes again. If no process has exclusive access, this process gains ownership of exclusive access.
- [func translateTime(AudioTimeStamp) throws -> AudioTimeStamp](audiohardwaredevice/translatetime(_:).md)
  Translates the time in the device’s time base from one representation to another. Note that the device has to be running

## Relationships

### Inherits From
- [AudioHardwareClock](audiohardwareclock.md)
### Inherited By
- [AudioHardwareAggregateDevice](audiohardwareaggregatedevice.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice)*