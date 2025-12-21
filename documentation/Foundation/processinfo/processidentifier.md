# processIdentifier

**Framework**: Foundation  
**Kind**: property

The identifier of the process (often called process ID).

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
var processIdentifier: Int32 { get }
```

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
- [var isiOSAppOnVision: Bool](processinfo/isiosapponvision.md)
  A Boolean value that indicates whether the process is an iPhone or iPad app running on visionOS.
- [var processName: String](processinfo/processname.md)
  The name of the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/processidentifier)*