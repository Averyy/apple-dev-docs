# operatingSystemVersionString

**Framework**: Foundation  
**Kind**: property

A string containing the version of the operating system on which the process is executing.

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
var operatingSystemVersionString: String { get }
```

#### Discussion

The operating system version string is human readable, localized, and is appropriate for displaying to the user. This string is  appropriate for parsing.

## See Also

- [var hostName: String](processinfo/hostname.md)
  The name of the host computer on which the process is executing.
- [var operatingSystemVersion: OperatingSystemVersion](processinfo/operatingsystemversion.md)
  The version of the operating system on which the process is executing.
- [func isOperatingSystemAtLeast(OperatingSystemVersion) -> Bool](processinfo/isoperatingsystematleast(_:).md)
  Returns a Boolean value indicating whether the version of the operating system on which the process is executing is the same or later than the given version.
- [func operatingSystem() -> Int](processinfo/operatingsystem.md)
  Returns a constant to indicate the operating system on which the process is executing.
- [func operatingSystemName() -> String](processinfo/operatingsystemname.md)
  Returns a string containing the name of the operating system on which the process is executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/operatingsystemversionstring)*