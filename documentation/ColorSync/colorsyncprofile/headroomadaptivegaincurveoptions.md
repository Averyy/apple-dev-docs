# ColorSyncProfile.HeadroomAdaptiveGainCurveOptions

**Framework**: ColorSync  
**Kind**: struct  
**Role**: Structure

Options that configure how a Headroom Adaptive Gain Curve is read from or embedded in a profile.

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
struct HeadroomAdaptiveGainCurveOptions
```

## Overview

This type is reserved for future use and currently carries no options.

## Topics

### Initializers
- [init()](./headroomadaptivegaincurveoptions/init%28%29.md)
  Creates an empty set of options.

## See Also

### Attaching a curve in Swift
- [func adding(headroomAdaptiveGainCurve: ColorSyncProfile.HeadroomAdaptiveGainCurve) -> ColorSyncProfile?](./adding%28headroomadaptivegaincurve%29.md)
  Returns a copy of this profile with raw Headroom Adaptive Gain Curve data embedded as an HAGC tag.
- [func adding(headroomAdaptiveGainCurveMetadata: Data, options: ColorSyncProfile.HeadroomAdaptiveGainCurveOptions) -> ColorSyncProfile?](./adding%28headroomadaptivegaincurvemetadata,options%29.md)
  Returns a copy of this profile with raw Headroom Adaptive Gain Curve data embedded as an HAGC tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurveoptions)*