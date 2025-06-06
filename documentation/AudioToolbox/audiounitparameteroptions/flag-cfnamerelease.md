# flag_CFNameRelease

**Framework**: Audio Toolbox  
**Kind**: property

If an audio unit can generate parameter names dynamically, it should set this flag.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var flag_CFNameRelease: AudioUnitParameterOptions { get }
```

#### Discussion

Audio unit hosting applications should check for this flag being set. If it is, the host should release the audio unit parameter name when it is done using it.

If this flag is not set, the host application can assume that the audio unit will release its parameter names.

## See Also

- [static var flag_CanRamp: AudioUnitParameterOptions](audiounitparameteroptions/flag_canramp.md)
- [static var flag_DisplayCubeRoot: AudioUnitParameterOptions](audiounitparameteroptions/flag_displaycuberoot.md)
- [static var flag_DisplayCubed: AudioUnitParameterOptions](audiounitparameteroptions/flag_displaycubed.md)
- [static var flag_DisplayExponential: AudioUnitParameterOptions](audiounitparameteroptions/flag_displayexponential.md)
- [static var flag_DisplayLogarithmic: AudioUnitParameterOptions](audiounitparameteroptions/flag_displaylogarithmic.md)
- [static var flag_DisplayMask: AudioUnitParameterOptions](audiounitparameteroptions/flag_displaymask.md)
- [static var flag_DisplaySquareRoot: AudioUnitParameterOptions](audiounitparameteroptions/flag_displaysquareroot.md)
- [static var flag_DisplaySquared: AudioUnitParameterOptions](audiounitparameteroptions/flag_displaysquared.md)
- [static var flag_ExpertMode: AudioUnitParameterOptions](audiounitparameteroptions/flag_expertmode.md)
- [static var flag_HasCFNameString: AudioUnitParameterOptions](audiounitparameteroptions/flag_hascfnamestring.md)
- [static var flag_HasClump: AudioUnitParameterOptions](audiounitparameteroptions/flag_hasclump.md)
- [static var flag_IsElementMeta: AudioUnitParameterOptions](audiounitparameteroptions/flag_iselementmeta.md)
- [static var flag_IsGlobalMeta: AudioUnitParameterOptions](audiounitparameteroptions/flag_isglobalmeta.md)
- [static var flag_IsHighResolution: AudioUnitParameterOptions](audiounitparameteroptions/flag_ishighresolution.md)
- [static var flag_IsReadable: AudioUnitParameterOptions](audiounitparameteroptions/flag_isreadable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameteroptions/flag_cfnamerelease)*