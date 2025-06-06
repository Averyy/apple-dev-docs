# Audio Unit v2 (C) API

**Framework**: Audio Toolbox

Configure an Audio Unit and prepare it to render audio.

## Topics

### Initializing the Audio Unit
- [func AudioUnitInitialize(AudioUnit) -> OSStatus](audiounitinitialize(_:).md)
  Initializes an audio unit
- [func AudioUnitUninitialize(AudioUnit) -> OSStatus](audiounituninitialize(_:).md)
  Uninitializes an audio unit.
- [func AudioUnitProcess(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](audiounitprocess(_:_:_:_:_:).md)
- [func AudioUnitProcessMultiple(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus](audiounitprocessmultiple(_:_:_:_:_:_:_:_:).md)
- [func AudioUnitReset(AudioUnit, AudioUnitScope, AudioUnitElement) -> OSStatus](audiounitreset(_:_:_:).md)
  Resets an audio unit’s render state.
- [typealias AudioUnit](audiounit.md)
  The data type for a plug-in component that provides audio processing or audio data generation.
### Starting and Stopping Output
- [func AudioOutputUnitStart(AudioUnit) -> OSStatus](audiooutputunitstart(_:).md)
  Starts an I/O audio unit, which in turn starts the audio unit processing graph that it is connected to.
- [func AudioOutputUnitStop(AudioUnit) -> OSStatus](audiooutputunitstop(_:).md)
  Stops an I/O audio unit, which in turn stops the audio unit processing graph that it is connected to.
- [typealias AudioOutputUnitStartProc](audiooutputunitstartproc.md)
- [typealias AudioOutputUnitStopProc](audiooutputunitstopproc.md)
### Rendering the Audio
- [func AudioUnitRender(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](audiounitrender(_:_:_:_:_:_:).md)
  Initiates a rendering cycle for an audio unit.
- [func AudioUnitAddRenderNotify(AudioUnit, AURenderCallback, UnsafeMutableRawPointer?) -> OSStatus](audiounitaddrendernotify(_:_:_:).md)
  Registers a callback to receive audio unit render notifications.
- [func AudioUnitRemoveRenderNotify(AudioUnit, AURenderCallback, UnsafeMutableRawPointer?) -> OSStatus](audiounitremoverendernotify(_:_:_:).md)
  Unregisters a previously-registered render listener callback function.
- [typealias AURenderCallback](aurendercallback.md)
  Called by the system when an audio unit requires input samples, or before and after a render operation.
- [struct AudioUnitRenderActionFlags](audiounitrenderactionflags.md)
  Flags for configuring audio unit rendering.
### Configuring Audio Unit Properties
- [func AudioUnitGetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audiounitgetproperty(_:_:_:_:_:_:).md)
  Gets the value of an audio unit property.
- [func AudioUnitSetProperty(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeRawPointer?, UInt32) -> OSStatus](audiounitsetproperty(_:_:_:_:_:_:).md)
  Sets the value of an audio unit property.
- [func AudioUnitGetPropertyInfo(AudioUnit, AudioUnitPropertyID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audiounitgetpropertyinfo(_:_:_:_:_:_:).md)
  Gets information about an audio unit property.
- [func AudioUnitAddPropertyListener(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audiounitaddpropertylistener(_:_:_:_:).md)
  Registers a callback to receive audio unit property change notifications.
- [func AudioUnitRemovePropertyListenerWithUserData(AudioUnit, AudioUnitPropertyID, AudioUnitPropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audiounitremovepropertylistenerwithuserdata(_:_:_:_:).md)
  Unregisters a previously-registered property listener callback function.
### Responding to Events
- [func AUEventListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUEventListenerRef?>, Float32, Float32, dispatch_queue_t, AUEventListenerBlock) -> OSStatus](aueventlistenercreatewithdispatchqueue(_:_:_:_:_:).md)
- [func AUEventListenerCreate(AUEventListenerProc, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, Float32, Float32, UnsafeMutablePointer<AUEventListenerRef?>) -> OSStatus](aueventlistenercreate(_:_:_:_:_:_:_:).md)
- [func AUListenerDispose(AUParameterListenerRef) -> OSStatus](aulistenerdispose(_:).md)
- [func AUEventListenerNotify(AUEventListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](aueventlistenernotify(_:_:_:).md)
- [func AUEventListenerAddEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](aueventlisteneraddeventtype(_:_:_:).md)
- [func AUEventListenerRemoveEventType(AUEventListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitEvent>) -> OSStatus](aueventlistenerremoveeventtype(_:_:_:).md)
- [func AUListenerAddParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](aulisteneraddparameter(_:_:_:).md)
- [func AUListenerRemoveParameter(AUParameterListenerRef, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](aulistenerremoveparameter(_:_:_:).md)
- [typealias AUEventListenerBlock](aueventlistenerblock.md)
### Getting and Setting Parameters
- [func AudioUnitGetParameter(AudioUnit, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<AudioUnitParameterValue>) -> OSStatus](audiounitgetparameter(_:_:_:_:_:).md)
  Gets the value of an audio unit parameter.
- [func AudioUnitScheduleParameters(AudioUnit, UnsafePointer<AudioUnitParameterEvent>, UInt32) -> OSStatus](audiounitscheduleparameters(_:_:_:).md)
  Schedules changes to the value of an audio unit parameter.
- [func AudioUnitSetParameter(AudioUnit, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, AudioUnitParameterValue, UInt32) -> OSStatus](audiounitsetparameter(_:_:_:_:_:_:).md)
  Sets the value of an audio unit parameter.
### Monitoring Parameter Changes
- [func AUListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUParameterListenerRef?>, Float32, dispatch_queue_t, AUParameterListenerBlock) -> OSStatus](aulistenercreatewithdispatchqueue(_:_:_:_:).md)
- [func AUListenerCreate(AUParameterListenerProc, UnsafeMutableRawPointer, CFRunLoop?, CFString?, Float32, UnsafeMutablePointer<AUParameterListenerRef?>) -> OSStatus](aulistenercreate(_:_:_:_:_:_:).md)
- [func AUParameterListenerNotify(AUParameterListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>) -> OSStatus](auparameterlistenernotify(_:_:_:).md)
- [func AUParameterFormatValue(Float64, UnsafePointer<AudioUnitParameter>, UnsafeMutablePointer<CChar>, UInt32) -> UnsafeMutablePointer<CChar>](auparameterformatvalue(_:_:_:_:).md)
- [func AUParameterSet(AUParameterListenerRef?, UnsafeMutableRawPointer?, UnsafePointer<AudioUnitParameter>, AudioUnitParameterValue, UInt32) -> OSStatus](auparameterset(_:_:_:_:_:).md)
- [func AUParameterValueFromLinear(Float32, UnsafePointer<AudioUnitParameter>) -> AudioUnitParameterValue](auparametervaluefromlinear(_:_:).md)
- [func AUParameterValueToLinear(AudioUnitParameterValue, UnsafePointer<AudioUnitParameter>) -> Float32](auparametervaluetolinear(_:_:).md)
- [typealias AUParameterListenerBlock](auparameterlistenerblock.md)
- [typealias AUParameterListenerProc](auparameterlistenerproc.md)
- [typealias AUParameterListenerRef](auparameterlistenerref.md)
- [typealias AUImplementorDisplayNameWithLengthCallback](auimplementordisplaynamewithlengthcallback.md)
  A block called to obtain a parameter node’s display name, possibly truncated to a desired length.
- [typealias AUImplementorStringFromValueCallback](auimplementorstringfromvaluecallback.md)
  A block called to convert a parameter value to a string representation.
- [typealias AUImplementorValueFromStringCallback](auimplementorvaluefromstringcallback.md)
  A block called to convert a string to a parameter value.
### Getting Information from the Host
- [typealias HostCallback_GetBeatAndTempo](hostcallback_getbeatandtempo.md)
  When called by the system, provides beat and tempo information to an audio unit from a host application.
- [typealias HostCallback_GetMusicalTimeLocation](hostcallback_getmusicaltimelocation.md)
  When called by the system, provides musical timing information to an audio unit from a host application.
- [typealias HostCallback_GetTransportState](hostcallback_gettransportstate.md)
  When called by the system, provides audio transport state and timeline information to an audio unit from a host application.
- [typealias HostCallback_GetTransportState2](hostcallback_gettransportstate2.md)
- [typealias AUInputSamplesInOutputCallback](auinputsamplesinoutputcallback.md)
  Called by the system when an audio unit has provided a buffer of output samples.
- [typealias AUMIDIOutputCallback](aumidioutputcallback.md)
  When called by a host application, gets MIDI data from an audio unit.
### Getting the Configuration Information
- [var kAudioUnitConfigurationInfo_BusCountWritable: String](kaudiounitconfigurationinfo_buscountwritable.md)
- [var kAudioUnitConfigurationInfo_ChannelConfigurations: String](kaudiounitconfigurationinfo_channelconfigurations.md)
- [var kAudioUnitConfigurationInfo_HasCustomView: String](kaudiounitconfigurationinfo_hascustomview.md)
- [var kAudioUnitConfigurationInfo_IconURL: String](kaudiounitconfigurationinfo_iconurl.md)
- [var kAudioUnitConfigurationInfo_InitialInputs: String](kaudiounitconfigurationinfo_initialinputs.md)
- [var kAudioUnitConfigurationInfo_InitialOutputs: String](kaudiounitconfigurationinfo_initialoutputs.md)
- [var kAudioUnitConfigurationInfo_SupportedChannelLayoutTags: String](kaudiounitconfigurationinfo_supportedchannellayouttags.md)
### Configuring the Audio Unit UI
- [struct AudioUnitCocoaViewInfo](audiounitcocoaviewinfo.md)
  The name and number of custom Cocoa views for an audio unit.
- [func GetAudioUnitParameterDisplayType(AudioUnitParameterOptions) -> AudioUnitParameterOptions](getaudiounitparameterdisplaytype(_:).md)
- [func SetAudioUnitParameterDisplayType(AudioUnitParameterOptions, AudioUnitParameterOptions) -> AudioUnitParameterOptions](setaudiounitparameterdisplaytype(_:_:).md)
### Audio Unit Types
- [struct ScheduledAudioFileRegion](scheduledaudiofileregion.md)
- [struct ScheduledAudioSlice](scheduledaudioslice.md)
- [typealias ScheduledAudioFileRegionCompletionProc](scheduledaudiofileregioncompletionproc.md)
- [typealias ScheduledAudioSliceCompletionProc](scheduledaudioslicecompletionproc.md)
- [typealias MIDIChannelNumber](midichannelnumber.md)
  MIDI Channel, 0~15 (channels 1 through 16, respectively).
- [typealias AUAudioObjectID](auaudioobjectid.md)
- [typealias AUMIDICIProfileChangedBlock](aumidiciprofilechangedblock.md)
- [typealias AUAudioChannelCount](auaudiochannelcount.md)
  A number of audio channels.
- [typealias AUAudioFrameCount](auaudioframecount.md)
  A number of audio sample frames.
- [typealias AUAudioUnitStatus](auaudiounitstatus.md)
  A result code returned from an audio unit’s render function.
- [typealias AUEventListenerProc](aueventlistenerproc.md)
- [typealias AUEventListenerRef](aueventlistenerref.md)
- [typealias AUEventSampleTime](aueventsampletime.md)
  Expresses time as a sample count.
- [typealias AUImplementorValueObserver](auimplementorvalueobserver.md)
  A block called to notify the audio unit implementation of changes to a parameter value.
- [typealias AUImplementorValueProvider](auimplementorvalueprovider.md)
  A block called to fetch a parameter’s current value from the audio unit implementation.
- [typealias AUInputHandler](auinputhandler.md)
  A block to notify the host of an I/O unit that an input is available.
- [typealias AUNodeConnection](aunodeconnection.md)
- [typealias AUParameterAddress](auparameteraddress.md)
  A numeric identifier for an audio unit parameter.
- [typealias AUParameterAutomationObserver](auparameterautomationobserver.md)
- [typealias AUParameterObserver](auparameterobserver.md)
  A block called after the value of a parameter changes.
- [typealias AUParameterObserverToken](auparameterobservertoken.md)
  A token representing an installed parameter observer block.
- [typealias AUParameterRecordingObserver](auparameterrecordingobserver.md)
  A block called to record parameter changes as automation events.
- [typealias AURenderBlock](aurenderblock.md)
  A block to render the audio unit.
- [typealias AURenderObserver](aurenderobserver.md)
  A block called when an audio unit renders audio.
- [typealias AURenderPullInputBlock](aurenderpullinputblock.md)
  A block to supply audio input to a render block.
- [typealias AUScheduleParameterBlock](auscheduleparameterblock.md)
  A block to schedule parameter changes.
- [typealias AUValue](auvalue.md)
  A value of an audio unit parameter.
- [typealias AudioUnitAddPropertyListenerProc](audiounitaddpropertylistenerproc.md)
- [typealias AudioUnitAddRenderNotifyProc](audiounitaddrendernotifyproc.md)
- [typealias AudioUnitComplexRenderProc](audiounitcomplexrenderproc.md)
- [typealias AudioUnitElement](audiounitelement.md)
  The data type for an audio unit element identifier.
- [typealias AudioUnitGetParameterProc](audiounitgetparameterproc.md)
- [typealias AudioUnitGetPropertyInfoProc](audiounitgetpropertyinfoproc.md)
- [typealias AudioUnitGetPropertyProc](audiounitgetpropertyproc.md)
- [typealias AudioUnitInitializeProc](audiounitinitializeproc.md)
- [typealias AudioUnitParameterID](audiounitparameterid.md)
  The data type for an audio unit parameter identifier.
- [struct AudioUnitParameterNameInfo](audiounitparameternameinfo.md)
  A short version of the name for an audio unit parameter.
- [typealias AudioUnitParameterIDName](audiounitparameteridname.md)
  A type definition for a data type that defines the short version of the name for an audio unit parameter.
- [typealias AudioUnitParameterValue](audiounitparametervalue.md)
  The data type for an audio unit parameter value.
- [typealias AudioUnitProcessMultipleProc](audiounitprocessmultipleproc.md)
- [typealias AudioUnitProcessProc](audiounitprocessproc.md)
- [typealias AudioUnitPropertyID](audiounitpropertyid.md)
  The data type for audio unit property keys.
- [typealias AudioUnitPropertyListenerProc](audiounitpropertylistenerproc.md)
  Called by the system when the value of a specified audio unit property has changed.
- [typealias AudioUnitRemoteControlEventListener](audiounitremotecontroleventlistener.md)
- [typealias AudioUnitRemovePropertyListenerProc](audiounitremovepropertylistenerproc.md)
- [typealias AudioUnitRemovePropertyListenerWithUserDataProc](audiounitremovepropertylistenerwithuserdataproc.md)
- [typealias AudioUnitRemoveRenderNotifyProc](audiounitremoverendernotifyproc.md)
- [typealias AudioUnitRenderProc](audiounitrenderproc.md)
- [typealias AudioUnitResetProc](audiounitresetproc.md)
- [typealias AudioUnitScheduleParametersProc](audiounitscheduleparametersproc.md)
- [typealias AudioUnitScope](audiounitscope.md)
  The data type for audio unit scope identifiers.
- [typealias AudioUnitSetParameterProc](audiounitsetparameterproc.md)
- [typealias AudioUnitSetPropertyProc](audiounitsetpropertyproc.md)
- [typealias AudioUnitUninitializeProc](audiounituninitializeproc.md)
### Enumerations
- [Audio Unit Types](1584142-audio_unit_types.md)
  The defined types of audio processing plug-ins known as audio units.
- [Inter-App Audio Unit Types](1619501-inter-app-audio-unit-types.md)
- [Audio Unit Manufacturer Identifier](1584143-audio_unit_manufacturer_identifi.md)
  The Apple audio unit manufacturer code.
- [Audio Unit Output Subtypes](1584148-audio-unit-output-subtypes.md)
- [I/O Audio Unit Subtypes](1619485-i-o-audio-unit-subtypes.md)
- [Converter Audio Unit Subtypes](1584145-converter_audio_unit_subtypes.md)
  Audio data format converter audio unit subtypes for audio units provided by Apple.
- [Reserved Audio Unit Clump Identifier](1533986-reserved_audio_unit_clump_identi.md)
  Reserved for system use.
- [Offline Audio Unit Properties](1534054-offline_audio_unit_properties.md)
  Properties for audio units that perform offline processing—that is, processing in a nonplayback, nonrealtime mode.
- [MIDI Audio Unit Parameters](1389613-midi_audio_unit_parameters.md)
  Parameters for instrument units.
- [General Audio Unit Function Selectors](1584140-general_audio_unit_function_sele.md)
  General audio unit component selectors that correspond to functions in the audio unit API.
- [Generator Audio Unit Subtypes](1619493-generator_audio_unit_subtypes.md)
  Audio units that serve as sound sources.
- [Input/Output Audio Unit Subtypes](1584139-input_output_audio_unit_subtypes.md)
  Input/output audio unit subtypes for audio units provided by Apple.
- [Audio Unit Panner Subtypes](1584151-audio-unit-panner-subtypes.md)
- [Audio Unit Player Subtypes](1584155-audio-unit-player-subtypes.md)
- [Audio Unit Pitch Subtypes](1584152-audio-unit-pitch-subtypes.md)
- [enum AudioUnitEventType](audiouniteventtype.md)
- [struct AudioUnitParameterOptions](audiounitparameteroptions.md)
  Value options for audio unit parameters.
- [enum AudioUnitParameterUnit](audiounitparameterunit.md)
  The unit-of-measure for an audio unit parameter.
- [enum AudioUnitRemoteControlEvent](audiounitremotecontrolevent.md)
- [Audio Unit Sample Rate Converter Complexity](1534173-audio_unit_sample_rate_converter.md)
  Quality levels for the audio sample-rate conversion algorithm.
- [Audio Unit Scopes](1534214-audio_unit_scopes.md)
  Programmatic roles and contexts for audio unit properties.
- [Audio Unit SRC Algorithms](1533994-audio-unit-src-algorithms.md)
- [Audio Unit Full Name Parameter](1534055-audio-unit-full-name-parameter.md)
- [Audio Unit Parameter Flags](1534035-audio-unit-parameter-flags.md)
- [Audio Unit Filter Parameters](1390052-audio-unit-filter-parameters.md)
- [Audio Unit Generic Properties](1533969-audio-unit-generic-properties.md)
- [Audio Unit Parameter Flags](1534166-audio-unit-parameter-flags.md)
- [Audio Unit Scheduled Sound Player Properties](1534024-audio-unit-scheduled-sound-playe.md)
- [Audio Unit Offline Preflight Flags](1534010-audio-unit-offline-preflight-fla.md)
- [Audio Unit Migration Properties](1534149-audio-unit-migration-properties.md)
- [Audio Unit File Player Properties](1534079-audio-unit-file-player-propertie.md)
- [Audio Unit Parameter Listener](1509425-audio-unit-parameter-listener.md)
- [Audio Unit Errors](1584138-audio-unit-errors.md)
- [enum AUAudioUnitBusType](auaudiounitbustype.md)
- [AUEventSampleTime](1387633-aueventsampletime.md)
  Expresses time as a sample count.
- [struct AUHostTransportStateFlags](auhosttransportstateflags.md)
- [enum AUParameterAutomationEventType](auparameterautomationeventtype.md)
- [enum AUParameterEventType](auparametereventtype.md)
  Audio unit parameter event types.
- [enum AURenderEventType](aurendereventtype.md)
- [struct AUScheduledAudioSliceFlags](auscheduledaudiosliceflags.md)
- [struct AUParameterMIDIMappingFlags](auparametermidimappingflags.md)

## See Also

- [Generating spatial audio from a multichannel audio stream](generating-spatial-audio-from-a-multichannel-audio-stream.md)
  Convert 8-channel audio to 2-channel spatial audio by using a spatial mixer audio unit.
- [Audio Unit v3 Plug-Ins](audio-unit-v3-plug-ins.md)
  Deliver custom audio effects, instruments, and other audio behaviors using an Audio Unit v3 app extension.
- [Audio Components](audio-components.md)
  Find, load, and configure audio components, such as Audio Units and audio codecs.
- [Audio Unit Properties](audio-unit-properties.md)
  Obtain information about the built-in mixers, equalizers, filters, effects, and other Audio Unit app extensions.
- [Audio Unit Voice I/O](audio-unit-voice-i-o.md)
  Configure system voice processing and respond to speech events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-unit-v2-c-api)*