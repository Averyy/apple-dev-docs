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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var hostName: String](processinfo/hostname.md)
  The name of the host computer on which the process is executing.
- [var operatingSystemVersionString: String](processinfo/operatingsystemversionstring.md)
  A string containing the version of the operating system on which the process is executing.
- [var operatingSystemVersion: OperatingSystemVersion](processinfo/operatingsystemversion.md)
  The version of the operating system on which the process is executing.
- [func isOperatingSystemAtLeast(OperatingSystemVersion) -> Bool](processinfo/isoperatingsystematleast(_:).md)
  Returns a Boolean value indicating whether the version of the operating system on which the process is executing is the same or later than the given version.
- [func operatingSystem() -> Int](processinfo/operatingsystem.md)
  Returns a constant to indicate the operating system on which the process is executing.
- [Anonymous](1552984-anonymous.md)
  The following constants are provided by the `NSProcessInfo` class as return values for [`operatingSystem()`](processinfo/operatingsystem().md).
- [func operatingSystemName() -> String](processinfo/operatingsystemname.md)
  Returns a string containing the name of the operating system on which the process is executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operatingsystemversion)*