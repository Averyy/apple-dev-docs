# isiOSAppOnVision

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the process is an iPhone or iPad app running on visionOS.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- tvOS 26.1+
- visionOS 26.1+
- watchOS 26.1+

## Declaration

```swift
var isiOSAppOnVision: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) only when the process is an iOS app running on a visionOS device. The value of the property is [`false`](https://developer.apple.com/documentation/Swift/false) for all other apps on visionOS. The property is also [`false`](https://developer.apple.com/documentation/Swift/false) for processes running on platforms other than visonOS.

## See Also

- [var arguments: [String]](processinfo/arguments.md)
  Array of strings with the command-line arguments for the process.
- [var environment: [String : String]](processinfo/environment.md)
  The variable names (keys) and their values in the environment from which the process was launched.
- [var globallyUniqueString: String](processinfo/globallyuniquestring.md)
  Global unique identifier for the process.
- [var isMacCatalystApp: Bool](processinfo/ismaccatalystapp.md)
  A Boolean value that indicates whether the process originated as an iOS app and runs on macOS.
- [var isiOSAppOnMac: Bool](processinfo/isiosapponmac.md)
  A Boolean value that indicates whether the process is an iPhone or iPad app running on a Mac.
- [var processIdentifier: Int32](processinfo/processidentifier.md)
  The identifier of the process (often called process ID).
- [var processName: String](processinfo/processname.md)
  The name of the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/isiosapponvision)*