# SurfaceSnappingInfo.AuthorizationStatus

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

A type representing whether the user has granted permissions to provide more detailed information about the surface a scene is snapped to.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum AuthorizationStatus
```

## Overview

To provide `ARKit/SurfaceClassification` data, the user must allow the app to access information about their surroundings. To request this data, set `UIWantsDetailedSurfaceInfo` to `YES` and set `NSWorldSensingUsageDescription` to provide a description of why your app is requesting this information. These values are set in your app’s `Info.plist` file.

## Topics

### Enumeration Cases
- [SurfaceSnappingInfo.AuthorizationStatus.authorized](./authorizationstatus-swift.enum/authorized.md)
  The user has authorized sharing information about their surroundings.
- [SurfaceSnappingInfo.AuthorizationStatus.denied](./authorizationstatus-swift.enum/denied.md)
  The user denied providing access to information about their surroundings.
- [SurfaceSnappingInfo.AuthorizationStatus.notDetermined](./authorizationstatus-swift.enum/notdetermined.md)
  The user has not yet authorized or denied providing information about their surroundings. Set `UIWantsDetailedSurfaceInfo` to `YES` in your `Info.plist` to request information about the user’s surroundings when they first snap a scene from your app.
- [SurfaceSnappingInfo.AuthorizationStatus.restricted](./authorizationstatus-swift.enum/restricted.md)
  The user is unable to grant authorization to share detailed information about their surroundings.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/surfacesnappinginfo/authorizationstatus-swift.enum)*