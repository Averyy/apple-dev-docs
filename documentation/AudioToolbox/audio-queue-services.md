# Audio Queue Services

**Framework**: Audiotoolbox

Connect to audio hardware and manage the recording or playback process.

#### Overview

This document describes Audio Queue Services, a C programming interface in the Audio Toolbox framework, which is part of Core Audio.

An audio queue is a software object you use for recording or playing audio. An audio queue does the work of:

- Connecting to audio hardware
- Managing memory
- Employing codecs, as needed, for compressed audio formats
- Mediating playback or recording

Audio Queue Services enables you to record and play audio in linear PCM, in compressed formats (such as Apple Lossless and AAC), and in other formats for which users have installed codecs. Audio Queue Services also supports scheduled playback and synchronization of multiple audio queues and synchronization of audio with video.

> **Note**:  Audio Queue Services provides features similar to those previously offered by the Sound Manager and in macOS. It adds additional features such as synchronization. The Sound Manager is deprecated in OS X v10.5 and does not work with 64-bit applications. Audio Queue Services is recommended for all new development and as a replacement for the Sound Manager in existing Mac apps.

## Topics

### Creating and Disposing of Audio Queues
- [func AudioQueueNewOutputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueOutputCallbackBlock) -> OSStatus](audioqueuenewoutputwithdispatchqueue(_:_:_:_:_:).md)
- [func AudioQueueNewInputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef?>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t, AudioQueueInputCallbackBlock) -> OSStatus](audioqueuenewinputwithdispatchqueue(_:_:_:_:_:).md)
- [func AudioQueueNewOutput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueOutputCallback, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, UInt32, UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](audioqueuenewoutput(_:_:_:_:_:_:_:).md)
  Creates a new playback audio queue object.
- [func AudioQueueNewInput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueInputCallback, UnsafeMutableRawPointer?, CFRunLoop?, CFString?, UInt32, UnsafeMutablePointer<AudioQueueRef?>) -> OSStatus](audioqueuenewinput(_:_:_:_:_:_:_:).md)
  Creates a new recording audio queue object.
- [func AudioQueueDispose(AudioQueueRef, Bool) -> OSStatus](audioqueuedispose(_:_:).md)
  Disposes of an audio queue.
- [typealias AudioQueueRef](audioqueueref.md)
  Defines an opaque data type that represents an audio queue.
- [typealias AudioQueueInputCallbackBlock](audioqueueinputcallbackblock.md)
- [typealias AudioQueueOutputCallbackBlock](audioqueueoutputcallbackblock.md)
### Controlling Audio Queues
- [func AudioQueueStart(AudioQueueRef, UnsafePointer<AudioTimeStamp>?) -> OSStatus](audioqueuestart(_:_:).md)
  Begins playing or recording audio.
- [func AudioQueuePrime(AudioQueueRef, UInt32, UnsafeMutablePointer<UInt32>?) -> OSStatus](audioqueueprime(_:_:_:).md)
  Decodes enqueued buffers in preparation for playback.
- [func AudioQueueFlush(AudioQueueRef) -> OSStatus](audioqueueflush(_:).md)
  Resets an audio queue’s decoder state.
- [func AudioQueueStop(AudioQueueRef, Bool) -> OSStatus](audioqueuestop(_:_:).md)
  Stops playing or recording audio.
- [func AudioQueuePause(AudioQueueRef) -> OSStatus](audioqueuepause(_:).md)
  Pauses audio playback or recording.
- [func AudioQueueReset(AudioQueueRef) -> OSStatus](audioqueuereset(_:).md)
  Resets an audio queue.
### Handling Audio Queue Buffers
- [func AudioQueueAllocateBuffer(AudioQueueRef, UInt32, UnsafeMutablePointer<AudioQueueBufferRef?>) -> OSStatus](audioqueueallocatebuffer(_:_:_:).md)
  Asks an audio queue object to allocate an audio queue buffer.
- [func AudioQueueAllocateBufferWithPacketDescriptions(AudioQueueRef, UInt32, UInt32, UnsafeMutablePointer<AudioQueueBufferRef?>) -> OSStatus](audioqueueallocatebufferwithpacketdescriptions(_:_:_:_:).md)
  Asks an audio queue object to allocate an audio queue buffer with space for packet descriptions.
- [func AudioQueueFreeBuffer(AudioQueueRef, AudioQueueBufferRef) -> OSStatus](audioqueuefreebuffer(_:_:).md)
  Asks an audio queue to dispose of an audio queue buffer.
