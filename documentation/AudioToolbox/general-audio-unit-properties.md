# General Audio Unit Properties

**Framework**: Audio Toolbox

Properties that apply to any audio unit.

#### Overview

The integer range for the set of generic audio unit property identifiers is 0 through 999.

## Topics

### Properties
- [var kAudioUnitProperty_ElementCount: AudioUnitPropertyID](kaudiounitproperty_elementcount.md)
  A read/write `UInt32` value valid on any audio unit scope. The global audio unit scope always has an element count of 1.
- [var kAudioUnitProperty_SupportedNumChannels: AudioUnitPropertyID](kaudiounitproperty_supportednumchannels.md)
  A read-only array of channel information structures valid on the audio unit global scope.
- [var kAudioUnitProperty_AudioChannelLayout: AudioUnitPropertyID](kaudiounitproperty_audiochannellayout.md)
  A read/write `AudioChannelLayout` data structure valid on the audio unit input and output scopes.
- [var kAudioUnitProperty_AudioUnitMIDIProtocol: AudioUnitPropertyID](kaudiounitproperty_audiounitmidiprotocol.md)
- [var kAudioUnitProperty_AUHostIdentifier: AudioUnitPropertyID](kaudiounitproperty_auhostidentifier.md)
- [var kAudioUnitProperty_BypassEffect: AudioUnitPropertyID](kaudiounitproperty_bypasseffect.md)
  A read/write `UInt32` value, representing a Boolean value, valid on the audio unit global scope.
- [var kAudioUnitProperty_ClassInfo: AudioUnitPropertyID](kaudiounitproperty_classinfo.md)
  Describes the state of an audio unit.
- [var kAudioUnitProperty_ClassInfoFromDocument: AudioUnitPropertyID](kaudiounitproperty_classinfofromdocument.md)
  A read/write CFDictionary object, valid on the audio unit global scope.
- [var kAudioUnitProperty_CocoaUI: AudioUnitPropertyID](kaudiounitproperty_cocoaui.md)
  A read-only `AudioUnitCocoaViewInfo` data structure valid on the audio unit global scope.
- [var kAudioUnitProperty_ContextName: AudioUnitPropertyID](kaudiounitproperty_contextname.md)
- [var kAudioUnitProperty_CPULoad: AudioUnitPropertyID](kaudiounitproperty_cpuload.md)
  A read-only `Float64` value valid on the audio unit global scope.
- [var kAudioUnitProperty_DependentParameters: AudioUnitPropertyID](kaudiounitproperty_dependentparameters.md)
- [var kAudioUnitProperty_ElementName: AudioUnitPropertyID](kaudiounitproperty_elementname.md)
  The name of the specified element.
- [var kAudioUnitProperty_FactoryPresets: AudioUnitPropertyID](kaudiounitproperty_factorypresets.md)
  So-called  (as opposed to user-configured presets) are ones supplied with an audio unit by the manufacturer. You choose the active preset by setting the `kAudioUnitProperty_PresentPreset` property.
- [var kAudioUnitProperty_FastDispatch: AudioUnitPropertyID](kaudiounitproperty_fastdispatch.md)
  A read-only `void *` value valid on the audio unit global scope.
- [var kAudioUnitProperty_FrequencyResponse: AudioUnitPropertyID](kaudiounitproperty_frequencyresponse.md)
- [var kAudioUnitProperty_GetUIComponentList: AudioUnitPropertyID](kaudiounitproperty_getuicomponentlist.md)
- [var kAudioUnitProperty_HostCallbacks: AudioUnitPropertyID](kaudiounitproperty_hostcallbacks.md)
- [var kAudioUnitProperty_HostMIDIProtocol: AudioUnitPropertyID](kaudiounitproperty_hostmidiprotocol.md)
- [var kAudioUnitProperty_IconLocation: AudioUnitPropertyID](kaudiounitproperty_iconlocation.md)
- [var kAudioUnitProperty_InPlaceProcessing: AudioUnitPropertyID](kaudiounitproperty_inplaceprocessing.md)
  A read/write `UInt32` value, representing a Boolean value, valid on the audio unit global scope.
- [var kAudioUnitProperty_InputSamplesInOutput: AudioUnitPropertyID](kaudiounitproperty_inputsamplesinoutput.md)
  A read/write AUInputSamplesInOutputCallbackStruct struct, valid on the audio unit global scope.
- [var kAudioUnitProperty_LastRenderError: AudioUnitPropertyID](kaudiounitproperty_lastrendererror.md)
  A read-only `OSStatus` value valid on the audio unit global scope.
- [var kAudioUnitProperty_LastRenderSampleTime: AudioUnitPropertyID](kaudiounitproperty_lastrendersampletime.md)
- [var kAudioUnitProperty_Latency: AudioUnitPropertyID](kaudiounitproperty_latency.md)
  A read-only `Float64` value valid on the audio unit global scope.
- [var kAudioUnitProperty_LoadedOutOfProcess: AudioUnitPropertyID](kaudiounitproperty_loadedoutofprocess.md)
- [var kAudioUnitProperty_MakeConnection: AudioUnitPropertyID](kaudiounitproperty_makeconnection.md)
  A write-only [`AudioUnitConnection`](audiounitconnection.md) data structure valid on the audio unit input scope.
- [var kAudioUnitProperty_MIDIOutputBufferSizeHint: AudioUnitPropertyID](kaudiounitproperty_midioutputbuffersizehint.md)
- [var kAudioUnitProperty_MIDIOutputCallback: AudioUnitPropertyID](kaudiounitproperty_midioutputcallback.md)
  A write-only AUMIDIOutputCallbackStruct struct, valid on the audio unit global scope.
