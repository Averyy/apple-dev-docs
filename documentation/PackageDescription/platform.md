# Platform

**Framework**: PackageDescription  
**Kind**: struct

A platform supported by Swift Package Manager.

## Declaration

```swift
struct Platform
```

## Topics

### Platforms
- [static let iOS: Platform](platform/ios.md)
  The iOS platform.
- [static let macOS: Platform](platform/macos.md)
  The macOS platform.
- [static let tvOS: Platform](platform/tvos.md)
  The tvOS platform.
- [static let watchOS: Platform](platform/watchos.md)
  The watchOS platform.
- [static let visionOS: Platform](platform/visionos.md)
  The visionOS platform.
- [static let macCatalyst: Platform](platform/maccatalyst.md)
  The Mac Catalyst platform.
- [static let driverKit: Platform](platform/driverkit.md)
  The DriverKit platform
- [static let android: Platform](platform/android.md)
  The Android platform.
- [static let linux: Platform](platform/linux.md)
  The Linux platform.
- [static let freebsd: Platform](platform/freebsd.md)
  The FreeBSD platform.
- [static let openbsd: Platform](platform/openbsd.md)
  The OpenBSD platform.
- [static let wasi: Platform](platform/wasi.md)
  The WebAssembly System Interface platform.
- [static let windows: Platform](platform/windows.md)
  The Windows platform.
### Type methods
- [static func custom(String) -> Platform](platform/custom(_:).md)
  Creates a custom platform.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var platforms: [SupportedPlatform]?](package/platforms.md)
  The list of minimum versions for platforms supported by the package.
- [struct SupportedPlatform](supportedplatform.md)
  A platform that the Swift package supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/platform)*