- [func AudioQueueEnqueueBuffer(AudioQueueRef, AudioQueueBufferRef, UInt32, UnsafePointer<AudioStreamPacketDescription>?) -> OSStatus](audioqueueenqueuebuffer(_:_:_:_:).md)
  Adds a buffer to the buffer queue of a recording or playback audio queue.
- [func AudioQueueEnqueueBufferWithParameters(AudioQueueRef, AudioQueueBufferRef, UInt32, UnsafePointer<AudioStreamPacketDescription>?, UInt32, UInt32, UInt32, UnsafePointer<AudioQueueParameterEvent>?, UnsafePointer<AudioTimeStamp>?, UnsafeMutablePointer<AudioTimeStamp>?) -> OSStatus](audioqueueenqueuebufferwithparameters(_:_:_:_:_:_:_:_:_:_:).md)
  Adds a buffer to the buffer queue of a playback audio queue object, specifying start time and other settings.
### Tapping the Queue’s Audio
- [func AudioQueueProcessingTapNew(AudioQueueRef, AudioQueueProcessingTapCallback, UnsafeMutableRawPointer?, AudioQueueProcessingTapFlags, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamBasicDescription>, UnsafeMutablePointer<AudioQueueProcessingTapRef?>) -> OSStatus](audioqueueprocessingtapnew(_:_:_:_:_:_:_:).md)
- [func AudioQueueProcessingTapGetQueueTime(AudioQueueProcessingTapRef, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<UInt32>) -> OSStatus](audioqueueprocessingtapgetqueuetime(_:_:_:).md)
- [func AudioQueueProcessingTapGetSourceAudio(AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioQueueProcessingTapFlags>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](audioqueueprocessingtapgetsourceaudio(_:_:_:_:_:_:).md)
- [func AudioQueueProcessingTapDispose(AudioQueueProcessingTapRef) -> OSStatus](audioqueueprocessingtapdispose(_:).md)
### Manipulating Audio Queue Parameters
- [func AudioQueueGetParameter(AudioQueueRef, AudioQueueParameterID, UnsafeMutablePointer<AudioQueueParameterValue>) -> OSStatus](audioqueuegetparameter(_:_:_:).md)
  Gets an audio queue parameter value.
- [func AudioQueueSetParameter(AudioQueueRef, AudioQueueParameterID, AudioQueueParameterValue) -> OSStatus](audioqueuesetparameter(_:_:_:).md)
  Sets a playback audio queue parameter value.
### Manipulating Audio Queue Properties
- [func AudioQueueGetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audioqueuegetproperty(_:_:_:_:).md)
  Gets an audio queue property value.
- [func AudioQueueSetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeRawPointer, UInt32) -> OSStatus](audioqueuesetproperty(_:_:_:_:).md)
  Sets an audio queue property value.
- [func AudioQueueGetPropertySize(AudioQueueRef, AudioQueuePropertyID, UnsafeMutablePointer<UInt32>) -> OSStatus](audioqueuegetpropertysize(_:_:_:).md)
  Gets the size of the value of an audio queue property.
- [func AudioQueueAddPropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audioqueueaddpropertylistener(_:_:_:_:).md)
  Adds a property listener callback to an audio queue.
- [func AudioQueueRemovePropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audioqueueremovepropertylistener(_:_:_:_:).md)
  Removes a property listener callback from an audio queue.
### Managing the Timeline
- [func AudioQueueCreateTimeline(AudioQueueRef, UnsafeMutablePointer<AudioQueueTimelineRef?>) -> OSStatus](audioqueuecreatetimeline(_:_:).md)
  Creates a timeline object for an audio queue.
- [func AudioQueueDisposeTimeline(AudioQueueRef, AudioQueueTimelineRef) -> OSStatus](audioqueuedisposetimeline(_:_:).md)
  Disposes of an audio queue’s timeline object.
- [func AudioQueueDeviceGetCurrentTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](audioqueuedevicegetcurrenttime(_:_:).md)
  Gets the current time of the audio hardware device associated with an audio queue.
- [func AudioQueueDeviceGetNearestStartTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](audioqueuedevicegetneareststarttime(_:_:_:).md)
  Gets the start time, for an audio hardware device, that is closest to a requested start time.
