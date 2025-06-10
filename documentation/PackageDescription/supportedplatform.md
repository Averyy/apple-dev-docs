# SupportedPlatform

**Framework**: PackageDescription  
**Kind**: struct

A platform that the Swift package supports.

## Declaration

```swift
struct SupportedPlatform
```

#### Overview

By default, Swift Package Manager assigns a predefined minimum deployment version for each supported platforms unless you configure supported platforms using the `platforms` API. This predefined deployment version is the oldest deployment target version that the installed SDK supports for a given platform. One exception to this rule is macOS, for which the minimum deployment target version starts from 10.10. Packages can choose to configure the minimum deployment target version for a platform by using the APIs defined in this struct. Swift Package Manager emits appropriate errors when an invalid value is provided for supported platforms, such as an empty array, multiple declarations for the same platform, or an invalid version specification.

Swift Package Manager emits an error if a dependency isn’t compatible with the top-level package’s deployment version. The deployment target of a package’s dependencies must be lower than or equal to the top-level package’s deployment target version for a particular platform.

## Topics

### Supporting iOS
- [static func iOS(SupportedPlatform.IOSVersion) -> SupportedPlatform](supportedplatform/ios(_:)-5pvv5.md)
  Configures the minimum deployment target version for the iOS platform.
- [static func iOS(String) -> SupportedPlatform](supportedplatform/ios(_:)-83bbf.md)
  Configures the minimum deployment target version for the iOS platform using a custom version string.
- [static let iOS: Platform](platform/ios.md)
  The iOS platform.
- [SupportedPlatform.IOSVersion](supportedplatform/iosversion.md)
  The supported iOS version.
### Supporting macOS
- [static func macOS(SupportedPlatform.MacOSVersion) -> SupportedPlatform](supportedplatform/macos(_:)-2wthp.md)
  Configures the minimum deployment target version for the macOS platform.
- [static func macOS(String) -> SupportedPlatform](supportedplatform/macos(_:)-9771f.md)
  Configures the minimum deployment target version for the macOS platform using a version string.
- [static let macOS: Platform](platform/macos.md)
  The macOS platform.
- [SupportedPlatform.MacOSVersion](supportedplatform/macosversion.md)
  The supported macOS version.
### Supporting watchOS
- [static func watchOS(SupportedPlatform.WatchOSVersion) -> SupportedPlatform](supportedplatform/watchos(_:)-t998.md)
  Configure the minimum deployment target version for the watchOS platform.
- [static func watchOS(String) -> SupportedPlatform](supportedplatform/watchos(_:)-4lrx0.md)
  Configure the minimum deployment target version for the watchOS platform using a custom version string.
- [static let watchOS: Platform](platform/watchos.md)
  The watchOS platform.
- [SupportedPlatform.WatchOSVersion](supportedplatform/watchosversion.md)
  The supported watchOS version.
### Supporting visionOS
- [static func visionOS(SupportedPlatform.VisionOSVersion) -> SupportedPlatform](supportedplatform/visionos(_:)-3ip0z.md)
  Configure the minimum deployment target version for the visionOS platform.
- [static func visionOS(String) -> SupportedPlatform](supportedplatform/visionos(_:)-6ur2u.md)
  Configure the minimum deployment target version for the visionOS platform using a custom version string.
- [static let visionOS: Platform](platform/visionos.md)
  The visionOS platform.
- [SupportedPlatform.VisionOSVersion](supportedplatform/visionosversion.md)
  The supported visionOS version.
### Supporting tvOS
- [static func tvOS(SupportedPlatform.TVOSVersion) -> SupportedPlatform](supportedplatform/tvos(_:)-6931l.md)
  Configures the minimum deployment target version for the tvOS platform.
- [static func tvOS(String) -> SupportedPlatform](supportedplatform/tvos(_:)-3k8sy.md)
  Configures the minimum deployment target version for the tvOS platform using a custom version string.
- [static let tvOS: Platform](platform/tvos.md)
  The tvOS platform.
- [SupportedPlatform.TVOSVersion](supportedplatform/tvosversion.md)
  The supported tvOS version.
### Supporting MacCatalyst
- [static func macCatalyst(SupportedPlatform.MacCatalystVersion) -> SupportedPlatform](supportedplatform/maccatalyst(_:)-6bh40.md)
  Configures the minimum deployment target version for the Mac Catalyst platform.
- [static func macCatalyst(String) -> SupportedPlatform](supportedplatform/maccatalyst(_:)-9wbz.md)
  Configures the minimum deployment target version for the Mac Catalyst platform using a version string.
- [static let macCatalyst: Platform](platform/maccatalyst.md)
  The Mac Catalyst platform.
- [SupportedPlatform.MacCatalystVersion](supportedplatform/maccatalystversion.md)
  The supported Mac Catalyst version.
### Supporting DriverKit
- [static func driverKit(SupportedPlatform.DriverKitVersion) -> SupportedPlatform](supportedplatform/driverkit(_:)-jxlz.md)
  Configures the minimum deployment target version for the DriverKit platform.
- [static func driverKit(String) -> SupportedPlatform](supportedplatform/driverkit(_:)-6evdd.md)
  Configures the minimum deployment target version for the DriverKit platform using a custom version string.
- [static let driverKit: Platform](platform/driverkit.md)
  The DriverKit platform
- [SupportedPlatform.DriverKitVersion](supportedplatform/driverkitversion.md)
  The supported DriverKit version.
### Supporting Custom Platforms
- [static func custom(String, versionString: String) -> SupportedPlatform](supportedplatform/custom(_:versionstring:).md)
  Configures the minimum deployment target version for custom platforms.
### Operator Functions
- [static func != (Self, Self) -> Bool](supportedplatform/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Structures
- [SupportedPlatform.CustomPlatformVersion](supportedplatform/customplatformversion.md)
  A supported custom platform version.
### Operators
- [static func == (SupportedPlatform, SupportedPlatform) -> Bool](supportedplatform/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](supportedplatform/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var platforms: [SupportedPlatform]?](package/platforms.md)
  The list of minimum versions for platforms supported by the package.
- [struct Platform](platform.md)
  A platform supported by Swift Package Manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform)*