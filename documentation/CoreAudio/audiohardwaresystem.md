# AudioHardwareSystem

**Framework**: Core Audio  
**Kind**: class

**Availability**:
- macOS 15.0+

## Declaration

```swift
class AudioHardwareSystem
```

## Topics

### Initializers
- [init(id: AudioObjectID)](audiohardwaresystem/init(id:).md)
### Instance Properties
- [var allowsHogMode: Bool](audiohardwaresystem/allowshogmode.md)
- [var allowsSleeping: Bool](audiohardwaresystem/allowssleeping.md)
- [var allowsUnloading: Bool](audiohardwaresystem/allowsunloading.md)
- [var boxes: [AudioHardwareBox]](audiohardwaresystem/boxes.md)
- [var clocks: [AudioHardwareClock]](audiohardwaresystem/clocks.md)
- [var defaultInputDevice: AudioHardwareDevice?](audiohardwaresystem/defaultinputdevice.md)
- [var defaultOutputDevice: AudioHardwareDevice?](audiohardwaresystem/defaultoutputdevice.md)
- [var defaultSoundEffectsDevice: AudioHardwareDevice?](audiohardwaresystem/defaultsoundeffectsdevice.md)
- [var devices: [AudioHardwareDevice]](audiohardwaresystem/devices.md)
- [var isInitializingOrExiting: Bool](audiohardwaresystem/isinitializingorexiting.md)
- [var isProcessInputMuted: Bool](audiohardwaresystem/isprocessinputmuted.md)
- [var plugins: [AudioHardwarePlugin]](audiohardwaresystem/plugins.md)
- [var powerHint: AudioHardwarePowerHint](audiohardwaresystem/powerhint.md)
- [var processes: [AudioHardwareProcess]](audiohardwaresystem/processes.md)
- [var shouldMixStereoToMono: Bool](audiohardwaresystem/shouldmixstereotomono.md)
- [var taps: [AudioHardwareTap]](audiohardwaresystem/taps.md)
### Instance Methods
- [func box(forUID: String) throws -> AudioHardwareBox?](audiohardwaresystem/box(foruid:).md)
- [func clock(forUID: String) throws -> AudioHardwareClock?](audiohardwaresystem/clock(foruid:).md)
- [func destroyAggregateDevice(AudioHardwareAggregateDevice) throws](audiohardwaresystem/destroyaggregatedevice(_:).md)
- [func destroyProcessTap(AudioHardwareTap) throws](audiohardwaresystem/destroyprocesstap(_:).md)
- [func device(forUID: String) throws -> AudioHardwareDevice?](audiohardwaresystem/device(foruid:).md)
- [func makeAggregateDevice(description: [String : Any]) throws -> AudioHardwareAggregateDevice?](audiohardwaresystem/makeaggregatedevice(description:).md)
- [func makeProcessTap(description: CATapDescription) throws -> AudioHardwareTap?](audiohardwaresystem/makeprocesstap(description:).md)
- [func plugin(forBundleID: String) throws -> AudioHardwarePlugin?](audiohardwaresystem/plugin(forbundleid:).md)
- [func process(for: pid_t) throws -> AudioHardwareProcess?](audiohardwaresystem/process(for:).md)
- [func setAllowsHogMode(Bool) throws](audiohardwaresystem/setallowshogmode(_:).md)
- [func setAllowsSleeping(Bool) throws](audiohardwaresystem/setallowssleeping(_:).md)
- [func setAllowsUnloading(Bool) throws](audiohardwaresystem/setallowsunloading(_:).md)
- [func setDefaultInputDevice(AudioHardwareDevice) throws](audiohardwaresystem/setdefaultinputdevice(_:).md)
- [func setDefaultOutputDevice(AudioHardwareDevice) throws](audiohardwaresystem/setdefaultoutputdevice(_:).md)
- [func setDefaultSoundEffectsDevice(AudioHardwareDevice) throws](audiohardwaresystem/setdefaultsoundeffectsdevice(_:).md)
- [func setIsProcessInputMuted(Bool) throws](audiohardwaresystem/setisprocessinputmuted(_:).md)
- [func setPowerHint(AudioHardwarePowerHint) throws](audiohardwaresystem/setpowerhint(_:).md)
- [func setShouldMixStereoToMono(Bool) throws](audiohardwaresystem/setshouldmixstereotomono(_:).md)
- [func tap(forUID: String) throws -> AudioHardwareTap?](audiohardwaresystem/tap(foruid:).md)
- [func unload() throws](audiohardwaresystem/unload.md)
### Type Properties
- [static let shared: AudioHardwareSystem](audiohardwaresystem/shared.md)

## Relationships

### Inherits From
- [AudioHardwareObject](audiohardwareobject.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem)*