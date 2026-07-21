# applicationVersion

**Framework**: ColorSync  
**Kind**: property

The application version of the metadata, as defined by ST 2094-50.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var applicationVersion: UInt8
```

#### Discussion

This 3-bit field is currently always `0`. Initializing the metadata with any other value throws [`ColorSyncProfile.HeadroomAdaptiveGainCurve.Error.unsupportedApplicationVersion(_:)`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error/unsupportedapplicationversion(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofile/headroomadaptivegaincurve-swift.struct/applicationversion)*