- [var kAudioUnitProperty_MIDIOutputCallbackInfo: AudioUnitPropertyID](kaudiounitproperty_midioutputcallbackinfo.md)
  A read-only CFArray object valid on the audio unit global scope.
- [var kAudioUnitProperty_MIDIOutputEventListCallback: AudioUnitPropertyID](kaudiounitproperty_midioutputeventlistcallback.md)
- [var kAudioUnitProperty_MaximumFramesPerSlice: AudioUnitPropertyID](kaudiounitproperty_maximumframesperslice.md)
  Specifies the maximum number of sample frames an audio unit is prepared to supply on one invocation of its [`AudioUnitRender(_:_:_:_:_:_:)`](audiounitrender(_:_:_:_:_:_:).md) function.
- [var kAudioUnitProperty_NickName: AudioUnitPropertyID](kaudiounitproperty_nickname.md)
- [var kAudioUnitProperty_OfflineRender: AudioUnitPropertyID](kaudiounitproperty_offlinerender.md)
- [var kAudioUnitProperty_ParameterClumpName: AudioUnitPropertyID](kaudiounitproperty_parameterclumpname.md)
  A read-only `AudioUnitParameterNameInfo` struct, valid on any audio unit scope.
- [var kAudioUnitProperty_ParameterHistoryInfo: AudioUnitPropertyID](kaudiounitproperty_parameterhistoryinfo.md)
  For parameters that have the [`flag_PlotHistory`](audiounitparameteroptions/flag_plothistory.md) flag set, getting this property fills out the [`AudioUnitParameterHistoryInfo`](audiounitparameterhistoryinfo.md) struct containing the recommended update rate and history duration.
- [var kAudioUnitProperty_ParameterIDName: AudioUnitPropertyID](kaudiounitproperty_parameteridname.md)
  A shortened version of an audio unit parameter name, suitable for compact display situations.
- [var kAudioUnitProperty_ParameterInfo: AudioUnitPropertyID](kaudiounitproperty_parameterinfo.md)
- [var kAudioUnitProperty_ParameterList: AudioUnitPropertyID](kaudiounitproperty_parameterlist.md)
  A list of read-only parameter ID values valid on any audio unit scope.
- [var kAudioUnitProperty_ParameterStringFromValue: AudioUnitPropertyID](kaudiounitproperty_parameterstringfromvalue.md)
  A read-only [`AudioUnitParameterStringFromValue`](audiounitparameterstringfromvalue.md) struct, valid on any audio unit scope.
- [var kAudioUnitProperty_ParameterValueFromString: AudioUnitPropertyID](kaudiounitproperty_parametervaluefromstring.md)
- [var kAudioUnitProperty_ParameterValueStrings: AudioUnitPropertyID](kaudiounitproperty_parametervaluestrings.md)
  An array of names for a named, indexed audio unit parameter. An indexed parameter is one whose unit type is [`AudioUnitParameterUnit.indexed`](audiounitparameterunit/indexed.md). The array’s strings can be used to build a menu for the parameter.
- [var kAudioUnitProperty_ParametersForOverview: AudioUnitPropertyID](kaudiounitproperty_parametersforoverview.md)
- [var kAudioUnitProperty_PresentPreset: AudioUnitPropertyID](kaudiounitproperty_presentpreset.md)
  The active factory preset for an audio unit.
- [var kAudioUnitProperty_PresentationLatency: AudioUnitPropertyID](kaudiounitproperty_presentationlatency.md)
- [var kAudioUnitProperty_RenderQuality: AudioUnitPropertyID](kaudiounitproperty_renderquality.md)
  A read/write `UInt32` value valid on the audio unit global scope.
- [var kAudioUnitProperty_RequestViewController: AudioUnitPropertyID](kaudiounitproperty_requestviewcontroller.md)
- [var kAudioUnitProperty_SampleRate: AudioUnitPropertyID](kaudiounitproperty_samplerate.md)
- [var kAudioUnitProperty_SetExternalBuffer: AudioUnitPropertyID](kaudiounitproperty_setexternalbuffer.md)
- [var kAudioUnitProperty_SetRenderCallback: AudioUnitPropertyID](kaudiounitproperty_setrendercallback.md)
- [var kAudioUnitProperty_StreamFormat: AudioUnitPropertyID](kaudiounitproperty_streamformat.md)
- [var kAudioUnitProperty_ShouldAllocateBuffer: AudioUnitPropertyID](kaudiounitproperty_shouldallocatebuffer.md)
  A read/write `UInt32` value valid on the audio unit input and output scopes, settable individually on each element.
- [var kAudioUnitProperty_SupportedChannelLayoutTags: AudioUnitPropertyID](kaudiounitproperty_supportedchannellayouttags.md)
  A read-only array on `AudioChannelLayoutTag` structures, valid on the audio unit input and output scopes.
- [var kAudioUnitProperty_SupportsMPE: AudioUnitPropertyID](kaudiounitproperty_supportsmpe.md)
- [var kAudioUnitProperty_TailTime: AudioUnitPropertyID](kaudiounitproperty_tailtime.md)
  A read-only `Float64` value valid on the audio unit global scope.

## See Also

- [Other Plug-In Formats](1534082-other-plug-in-formats.md)
- [RenderQuality](1534177-renderquality.md)
  Render quality settings for audio units.
- [struct HostCallbackInfo](hostcallbackinfo.md)
  The time- and transport-related callback functions for an audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/general-audio-unit-properties)*