- [func AudioQueueDeviceTranslateTime(AudioQueueRef, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](audioqueuedevicetranslatetime(_:_:_:).md)
  Converts the time for an audio queue’s associated audio hardware device from one time base representation to another.
- [func AudioQueueGetCurrentTime(AudioQueueRef, AudioQueueTimelineRef?, UnsafeMutablePointer<AudioTimeStamp>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audioqueuegetcurrenttime(_:_:_:_:).md)
  Gets the current audio queue time.
- [typealias AudioQueueTimelineRef](audioqueuetimelineref.md)
  Defines an opaque data type that represents an audio queue timeline object.
### Performing Offline Rendering
- [func AudioQueueSetOfflineRenderFormat(AudioQueueRef, UnsafePointer<AudioStreamBasicDescription>?, UnsafePointer<AudioChannelLayout>?) -> OSStatus](audioqueuesetofflinerenderformat(_:_:_:).md)
  Sets the rendering mode and audio format for a playback audio queue.
- [func AudioQueueOfflineRender(AudioQueueRef, UnsafePointer<AudioTimeStamp>, AudioQueueBufferRef, UInt32) -> OSStatus](audioqueueofflinerender(_:_:_:_:).md)
  Exports audio to a buffer, instead of to a device, using a playback audio queue.
### Callbacks
- [typealias AudioQueueInputCallback](audioqueueinputcallback.md)
  Called by the system when a recording audio queue has finished filling an audio queue buffer.
- [typealias AudioQueueOutputCallback](audioqueueoutputcallback.md)
  Called by the system when an audio queue buffer is available for reuse.
- [typealias AudioQueuePropertyListenerProc](audioqueuepropertylistenerproc.md)
  Called by the system when a specified audio queue property changes value.
### Data Types
- [struct AudioQueueChannelAssignment](audioqueuechannelassignment.md)
- [struct AudioQueueProcessingTapFlags](audioqueueprocessingtapflags.md)
- [struct AudioQueueBuffer](audioqueuebuffer.md)
  Defines an audio queue buffer.
- [typealias AudioQueueBufferRef](audioqueuebufferref.md)
  A pointer to an audio queue buffer.
- [struct AudioQueueLevelMeterState](audioqueuelevelmeterstate.md)
  Specifies the current level metering information for one channel of an audio queue.
- [struct AudioQueueParameterEvent](audioqueueparameterevent.md)
  Specifies an audio queue parameter and associated value.
- [typealias AudioQueueParameterID](audioqueueparameterid.md)
  A `UInt32` value that uniquely identifies an audio queue parameter.
- [typealias AudioQueueParameterValue](audioqueueparametervalue.md)
  A `Float32` value for an audio queue parameter.
- [typealias AudioQueueProcessingTapCallback](audioqueueprocessingtapcallback.md)
- [typealias AudioQueueProcessingTapRef](audioqueueprocessingtapref.md)
### Structures
- [struct AudioUnitConnection](audiounitconnection.md)
  An audio unit source-to-destination connection specification.
- [struct AudioUnitEvent](audiounitevent.md)
- [struct AudioUnitExternalBuffer](audiounitexternalbuffer.md)
  Allows an audio unit host application to tell an audio unit to use a specified buffer for its input callback.
- [struct AudioUnitFrequencyResponseBin](audiounitfrequencyresponsebin.md)
  An audio unit’s audio level at a particular frequency.
- [struct AudioUnitMeterClipping](audiounitmeterclipping.md)
  Audio clipping that has occurred in a mixer unit.
- [struct AudioUnitMIDIControlMapping](audiounitmidicontrolmapping.md)
- [struct AudioUnitOtherPluginDesc](audiounitotherplugindesc.md)
- [struct AudioUnitParameter](audiounitparameter.md)
  An adjustable audio unit attribute such as volume, pitch, or filter cutoff frequency.
- [struct AudioUnitParameterEvent](audiounitparameterevent.md)
  A scheduled change to an audio unit parameter’s value.
- [struct AudioUnitParameterHistoryInfo](audiounitparameterhistoryinfo.md)
  The suggested update rate and history duration for parameters which have the [`flag_PlotHistory`](audiounitparameteroptions/flag_plothistory.md) flag set.
- [struct AudioUnitParameterNameInfo](audiounitparameternameinfo.md)
  A short version of the name for an audio unit parameter.
- [typealias AudioUnitParameterIDName](audiounitparameteridname.md)
  A type definition for a data type that defines the short version of the name for an audio unit parameter.
- [struct AudioUnitParameterInfo](audiounitparameterinfo.md)
- [struct AudioUnitParameterOptions](audiounitparameteroptions.md)
  Value options for audio unit parameters.
- [struct AudioUnitParameterStringFromValue](audiounitparameterstringfromvalue.md)
  A string representation of a parameter’s value.
- [struct AudioUnitParameterValueFromString](audiounitparametervaluefromstring.md)
  A parameter’s value based on a string representation of the value.
- [struct AudioUnitParameterValueName](audiounitparametervaluename.md)
- [struct AudioUnitParameterValueTranslation](audiounitparametervaluetranslation.md)
- [struct AudioUnitPresetMAS_SettingData](audiounitpresetmas_settingdata.md)
- [struct AudioUnitPresetMAS_Settings](audiounitpresetmas_settings.md)
- [struct AudioUnitProperty](audiounitproperty.md)
  A key-value pair that declares an attribute or behavior for an audio unit.
- [struct AudioUnitRenderActionFlags](audiounitrenderactionflags.md)
  Flags for configuring audio unit rendering.
- [struct AU3DMixerRenderingFlags](au3dmixerrenderingflags.md)
- [struct AUChannelInfo](auchannelinfo.md)
  The audio input and output channel capabilities for an audio unit.
- [struct AUDependentParameter](audependentparameter.md)
  An audio unit parameter whose value can change in response to a change in its parent metaparameter.
- [struct AUDistanceAttenuationData](audistanceattenuationdata.md)
- [struct AUHostIdentifier](auhostidentifier.md)
- [struct AUHostTransportStateFlags](auhosttransportstateflags.md)
- [struct AUHostVersionIdentifier](auhostversionidentifier.md)
  The name and version of an audio unit’s host application.
- [struct AUInputSamplesInOutputCallbackStruct](auinputsamplesinoutputcallbackstruct.md)
  The callback function and custom data for providing input-to-output sample mapping for an audio unit.
- [struct AUMIDIEvent](aumidievent.md)
  A structure that describes a scheduled MIDI event.
- [struct AUMIDIOutputCallbackStruct](aumidioutputcallbackstruct.md)
  The callback function and custom data for an audio unit that provides MIDI output.
- [struct AUNumVersion](aunumversion.md)
- [struct AUParameterAutomationEvent](auparameterautomationevent.md)
- [struct AUParameterEvent](auparameterevent.md)
  A structure that describes a scheduled parameter event.
- [struct AUParameterMIDIMapping](auparametermidimapping.md)
- [struct AUParameterMIDIMappingFlags](auparametermidimappingflags.md)
- [struct AUPreset](aupreset.md)
  Used to set factory presets for an audio unit.
- [struct AUPresetEvent](aupresetevent.md)
  Describes an audio unit preset.
- [struct AURecordedParameterEvent](aurecordedparameterevent.md)
  An event recording the changing of a parameter at a particular host time.
- [struct AURenderCallbackStruct](aurendercallbackstruct.md)
  Used for registering an input callback function with an audio unit.
- [struct AURenderEvent](aurenderevent.md)
  A union of the various specific render event types.
- [struct AURenderEventHeader](aurendereventheader.md)
  The common header for a render event.
- [struct AUSamplerBankPresetData](ausamplerbankpresetdata.md)
- [struct AUSamplerInstrumentData](ausamplerinstrumentdata.md)
- [struct AUScheduledAudioSliceFlags](auscheduledaudiosliceflags.md)
- [struct AUSpatialMixerRenderingFlags](auspatialmixerrenderingflags.md)
### Enumerations
- [struct AudioQueueProcessingTapFlags](audioqueueprocessingtapflags.md)
- [Anonymous](1552627-anonymous.md)
- [Audio Queue Time Pitch Algorithms](1552630-audio-queue-time-pitch-algorithm.md)
- [Audio Queue Property IDs](1552629-audio-queue-property-ids.md)
- [Audio Queue Property IDs](1618733-audio-queue-property-ids.md)
- [Audio Queue Hardware Codec Policy](1618727-audio-queue-hardware-codec-polic.md)
### Constants
- [typealias AudioQueuePropertyID](audioqueuepropertyid.md)
  Identifiers for audio queue properties.
- [Audio Queue Parameters](1552626-audio-queue-parameters.md)
  Identifiers for audio queue parameters.
- [Hardware Codec Policy Keys](1618724-hardware-codec-policy-keys.md)
  Indicates how an audio queue should choose between hardware and software implementations of a codec.
### Result Codes
- [var kAudioQueueErr_InvalidBuffer: OSStatus](kaudioqueueerr_invalidbuffer.md)
  The specified audio queue buffer does not belong to the specified audio queue.
- [var kAudioQueueErr_BufferEmpty: OSStatus](kaudioqueueerr_bufferempty.md)
  The audio queue buffer is empty (that is, the `mAudioDataByteSize` field = `0`).
- [var kAudioQueueErr_DisposalPending: OSStatus](kaudioqueueerr_disposalpending.md)
  The function cannot act on the audio queue because it is being asynchronously disposed of.
- [var kAudioQueueErr_InvalidProperty: OSStatus](kaudioqueueerr_invalidproperty.md)
  The specified property ID is invalid.
- [var kAudioQueueErr_InvalidPropertySize: OSStatus](kaudioqueueerr_invalidpropertysize.md)
  The size of the specified property is invalid.
- [var kAudioQueueErr_InvalidParameter: OSStatus](kaudioqueueerr_invalidparameter.md)
  The specified parameter ID is invalid.
- [var kAudioQueueErr_CannotStart: OSStatus](kaudioqueueerr_cannotstart.md)
  The audio queue has encountered a problem and cannot start.
- [var kAudioQueueErr_InvalidDevice: OSStatus](kaudioqueueerr_invaliddevice.md)
  The specified audio hardware device could not be located.
- [var kAudioQueueErr_BufferInQueue: OSStatus](kaudioqueueerr_bufferinqueue.md)
  The audio queue buffer cannot be disposed of when it is enqueued.
- [var kAudioQueueErr_InvalidRunState: OSStatus](kaudioqueueerr_invalidrunstate.md)
  The queue is running but the function can only operate on the queue when it is stopped, or vice versa.
- [var kAudioQueueErr_InvalidQueueType: OSStatus](kaudioqueueerr_invalidqueuetype.md)
  The queue is an input queue but the function can only operate on an output queue, or vice versa.
- [var kAudioQueueErr_Permissions: OSStatus](kaudioqueueerr_permissions.md)
  You do not have the required permissions to call the function.
- [var kAudioQueueErr_InvalidPropertyValue: OSStatus](kaudioqueueerr_invalidpropertyvalue.md)
  The property value used is not valid.
- [var kAudioQueueErr_PrimeTimedOut: OSStatus](kaudioqueueerr_primetimedout.md)
  During a call to the [`AudioQueuePrime(_:_:_:)`](audioqueueprime(_:_:_:).md) function, the audio queue’s audio converter failed to convert the requested number of sample frames.
- [var kAudioQueueErr_CodecNotFound: OSStatus](kaudioqueueerr_codecnotfound.md)
  The requested codec was not found.
- [var kAudioQueueErr_InvalidCodecAccess: OSStatus](kaudioqueueerr_invalidcodecaccess.md)
  The codec could not be accessed.
- [var kAudioQueueErr_QueueInvalidated: OSStatus](kaudioqueueerr_queueinvalidated.md)
  In iOS, the audio server has exited, causing the audio queue to become invalid.
- [var kAudioQueueErr_RecordUnderrun: OSStatus](kaudioqueueerr_recordunderrun.md)
  During recording, data was lost because there was no enqueued buffer to store it in.
- [var kAudioQueueErr_EnqueueDuringReset: OSStatus](kaudioqueueerr_enqueueduringreset.md)
  During a call to the [`AudioQueueReset(_:)`](audioqueuereset(_:).md), [`AudioQueueStop(_:_:)`](audioqueuestop(_:_:).md), or [`AudioQueueDispose(_:_:)`](audioqueuedispose(_:_:).md) functions, the system does not allow you to enqueue buffers.
- [var kAudioQueueErr_InvalidOfflineMode: OSStatus](kaudioqueueerr_invalidofflinemode.md)
  The operation requires the audio queue to be in offline mode but it isn’t, or vice versa.
- [var kAudioFormatUnsupportedDataFormatError: OSStatus](kaudioformatunsupporteddataformaterror.md)
  The playback data format is unsupported (declared in `AudioFormat.h`).

## See Also

- [Audio Services](audio-services.md)
  Play short sounds or trigger a vibration effect on iOS devices with the appropriate hardware.
- [Music Player](music-player.md)
  Create and play a sequence of tracks, and manage aspects of playback in response to standard events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AudioToolbox/audio-queue-services)*