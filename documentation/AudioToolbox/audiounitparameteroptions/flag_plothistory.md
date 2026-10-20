# flag_PlotHistory

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Type Property

If set, getting the `kAudioUnitProperty_ParameterHistoryInfo` property fills out the [`AudioUnitParameterHistoryInfo`](../audiounitparameterhistoryinfo.md) struct containing the recommended update rate and history duration.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
static var flag_PlotHistory: AudioUnitParameterOptions { get }
```

```c
kAudioUnitParameterFlag_PlotHistory
```

## See Also

### Constants
- [static var flag_CFNameRelease: AudioUnitParameterOptions](./flag_cfnamerelease.md)
  If an audio unit can generate parameter names dynamically, it should set this flag.
- [static var flag_CanRamp: AudioUnitParameterOptions](./flag_canramp.md)
- [static var flag_DisplayCubeRoot: AudioUnitParameterOptions](./flag_displaycuberoot.md)
- [static var flag_DisplayCubed: AudioUnitParameterOptions](./flag_displaycubed.md)
- [static var flag_DisplayExponential: AudioUnitParameterOptions](./flag_displayexponential.md)
- [static var flag_DisplayLogarithmic: AudioUnitParameterOptions](./flag_displaylogarithmic.md)
- [static var flag_DisplayMask: AudioUnitParameterOptions](./flag_displaymask.md)
- [static var flag_DisplaySquareRoot: AudioUnitParameterOptions](./flag_displaysquareroot.md)
- [static var flag_DisplaySquared: AudioUnitParameterOptions](./flag_displaysquared.md)
- [static var flag_ExpertMode: AudioUnitParameterOptions](./flag_expertmode.md)
- [static var flag_HasCFNameString: AudioUnitParameterOptions](./flag_hascfnamestring.md)
- [static var flag_HasClump: AudioUnitParameterOptions](./flag_hasclump.md)
- [static var flag_IsElementMeta: AudioUnitParameterOptions](./flag_iselementmeta.md)
- [static var flag_IsGlobalMeta: AudioUnitParameterOptions](./flag_isglobalmeta.md)
- [static var flag_IsHighResolution: AudioUnitParameterOptions](./flag_ishighresolution.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/flag_plothistory)*