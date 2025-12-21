# isiOSAppOnMac

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the process is an iPhone or iPad app running on a Mac.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var isiOSAppOnMac: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) only when the process is an iOS app running on a Mac. The value of the property is [`false`](https://developer.apple.com/documentation/Swift/false) for all other apps on the Mac, including Mac apps built using Mac Catalyst. The property is also [`false`](https://developer.apple.com/documentation/Swift/false) for processes running on platforms other than macOS.

## See Also

- [var arguments: [String]](processinfo/arguments.md)
  Array of strings with the command-line arguments for the process.
- [var environment: [String : String]](processinfo/environment.md)
  The variable names (keys) and their values in the environment from which the process was launched.
- [var globallyUniqueString: String](processinfo/globallyuniquestring.md)
  Global unique identifier for the process.
- [var isMacCatalystApp: Bool](processinfo/ismaccatalystapp.md)
  A Boolean value that indicates whether the process originated as an iOS app and runs on macOS.
- [var isiOSAppOnVision: Bool](processinfo/isiosapponvision.md)
  A Boolean value that indicates whether the process is an iPhone or iPad app running on visionOS.
- [var processIdentifier: Int32](processinfo/processidentifier.md)
  The identifier of the process (often called process ID).
- [var processName: String](processinfo/processname.md)
  The name of the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/isiosapponmac)*