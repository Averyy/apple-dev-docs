# parametersForOverview(withCount:)

**Framework**: Audio Toolbox  
**Kind**: method

Returns the audio unit’s most important parameters.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func parametersForOverview(withCount count: Int) -> [NSNumber]
```

#### Return Value

An array of addresses representing the audio unit’s most important parameters.

#### Discussion

This method allows a host to query an audio unit for a small number of its most important parameters, to be displayed in a compact generic view.

This version 3 method is partially bridged to the version 2 `kAudioUnitProperty_ParametersForOverview` API.

## Parameters

- `count`: The number of parameters to return.

## See Also

- [var parameterTree: AUParameterTree?](auaudiounit/parametertree.md)
  An audio unit’s parameters, organized in a tree hierarchy.
- [var allParameterValues: Bool](auaudiounit/allparametervalues.md)
  Special read-only property for KVO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/parametersforoverview(withcount:))*