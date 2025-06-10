# AudioHardwareDevice

**Framework**: Core Audio  
**Kind**: class

**Availability**:
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
- [var bufferFrameSize: Int](audiohardwaredevice/bufferframesize.md)
- [var bufferFrameSizeRange: AudioValueRange](audiohardwaredevice/bufferframesizerange.md)
- [var canBeDefaultInputDevice: Bool](audiohardwaredevice/canbedefaultinputdevice.md)
- [var canBeDefaultOutputDevice: Bool](audiohardwaredevice/canbedefaultoutputdevice.md)
- [var canBeDefaultSoundEffectsDevice: Bool](audiohardwaredevice/canbedefaultsoundeffectsdevice.md)
- [var clock: AudioHardwareClock](audiohardwaredevice/clock.md)
- [var configurationApplication: String](audiohardwaredevice/configurationapplication.md)
- [var currentTime: AudioTimeStamp](audiohardwaredevice/currenttime.md)
- [var hogModePID: pid_t](audiohardwaredevice/hogmodepid.md)
- [var icon: URL?](audiohardwaredevice/icon.md)
- [var inputSafetyOffset: Int](audiohardwaredevice/inputsafetyoffset.md)
- [var inputStreamConfiguration: [AudioBuffer]](audiohardwaredevice/inputstreamconfiguration.md)
- [var ioCycleUsage: Float](audiohardwaredevice/iocycleusage.md)
- [var isHidden: Bool](audiohardwaredevice/ishidden.md)
- [var isProcessInputMuted: Bool](audiohardwaredevice/isprocessinputmuted.md)
- [var isProcessOutputMuted: Bool](audiohardwaredevice/isprocessoutputmuted.md)
- [var isRunningInAProcess: Bool](audiohardwaredevice/isrunninginaprocess.md)
- [var largestVariableBufferFrameSize: Int](audiohardwaredevice/largestvariablebufferframesize.md)
- [var modelUID: String](audiohardwaredevice/modeluid.md)
- [var outputSafetyOffset: Int](audiohardwaredevice/outputsafetyoffset.md)
- [var outputStreamConfiguration: [AudioBuffer]](audiohardwaredevice/outputstreamconfiguration.md)
- [var preferredInputChannelsForStereo: [UInt32]](audiohardwaredevice/preferredinputchannelsforstereo.md)
- [var preferredOutputChannelsForStereo: [UInt32]](audiohardwaredevice/preferredoutputchannelsforstereo.md)
- [var relatedDevices: [AudioHardwareDevice]](audiohardwaredevice/relateddevices.md)
- [var streams: [AudioHardwareStream]](audiohardwaredevice/streams.md)
- [var usesVariableBufferFrameSizes: Bool](audiohardwaredevice/usesvariablebufferframesizes.md)
- [var workgroup: WorkGroup](audiohardwaredevice/workgroup.md)
### Instance Methods
- [func nearestStartTime(atTime: AudioTimeStamp, withFlags: UInt32) throws -> AudioTimeStamp](audiohardwaredevice/neareststarttime(attime:withflags:).md)
- [func setBufferFrameSize(Int) throws](audiohardwaredevice/setbufferframesize(_:).md)
- [func setClock(AudioHardwareClock) throws](audiohardwaredevice/setclock(_:).md)
- [func setIOCycleUsage(Float) throws](audiohardwaredevice/setiocycleusage(_:).md)
- [func setIsProcessInputMuted(Bool) throws](audiohardwaredevice/setisprocessinputmuted(_:).md)
- [func setIsProcessOutputMuted(Bool) throws](audiohardwaredevice/setisprocessoutputmuted(_:).md)
- [func setPreferredInputChannelsForStereo([UInt32]) throws](audiohardwaredevice/setpreferredinputchannelsforstereo(_:).md)
- [func setPreferredOutputChannelsForStereo([UInt32]) throws](audiohardwaredevice/setpreferredoutputchannelsforstereo(_:).md)
- [func start(IOProcID: AudioDeviceIOProcID?) throws](audiohardwaredevice/start(ioprocid:).md)
- [func start(at: AudioTimeStamp, flags: UInt32, IOProcID: AudioDeviceIOProcID?) throws -> AudioTimeStamp?](audiohardwaredevice/start(at:flags:ioprocid:).md)
- [func stop(IOProcID: AudioDeviceIOProcID?) throws](audiohardwaredevice/stop(ioprocid:).md)
- [func toggleHogMode() throws -> pid_t](audiohardwaredevice/togglehogmode.md)
- [func translateTime(AudioTimeStamp) throws -> AudioTimeStamp](audiohardwaredevice/translatetime(_:).md)

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