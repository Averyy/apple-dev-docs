# AudioHardwareSystem

**Framework**: Core Audio  
**Kind**: class  
**Role**: Class

The audio objects in the HAL are arranged in a containment hierarchy. The root of the hierarchy is the one and only instance of the system class. The properties of the AudioHardwareSystem describe the process global settings such as the various default devices. The system object also contains all the devices that are available.

**Availability**:
- Mac Catalyst
- macOS 15.0+

## Declaration

```swift
class AudioHardwareSystem
```

## Topics

### Initializers
- [init(id: AudioObjectID)](./audiohardwaresystem/init%28id%29.md)
### Instance Properties
- [var allowsHogMode: Bool](./audiohardwaresystem/allowshogmode.md)
  A Bool where true indicates that this process wants the HAL to automatically take hog mode and false indicates that the HAL should not automatically take hog mode on behalf of the process.
- [var allowsSleeping: Bool](./audiohardwaresystem/allowssleeping.md)
  A Bool where true indicates that the process will allow the CPU to idle sleep even if there is audio IO in progress. Fasle indicates that the CPU will not be allowed to idle sleep.
- [var allowsUnloading: Bool](./audiohardwaresystem/allowsunloading.md)
  A Bool where true indicates that this process wants the HAL to unload itself after a period of inactivity where there are no IOProcs and no listeners registered with any object.
- [var boxes: [AudioHardwareBox]](./audiohardwaresystem/boxes.md)
  An array of AudioHardwareBoxes that represent all the box objects on the system.
- [var clocks: [AudioHardwareClock]](./audiohardwaresystem/clocks.md)
  An array of AudioHardwareClocks that represent all the clock objects on the system.
- [var defaultInputDevice: AudioHardwareDevice?](./audiohardwaresystem/defaultinputdevice.md)
  The default input audio device on the system, or nil if there is no default input device.
- [var defaultOutputDevice: AudioHardwareDevice?](./audiohardwaresystem/defaultoutputdevice.md)
  The default output audio device on the system, or nil if there is no default output device.
- [var defaultSoundEffectsDevice: AudioHardwareDevice?](./audiohardwaresystem/defaultsoundeffectsdevice.md)
  The default sounds effects audio device on the system, or nil if there is no default sound effects device.
- [var devices: [AudioHardwareDevice]](./audiohardwaresystem/devices.md)
  An array of the AudioHardwareDevices that represent all the devices currently available to the system.
- [var isInitializingOrExiting: Bool](./audiohardwaresystem/isinitializingorexiting.md)
  A Bool where true indicates the HAL is either in the midst of initializing or in the midst of exiting the process.
- [var isProcessInputMuted: Bool](./audiohardwaresystem/isprocessinputmuted.md)
  A Bool where true indicates that all data coming into the process for all devices will be silent. A value of false indicates that input data will be received normally.
- [var plugins: [AudioHardwarePlugin]](./audiohardwaresystem/plugins.md)
  An array of AudioHardwarePlugins that represent all the plugin objects on the system.
- [var powerHint: AudioHardwarePowerHint](./audiohardwaresystem/powerhint.md)
  An AudioHardwarePowerHint enum which allows a process to indicate how aggressive the system can be with optimizations that save power. The default value is none.
- [var processes: [AudioHardwareProcess]](./audiohardwaresystem/processes.md)
  An array of AudioHardwareProcesses that represent the Process objects for all client processes currently connected to the system.
- [var shouldMixStereoToMono: Bool](./audiohardwaresystem/shouldmixstereotomono.md)
  A Bool where a value of true indicates that devices should mix stereo signals down to mono.
- [var taps: [AudioHardwareTap]](./audiohardwaresystem/taps.md)
  An array of AudioHardwareTaps that represent all the tap objects on the system.
### Instance Methods
- [func box(forUID: String) throws -> AudioHardwareBox?](./audiohardwaresystem/box%28foruid%29.md)
- [func clock(forUID: String) throws -> AudioHardwareClock?](./audiohardwaresystem/clock%28foruid%29.md)
- [func destroyAggregateDevice(AudioHardwareAggregateDevice) throws](./audiohardwaresystem/destroyaggregatedevice%28_%29.md)
  Destroys the aggregate device represented by the given AudioHardwareAggregateDevice.
- [func destroyProcessTap(AudioHardwareTap) throws](./audiohardwaresystem/destroyprocesstap%28_%29.md)
  Destroys the given tap.
- [func device(forUID: String) throws -> AudioHardwareDevice?](./audiohardwaresystem/device%28foruid%29.md)
- [func makeAggregateDevice(description: [String : Any]) throws -> AudioHardwareAggregateDevice?](./audiohardwaresystem/makeaggregatedevice%28description%29.md)
  Creates a new aggregate device  using the provided description.
- [func makeProcessTap(description: CATapDescription) throws -> AudioHardwareTap?](./audiohardwaresystem/makeprocesstap%28description%29.md)
  Creates a new tap using the provided description.
- [func plugin(forBundleID: String) throws -> AudioHardwarePlugin?](./audiohardwaresystem/plugin%28forbundleid%29.md)
- [func process(for: pid_t) throws -> AudioHardwareProcess?](./audiohardwaresystem/process%28for%29.md)
- [func setAllowsHogMode(Bool) throws](./audiohardwaresystem/setallowshogmode%28_%29.md)
  Set the allowsHogMode property.
- [func setAllowsSleeping(Bool) throws](./audiohardwaresystem/setallowssleeping%28_%29.md)
  Set the allowsSleeping property.
- [func setAllowsUnloading(Bool) throws](./audiohardwaresystem/setallowsunloading%28_%29.md)
  Set the allowsUnloading property.
- [func setDefaultInputDevice(AudioHardwareDevice) throws](./audiohardwaresystem/setdefaultinputdevice%28_%29.md)
  Set the defaultInputDevice property.
- [func setDefaultOutputDevice(AudioHardwareDevice) throws](./audiohardwaresystem/setdefaultoutputdevice%28_%29.md)
  Set the defaultOutputDevice property.
- [func setDefaultSoundEffectsDevice(AudioHardwareDevice) throws](./audiohardwaresystem/setdefaultsoundeffectsdevice%28_%29.md)
  Set the defaultSoundEffectsDevice property.
- [func setIsProcessInputMuted(Bool) throws](./audiohardwaresystem/setisprocessinputmuted%28_%29.md)
  Set the isProcessInputMuted property.
- [func setPowerHint(AudioHardwarePowerHint) throws](./audiohardwaresystem/setpowerhint%28_%29.md)
  Set the powerHint property.
- [func setShouldMixStereoToMono(Bool) throws](./audiohardwaresystem/setshouldmixstereotomono%28_%29.md)
  Set the shouldMixStereoToMono property.
- [func tap(forUID: String) throws -> AudioHardwareTap?](./audiohardwaresystem/tap%28foruid%29.md)
- [func unload() throws](./audiohardwaresystem/unload%28%29.md)
  Terminates all IO on all devices within the process and releases all resources capable of being released. This essentially returns the HAL to its uninitialized state.
### Type Properties
- [static let shared: AudioHardwareSystem](./audiohardwaresystem/shared.md)
  The shared instance of the AudioHardwareSystem class.

## Relationships

### Inherits From
- [AudioHardwareObject](./audiohardwareobject.md)
### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem)*