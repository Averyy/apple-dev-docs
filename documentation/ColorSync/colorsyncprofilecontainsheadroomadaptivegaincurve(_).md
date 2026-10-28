# ColorSyncProfileContainsHeadroomAdaptiveGainCurve(_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Returns whether a profile contains a Headroom Adaptive Gain Curve tag.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func ColorSyncProfileContainsHeadroomAdaptiveGainCurve(_ profile: ColorSyncProfile) -> Bool
```

```c
extern bool ColorSyncProfileContainsHeadroomAdaptiveGainCurve(ColorSyncProfileRef profile);
```

## Return Value

`true` if the profile contains an HAGC tag; otherwise, `false`.

## Parameters

- `profile`: The profile to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecontainsheadroomadaptivegaincurve(_:))*