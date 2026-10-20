# operatingSystemName()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a string containing the name of the operating system on which the process is executing.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`operatingSystemVersionString`](./operatingsystemversionstring.md) instead.

## Declaration

```swift
func operatingSystemName() -> String
```

```objc
- (NSString *) operatingSystemName;
```

#### Return Value

Operating system name. In macOS, it’s `@"NSMACHOperatingSystem"`

## See Also

### Getting host information
- [var hostName: String](./hostname.md)
  The name of the host computer on which the process is executing.
- [var operatingSystemVersionString: String](./operatingsystemversionstring.md)
  A string containing the version of the operating system on which the process is executing.
- [var operatingSystemVersion: OperatingSystemVersion](./operatingsystemversion.md)
  The version of the operating system on which the process is executing.
- [func isOperatingSystemAtLeast(OperatingSystemVersion) -> Bool](./isoperatingsystematleast%28_%29.md)
  Returns a Boolean value indicating whether the version of the operating system on which the process is executing is the same or later than the given version.
- [struct OperatingSystemVersion](../operatingsystemversion.md)
  A structure that contains version information about the currently executing operating system, including major, minor, and patch version numbers.
- [func operatingSystem() -> Int](./operatingsystem%28%29.md)
  Returns a constant to indicate the operating system on which the process is executing.
- [Anonymous](../api-1552984-anonymous.md)
  The following constants are provided by the `NSProcessInfo` class as return values for [`operatingSystem()`](./operatingsystem%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/operatingsystemname())*