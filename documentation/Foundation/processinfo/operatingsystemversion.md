# operatingSystemVersion

**Framework**: Foundation  
**Kind**: property

The version of the operating system on which the process is executing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var operatingSystemVersion: OperatingSystemVersion { get }
```

## See Also

- [var hostName: String](processinfo/hostname.md)
  The name of the host computer on which the process is executing.
- [var operatingSystemVersionString: String](processinfo/operatingsystemversionstring.md)
  A string containing the version of the operating system on which the process is executing.
- [func isOperatingSystemAtLeast(OperatingSystemVersion) -> Bool](processinfo/isoperatingsystematleast(_:).md)
  Returns a Boolean value indicating whether the version of the operating system on which the process is executing is the same or later than the given version.
- [func operatingSystem() -> Int](processinfo/operatingsystem.md)
  Returns a constant to indicate the operating system on which the process is executing.
- [func operatingSystemName() -> String](processinfo/operatingsystemname.md)
  Returns a string containing the name of the operating system on which the process is executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/operatingsystemversion)*