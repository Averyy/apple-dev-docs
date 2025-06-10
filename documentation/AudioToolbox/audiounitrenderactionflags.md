# AudioUnitRenderActionFlags

**Framework**: Audio Toolbox  
**Kind**: struct

Flags for configuring audio unit rendering.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioUnitRenderActionFlags
```

#### Overview

These flags can be set in a callback from an audio unit during an audio unit render operation from either the `RenderNotify` Proc or the render input callback.

## Topics

### Constants
- [static var unitRenderAction_PreRender: AudioUnitRenderActionFlags](audiounitrenderactionflags/unitrenderaction_prerender.md)
  Called on a render notification Proc - which is called either before or after the render operation of the audio unit. If this flag is set, the proc is being called before the render operation is performed.
- [static var unitRenderAction_PostRender: AudioUnitRenderActionFlags](audiounitrenderactionflags/unitrenderaction_postrender.md)
  Called on a render notification Proc - which is called either before or after the render operation of the audio unit. If this flag is set, the proc is being called after the render operation is completed.
- [static var unitRenderAction_OutputIsSilence: AudioUnitRenderActionFlags](audiounitrenderactionflags/unitrenderaction_outputissilence.md)
  This flag can be set in a render input callback (or in the audio unit’s render operation itself) and is used to indicate that the render buffer contains only silence. It can then be used by the caller as a hint to whether the buffer needs to be processed or not.
- [static var offlineUnitRenderAction_Preflight: AudioUnitRenderActionFlags](audiounitrenderactionflags/offlineunitrenderaction_preflight.md)
  This is used with offline audio units (of type `'auol'`). It is used when an offline unit is being preflighted, which is performed prior to the actual offline rendering actions are performed. It is used for those cases where the offline process needs it (for example, with an offline unit that normalizes an audio file, it needs to see all of the audio data first before it can perform its normalization).
- [static var offlineUnitRenderAction_Render: AudioUnitRenderActionFlags](audiounitrenderactionflags/offlineunitrenderaction_render.md)
  Once an offline unit has been successfully preflighted, it is then put into its render mode. So this flag is set to indicate to the audio unit that it is now in that state and that it should perform its processing on the input data.
- [static var offlineUnitRenderAction_Complete: AudioUnitRenderActionFlags](audiounitrenderactionflags/offlineunitrenderaction_complete.md)
  This flag is set when an offline unit has completed either its preflight or performed render operation.
- [static var unitRenderAction_PostRenderError: AudioUnitRenderActionFlags](audiounitrenderactionflags/unitrenderaction_postrendererror.md)
  If this flag is set on the post-render call an error was returned by the audio unit’s render operation. In this case, the error can be retrieved through the lastRenderError property and the audio data in `ioData` handed to the post-render notification will be invalid.
- [static var unitRenderAction_DoNotCheckRenderArgs: AudioUnitRenderActionFlags](audiounitrenderactionflags/unitrenderaction_donotcheckrenderargs.md)
  If this flag is set, then checks that are done on the arguments provided to render are not performed. This can be useful to use to save computation time in situations where you are sure you are providing the correct arguments and structures to the various render calls.
### Initializers
- [init(rawValue: UInt32)](audiounitrenderactionflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitrenderactionflags)*