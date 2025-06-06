# OperatingSystemVersion

**Framework**: Foundation  
**Kind**: struct

A structure that contains version information about the currently executing operating system, including major, minor, and patch version numbers.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct OperatingSystemVersion
```

#### Overview

Use the [`ProcessInfo`](processinfo.md) property [`operatingSystemVersion`](processinfo/operatingsystemversion.md) to fetch an instance of this type. You can also pass this type to [`isOperatingSystemAtLeast(_:)`](processinfo/isoperatingsystematleast(_:).md) to determine whether the current operating system version is the same or later than the given value.

## Topics

### Creating an Operating System Version
- [init()](operatingsystemversion/init.md)
  Creates an empty operating system version.
- [init(majorVersion: Int, minorVersion: Int, patchVersion: Int)](operatingsystemversion/init(majorversion:minorversion:patchversion:).md)
  Creates an operating system version with the provided values.
### Version Components
- [var majorVersion: Int](operatingsystemversion/majorversion.md)
  The major release number, such as 10 in version 10.9.3.
- [var minorVersion: Int](operatingsystemversion/minorversion.md)
  The minor release number, such as 9 in version 10.9.3.
- [var patchVersion: Int](operatingsystemversion/patchversion.md)
  The update release number, such as 3 in version 10.9.3.
- [var majorVersion: Int](operatingsystemversion/majorversion.md)
  The major release number, such as 10 in version 10.9.3.
- [var minorVersion: Int](operatingsystemversion/minorversion.md)
  The minor release number, such as 9 in version 10.9.3.
- [var patchVersion: Int](operatingsystemversion/patchversion.md)
  The update release number, such as 3 in version 10.9.3.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [ProcessInfo.ActivityOptions](processinfo/activityoptions.md)
  Option flags used with [`beginActivity(options:reason:)`](processinfo/beginactivity(options:reason:).md) and [`performActivity(options:reason:using:)`](processinfo/performactivity(options:reason:using:).md).
- [ProcessInfo.ThermalState](processinfo/thermalstate-swift.enum.md)
  Values used to indicate the system’s thermal state.
- [Anonymous](1552984-anonymous.md)
  The following constants are provided by the `NSProcessInfo` class as return values for [`operatingSystem()`](processinfo/operatingsystem().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operatingsystemversion)*