# authorizationStatus

**Framework**: SwiftUI  
**Kind**: property

A value that represents whether the user has authorized providing more detailed information about the surface scenes are snapped to. To request this detailed surface information, in your `Info.plist` file, set `UIWantsDetailedSurfaceInfo` to `YES` and set `NSWorldSensingUsageDescription` to provide a description of why your app is requesting this information.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var authorizationStatus: SurfaceSnappingInfo.AuthorizationStatus { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/surfacesnappinginfo/authorizationstatus-swift.type.property)*