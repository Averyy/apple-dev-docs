# isOperatingSystemAtLeast(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the version of the operating system on which the process is executing is the same or later than the given version.

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
func isOperatingSystemAtLeast(_ version: OperatingSystemVersion) -> Bool
```

```objc
- (BOOL) isOperatingSystemAtLeastVersion:(NSOperatingSystemVersion) version;
```

## Return Value

[`true`](../../Swift/true.md) if the operating system on which the process is executing is the same or later than the given version; otherwise [`false`](../../Swift/false.md).

## Discussion

This method accounts for major, minor, and update versions of the operating system.

## Parameters

- `version`: The operating system version to test against.

## See Also

### Getting host information
- [var hostName: String](./hostname.md)
  The name of the host computer on which the process is executing.
- [var operatingSystemVersionString: String](./operatingsystemversionstring.md)
  A string containing the version of the operating system on which the process is executing.
- [var operatingSystemVersion: OperatingSystemVersion](./operatingsystemversion.md)
  The version of the operating system on which the process is executing.
- [struct OperatingSystemVersion](../operatingsystemversion.md)
  A structure that contains version information about the currently executing operating system, including major, minor, and patch version numbers.
- [func operatingSystem() -> Int](./operatingsystem%28%29.md)
  Returns a constant to indicate the operating system on which the process is executing.
- [Anonymous](../api-1552984-anonymous.md)
  The following constants are provided by the `NSProcessInfo` class as return values for [`operatingSystem()`](./operatingsystem%28%29.md).
- [func operatingSystemName() -> String](./operatingsystemname%28%29.md)
  Returns a string containing the name of the operating system on which the process is executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/isoperatingsystematleast(_:))*