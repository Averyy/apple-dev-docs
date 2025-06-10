# processName

**Framework**: Foundation  
**Kind**: property

The name of the process.

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
var processName: String { get set }
```

#### Discussion

The process name is used to register application defaults and is used in error messages. It does not uniquely identify the process.

> ⚠️ **Warning**:  User defaults and other aspects of the environment might depend on the process name, so be very careful if you change it. Setting the process name in this manner is not thread safe.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/processname)*