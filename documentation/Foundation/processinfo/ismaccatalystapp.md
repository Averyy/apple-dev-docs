# isMacCatalystApp

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the process originated as an iOS app and runs on macOS.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isMacCatalystApp: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the process is:

- A Mac app built with Mac Catalyst, or an iOS app running on Apple silicon.
- Running on a Mac.

Frameworks that support iOS and macOS use this property to determine if the process is a Mac app built with Mac Catalyst. To conditionally compile source code intended to run only in macOS, use `#if targetEnvironment(macCatalyst)` (or `#if TARGET_OS_MACCATALYST` in Objective-C) instead.

> **Note**:  To distinguish between an iOS app running on Apple silicon and a Mac app built with Mac Catalyst, use the [`isiOSAppOnMac`](processinfo/isiosapponmac.md) property.

## See Also

- [var arguments: [String]](processinfo/arguments.md)
  Array of strings with the command-line arguments for the process.
- [var environment: [String : String]](processinfo/environment.md)
  The variable names (keys) and their values in the environment from which the process was launched.
- [var globallyUniqueString: String](processinfo/globallyuniquestring.md)
  Global unique identifier for the process.
- [var isiOSAppOnMac: Bool](processinfo/isiosapponmac.md)
  A Boolean value that indicates whether the process is an iPhone or iPad app running on a Mac.
- [var processIdentifier: Int32](processinfo/processidentifier.md)
  The identifier of the process (often called process ID).
- [var processName: String](processinfo/processname.md)
  The name of the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/ismaccatalystapp)*