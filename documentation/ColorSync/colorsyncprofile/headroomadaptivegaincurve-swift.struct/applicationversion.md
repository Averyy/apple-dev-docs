# applicationVersion

**Framework**: ColorSync  
**Kind**: property  
**Role**: Instance Property

The application version of the metadata, as defined by ST 2094-50.

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
var applicationVersion: UInt8
```

#### Discussion

This 3-bit field is currently always `0`. Initializing the metadata with any other value throws [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.unsupportedApplicationVersion(_:)`](./error/unsupportedapplicationversion%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/applicationversion)*