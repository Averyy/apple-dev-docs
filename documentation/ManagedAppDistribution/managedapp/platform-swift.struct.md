# ManagedApp.Platform

**Framework**: ManagedAppDistribution  
**Kind**: struct  
**Role**: Structure

The supported platform for the app.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 2.4+

## Declaration

```swift
struct Platform
```

## Topics

### Type Properties
- [static var iOS: ManagedApp.Platform](./platform-swift.struct/ios.md)
  iOS is a supported platform.
- [static var macOS: ManagedApp.Platform](./platform-swift.struct/macos.md)
  macOS is a supported platform.
- [static var visionOS: ManagedApp.Platform](./platform-swift.struct/visionos.md)
  visionOS is a supported platform.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Obtaining platform and requirement information
- [let platform: Platform](./platform-swift.property.md)
  The platform of the app.
- [let requirements: String?](./requirements.md)
  The app’s localized operating system compatibility requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapp/platform-swift.struct)*