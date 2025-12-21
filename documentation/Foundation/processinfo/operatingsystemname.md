# operatingSystemName()

**Framework**: Foundation  
**Kind**: method

Returns a string containing the name of the operating system on which the process is executing.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func operatingSystemName() -> String
```

#### Return Value

Operating system name. In macOS, it’s `@"NSMACHOperatingSystem"`

## See Also

- [var hostName: String](processinfo/hostname.md)
  The name of the host computer on which the process is executing.
- [var operatingSystemVersionString: String](processinfo/operatingsystemversionstring.md)
  A string containing the version of the operating system on which the process is executing.
- [var operatingSystemVersion: OperatingSystemVersion](processinfo/operatingsystemversion.md)
  The version of the operating system on which the process is executing.
- [func isOperatingSystemAtLeast(OperatingSystemVersion) -> Bool](processinfo/isoperatingsystematleast(_:).md)
  Returns a Boolean value indicating whether the version of the operating system on which the process is executing is the same or later than the given version.
- [struct OperatingSystemVersion](operatingsystemversion.md)
  A structure that contains version information about the currently executing operating system, including major, minor, and patch version numbers.
- [func operatingSystem() -> Int](processinfo/operatingsystem.md)
  Returns a constant to indicate the operating system on which the process is executing.
- [Anonymous](1552984-anonymous.md)
  The following constants are provided by the `NSProcessInfo` class as return values for [`operatingSystem()`](processinfo/operatingsystem().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/operatingsystemname())*