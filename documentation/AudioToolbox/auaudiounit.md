# AUAudioUnit

**Framework**: Audio Toolbox  
**Kind**: class

A class that defines a host’s interface to an audio unit.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AUAudioUnit
```

## Mentions

- [Adding Parallel Real-Time Threads to Audio Workgroups](adding-parallel-real-time-threads-to-audio-workgroups.md)

#### Overview

Hosts can instantiate either version 3 or version 2 audio units with this class, and to some extent control whether an audio unit is instantiated in-process or in a separate extension process.

Version 3 audio units should subclass the [`AUAudioUnit`](auaudiounit.md) class. Version 3 audio unit components can be registered in the following ways:

- Package the component into an app extension containing an `AudioComponents`  `Info.plist` entry. The principal class must conform to the [`AUAudioUnitFactory`](auaudiounitfactory.md) protocol, which will typically instantiate an [`AUAudioUnit`](auaudiounit.md) subclass.
- Call the [`registerSubclass(_:as:name:version:)`](auaudiounit/registersubclass(_:as:name:version:).md) method to associate a component description with an [`AUAudioUnit`](auaudiounit.md) subclass. Use the convention `<manufacturer name>:<audio unit name>` when naming your audio unit component.

Version 2 audio units should subclass the [`AUAudioUnitV2Bridge`](auaudiounitv2bridge.md) class instead. Version 2 audio unit components can be registered in the following ways:

- Package the component into a component bundle containing an `AudioComponents` `Info.plist` entry, referring to an `AudioComponentFactoryFunction` function.
- Call the `AudioComponentRegister` function to associate a component description with an `AudioComponentFactoryFunction` function.

A host does not need to be aware of the concrete [`AUAudioUnit`](auaudiounit.md) subclass that is being instantiated. The [`init(componentDescription:options:)`](auaudiounit/init(componentdescription:options:).md) method ensures that the proper subclass is used.

> ❗ **Important**:  When using the [`AUAudioUnit`](auaudiounit.md) class with a version 2 audio unit, or the C [`AudioComponent`](audiocomponent.md) and `AudioUnit` APIs with a version 3 audio unit, all major pieces of functionality are bridged between the two APIs. When applicable, this document references the version 2 API equivalent of each version 3 method or property.

## Topics

### Creating an Audio Unit
- [convenience init(componentDescription: AudioComponentDescription) throws](auaudiounit/init(componentdescription:).md)
  Synchronously initializes a new audio unit object.
- [init(componentDescription: AudioComponentDescription, options: AudioComponentInstantiationOptions) throws](auaudiounit/init(componentdescription:options:).md)
  Synchronously initializes a new audio unit object.
- [class func instantiate(with: AudioComponentDescription, options: AudioComponentInstantiationOptions, completionHandler: (AUAudioUnit?, (any Error)?) -> Void)](auaudiounit/instantiate(with:options:completionhandler:).md)
  Asynchronously creates an audio unit instance.
### Returning the Audio Busses
- [var inputBusses: AUAudioUnitBusArray](auaudiounit/inputbusses.md)
  An array containing the audio unit’s input connection points.
- [var outputBusses: AUAudioUnitBusArray](auaudiounit/outputbusses.md)
  An array containing the audio unit’s output connection points.
### Customizing the Audio Unit Behavior
- [class func registerSubclass(AnyClass, as: AudioComponentDescription, name: String, version: UInt32)](auaudiounit/registersubclass(_:as:name:version:).md)
  Registers an audio unit subclass.
- [func shouldChange(to: AVAudioFormat, for: AUAudioUnitBus) -> Bool](auaudiounit/shouldchange(to:for:).md)
  This is called when you set the format on a bus.
- [func setRenderResourcesAllocated(Bool)](auaudiounit/setrenderresourcesallocated(_:).md)
  Sets the Boolean value of the [`renderResourcesAllocated`](auaudiounit/renderresourcesallocated.md) property.
- [var internalRenderBlock: AUInternalRenderBlock](auaudiounit/internalrenderblock.md)
  The block which you must provide, via a getter, in order to implement rendering.
- [var midiOutputBufferSizeHint: Int](auaudiounit/midioutputbuffersizehint.md)
- [typealias AUInternalRenderBlock](auinternalrenderblock.md)
  A block to render the audio unit.
### Querying Parameters
- [var parameterTree: AUParameterTree?](auaudiounit/parametertree.md)
  An audio unit’s parameters, organized in a tree hierarchy.
- [var allParameterValues: Bool](auaudiounit/allparametervalues.md)
  Special read-only property for KVO.
- [func parametersForOverview(withCount: Int) -> [NSNumber]](auaudiounit/parametersforoverview(withcount:).md)
  Returns the audio unit’s most important parameters.
### Providing Data to the Host
- [var musicalContextBlock: AUHostMusicalContextBlock?](auaudiounit/musicalcontextblock.md)
  A callback to the host for musical context information.
- [var transportStateBlock: AUHostTransportStateBlock?](auaudiounit/transportstateblock.md)
  A callback to the host for transport state information.
- [var contextName: String?](auaudiounit/contextname.md)
  Information about the host context in which the audio unit is connected, for display in the audio unit’s view.
- [var supportsMPE: Bool](auaudiounit/supportsmpe.md)
  A Boolean value that indicates whether the audio unit supports multi-dimensional polyphonic expression.
- [typealias AUHostMusicalContextBlock](auhostmusicalcontextblock.md)
  A block through which hosts provide musical tempo, time signature, and beat position.
- [typealias AUHostTransportStateBlock](auhosttransportstateblock.md)
  A block through which hosts provide information about their transport state.
### Managing MIDI Events
- [var isMusicDeviceOrEffect: Bool](auaudiounit/ismusicdeviceoreffect.md)
  Specifies whether an audio unit responds to MIDI events.
- [var virtualMIDICableCount: Int](auaudiounit/virtualmidicablecount.md)
  The number of virtual MIDI cables implemented by a music device or effect.
- [var scheduleMIDIEventBlock: AUScheduleMIDIEventBlock?](auaudiounit/schedulemidieventblock.md)
  A block used to schedule MIDI events.
- [var midiOutputEventBlock: AUMIDIOutputEventBlock?](auaudiounit/midioutputeventblock.md)
- [var midiOutputNames: [String]](auaudiounit/midioutputnames.md)
  The names of the MIDI outputs.
- [typealias AUScheduleMIDIEventBlock](auschedulemidieventblock.md)
  A block to schedule MIDI events.
- [typealias AUMIDIOutputEventBlock](aumidioutputeventblock.md)
### Managing Presets
- [var fullState: [String : Any]?](auaudiounit/fullstate.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving as a user preset.
- [var fullStateForDocument: [String : Any]?](auaudiounit/fullstatefordocument.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving in a user’s document.
- [var factoryPresets: [AUAudioUnitPreset]?](auaudiounit/factorypresets.md)
  A collection of presets provided by the audio unit’s developer.
- [var currentPreset: AUAudioUnitPreset?](auaudiounit/currentpreset.md)
  The audio unit’s last-selected preset.
- [var supportsUserPresets: Bool](auaudiounit/supportsuserpresets.md)
- [var userPresets: [AUAudioUnitPreset]](auaudiounit/userpresets.md)
- [func saveUserPreset(AUAudioUnitPreset) throws](auaudiounit/saveuserpreset(_:).md)
- [func deleteUserPreset(AUAudioUnitPreset) throws](auaudiounit/deleteuserpreset(_:).md)
- [func presetState(for: AUAudioUnitPreset) throws -> [String : Any]](auaudiounit/presetstate(for:).md)
### Managing the Render Cycle
- [func allocateRenderResources() throws](auaudiounit/allocaterenderresources.md)
  Allocates resources required to render audio.
- [func deallocateRenderResources()](auaudiounit/deallocaterenderresources.md)
  Deallocates resources required to render audio.
- [func reset()](auaudiounit/reset.md)
  Resets transitory rendering state to its initial state.
- [var renderResourcesAllocated: Bool](auaudiounit/renderresourcesallocated.md)
  Determines whether the audio unit has allocated render resources.
- [var renderBlock: AURenderBlock](auaudiounit/renderblock.md)
  The block that hosts use to ask the audio unit to render audio.
- [var scheduleParameterBlock: AUScheduleParameterBlock](auaudiounit/scheduleparameterblock.md)
  The block that hosts use to schedule parameters.
- [var maximumFramesToRender: AUAudioFrameCount](auaudiounit/maximumframestorender.md)
  The maximum number of frames that the audio unit can render at once.
- [func token(byAddingRenderObserver: AURenderObserver) -> Int](auaudiounit/token(byaddingrenderobserver:).md)
  Adds a block to be called on each render cycle.
- [func removeRenderObserver(Int)](auaudiounit/removerenderobserver(_:).md)
  Removes an observer block previously added to the render cycle.
- [typealias AURenderObserver](aurenderobserver.md)
  A block called when an audio unit renders audio.
### Messaging Channels
- [func messageChannel(for: String) -> any AUMessageChannel](auaudiounit/messagechannel(for:).md)
  Returns an object for bidirectional communication between an audio unit and its host.
- [protocol AUMessageChannel](aumessagechannel.md)
  A specification for a bidirectional communication message channel.
### Optimizing Performance
- [var latency: TimeInterval](auaudiounit/latency.md)
  The audio unit’s processing latency, in seconds.
- [var tailTime: TimeInterval](auaudiounit/tailtime.md)
  The audio unit’s tail time, in seconds.
- [var renderQuality: Int](auaudiounit/renderquality.md)
  Provides a trade-off between rendering quality and CPU load.
- [var shouldBypassEffect: Bool](auaudiounit/shouldbypasseffect.md)
  Determines whether an effect should route input directly to output, without any processing.
- [var canProcessInPlace: Bool](auaudiounit/canprocessinplace.md)
  Determines whether an audio unit can process in place.
- [var isRenderingOffline: Bool](auaudiounit/isrenderingoffline.md)
  Communicates to an audio unit that it is rendering offline.
### Describing the Audio Unit
- [var componentDescription: AudioComponentDescription](auaudiounit/componentdescription.md)
  The component description with which the audio unit was created.
- [var component: AudioComponent](auaudiounit/component.md)
  The component found in the component description with which the audio unit was created.
- [var componentName: String?](auaudiounit/componentname.md)
  The audio unit’s component’s name.
- [var componentVersion: UInt32](auaudiounit/componentversion.md)
  The audio unit’s component’s version.
- [var audioUnitName: String?](auaudiounit/audiounitname.md)
  The audio unit’s name, derived from the component’s name.
- [var audioUnitShortName: String?](auaudiounit/audiounitshortname.md)
- [var manufacturerName: String?](auaudiounit/manufacturername.md)
  The manufacturer’s name, derived from the component’s name.
### Configuring the Channel Capabilities
- [var channelCapabilities: [NSNumber]?](auaudiounit/channelcapabilities.md)
  Expresses valid combinations of input and output channels.
- [var channelMap: [NSNumber]?](auaudiounit/channelmap.md)
- [func profileState(forCable: UInt8, channel: MIDIChannelNumber) -> MIDICIProfileState](auaudiounit/profilestate(forcable:channel:).md)
- [func enable(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](auaudiounit/enable(_:cable:onchannel:).md)
- [func disableProfile(MIDICIProfile, cable: UInt8, onChannel: MIDIChannelNumber) throws](auaudiounit/disableprofile(_:cable:onchannel:).md)
- [var profileChangedBlock: AUMIDICIProfileChangedBlock?](auaudiounit/profilechangedblock.md)
### Configuring the Device
- [var deviceID: AUAudioObjectID](auaudiounit/deviceid.md)
  Gets the I/O hardware device.
- [func setDeviceID(AUAudioObjectID) throws](auaudiounit/setdeviceid(_:).md)
  Sets the I/O hardware device.
- [var canPerformInput: Bool](auaudiounit/canperforminput.md)
  Determines whether the I/O device can perform input.
- [var canPerformOutput: Bool](auaudiounit/canperformoutput.md)
  Determines whether the I/O device can perform output.
- [var isInputEnabled: Bool](auaudiounit/isinputenabled.md)
  A flag enabling audio input from the unit.
- [var isOutputEnabled: Bool](auaudiounit/isoutputenabled.md)
  A flag enabling audio output from the unit.
- [var inputHandler: AUInputHandler?](auaudiounit/inputhandler.md)
  The block that the output unit will call to notify when input is available.
- [var outputProvider: AURenderPullInputBlock?](auaudiounit/outputprovider.md)
  The block that the output unit will call to get audio to send to the output.
- [var deviceInputLatency: TimeInterval](auaudiounit/deviceinputlatency.md)
  The audio device’s input latency, in seconds.
- [var deviceOutputLatency: TimeInterval](auaudiounit/deviceoutputlatency.md)
  The audio devic’s output latency, in seconds.
- [func startHardware() throws](auaudiounit/starthardware.md)
  Starts the audio hardware.
- [func stopHardware()](auaudiounit/stophardware.md)
  Stops the audio hardware.
- [typealias AURenderPullInputBlock](aurenderpullinputblock.md)
  A block to supply audio input to a render block.
### Configuring the User Interface
- [var providesUserInterface: Bool](auaudiounit/providesuserinterface.md)
  A Boolean that indicates whether the audio unit provides a user interface, normally in the form of a view controller.
- [func supportedViewConfigurations([AUAudioUnitViewConfiguration]) -> IndexSet](auaudiounit/supportedviewconfigurations(_:).md)
- [func select(AUAudioUnitViewConfiguration)](auaudiounit/select(_:).md)
### Getting the Runtime Behavior
- [var isRunning: Bool](auaudiounit/isrunning.md)
- [var isLoadedInProcess: Bool](auaudiounit/isloadedinprocess.md)
### Constants
- [AUEventSampleTime](1387633-aueventsampletime.md)
  Expresses time as a sample count.
- [enum AUAudioUnitBusType](auaudiounitbustype.md)
- [struct AUHostTransportStateFlags](auhosttransportstateflags.md)
- [enum AURenderEventType](aurendereventtype.md)
- [typealias AURenderBlock](aurenderblock.md)
  A block to render the audio unit.
- [typealias AUInputHandler](auinputhandler.md)
  A block to notify the host of an I/O unit that an input is available.
### Getting the Audio Unit Presets
- [var kAUPresetNumberKey: String](kaupresetnumberkey.md)
- [var kAUPresetCPULoadKey: String](kaupresetcpuloadkey.md)
- [var kAUPresetDataKey: String](kaupresetdatakey.md)
- [var kAUPresetElementNameKey: String](kaupresetelementnamekey.md)
- [var kAUPresetExternalFileRefs: String](kaupresetexternalfilerefs.md)
- [var kAUPresetMASDataKey: String](kaupresetmasdatakey.md)
- [var kAUPresetManufacturerKey: String](kaupresetmanufacturerkey.md)
- [var kAUPresetNameKey: String](kaupresetnamekey.md)
- [var kAUPresetPartKey: String](kaupresetpartkey.md)
  If present, distinguishes a global preset that is set on the global scope from a part-based preset that is set on the part scope. The value of this key is defined by the audio unit it applies to.
- [var kAUPresetRenderQualityKey: String](kaupresetrenderqualitykey.md)
- [var kAUPresetSubtypeKey: String](kaupresetsubtypekey.md)
- [var kAUPresetTypeKey: String](kaupresettypekey.md)
- [var kAUPresetVSTDataKey: String](kaupresetvstdatakey.md)
  VST state from a VST “bank.”
- [var kAUPresetVSTPresetKey: String](kaupresetvstpresetkey.md)
  VST state from a VST “preset.”
- [var kAUPresetVersionKey: String](kaupresetversionkey.md)
### Instance properties
- [var audioUnitMIDIProtocol: MIDIProtocolID](auaudiounit/audiounitmidiprotocol.md)
- [var hostMIDIProtocol: MIDIProtocolID](auaudiounit/hostmidiprotocol.md)
- [var midiOutputEventListBlock: AUMIDIEventListBlock?](auaudiounit/midioutputeventlistblock.md)
- [var migrateFromPlugin: [Any]](auaudiounit/migratefromplugin.md)
- [var scheduleMIDIEventListBlock: AUMIDIEventListBlock?](auaudiounit/schedulemidieventlistblock.md)
### Instance Methods
- [func requestViewController(completionHandler: (UIViewController?) -> Void)](auaudiounit/requestviewcontroller(completionhandler:).md)
  Requests an audio unit’s custom view controller.
### Instance Properties
- [var intendedSpatialExperience: any SpatialAudioExperience](auaudiounit/intendedspatialexperience-7uqrm.md)
  The AUAudioUnit’s intended spatial audio experience.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AUAudioUnitV2Bridge](auaudiounitv2bridge.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating an audio unit extension](../AVFAudio/creating-an-audio-unit-extension.md)
  Build an extension by using an Xcode template.
- [Creating custom audio effects](../AVFAudio/creating-custom-audio-effects.md)
  Add custom audio-effect processing to apps like Logic Pro X and GarageBand by creating Audio Unit (AU) plug-ins.
- [Incorporating Audio Effects and Instruments](incorporating-audio-effects-and-instruments.md)
  Add custom audio processing and MIDI instruments to your app by hosting Audio Unit (AU) plug-ins.
- [Debugging Out-of-Process Audio Units on Apple Silicon](debugging-out-of-process-audio-units-on-apple-silicon.md)
  Connect to out-of-process audio units using the Xcode debugger.
- [class AUAudioUnitBus](auaudiounitbus.md)
  A class that defines an input or output connection point on an audio unit.
- [class AUAudioUnitBusArray](auaudiounitbusarray.md)
  A class that defines a container for an audio unit’s input or output busses.
- [class AUAudioUnitPreset](auaudiounitpreset.md)
  A class that describes an interface for custom parameter settings provided by the audio unit developer.
- [class AUAudioUnitV2Bridge](auaudiounitv2bridge.md)
  A class that wraps a version 2 audio unit as version 3 audio unit.
- [func AudioUnitExtensionCopyComponentList(CFString) -> Unmanaged<CFArray>?](audiounitextensioncopycomponentlist(_:).md)
  Returns the component registrations for a given audio unit extension.
- [func AudioUnitExtensionSetComponentList(CFString, CFArray?) -> OSStatus](audiounitextensionsetcomponentlist(_:_:).md)
  Allows the implementor of an audio unit extension to dynamically modify the list of component registrations for the extension.
- [protocol AUAudioUnitFactory](auaudiounitfactory.md)
  An object that creates a version 3 audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit)*