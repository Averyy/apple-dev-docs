# globallyUniqueString

**Framework**: Foundation  
**Kind**: property

Global unique identifier for the process.

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
var globallyUniqueString: String { get }
```

#### Discussion

The global ID for the process includes the host name, process ID, and a time stamp, which ensures that the ID is unique for the network. This property generates a new string each time its getter is invoked, and it uses a counter to guarantee that strings created from the same process are unique.

## See Also

- [var arguments: [String]](processinfo/arguments.md)
  Array of strings with the command-line arguments for the process.
- [var environment: [String : String]](processinfo/environment.md)
  The variable names (keys) and their values in the environment from which the process was launched.
- [var isMacCatalystApp: Bool](processinfo/ismaccatalystapp.md)
  A Boolean value that indicates whether the process originated as an iOS app and runs on macOS.
- [var isiOSAppOnMac: Bool](processinfo/isiosapponmac.md)
  A Boolean value that indicates whether the process is an iPhone or iPad app running on a Mac.
- [var processIdentifier: Int32](processinfo/processidentifier.md)
  The identifier of the process (often called process ID).
- [var processName: String](processinfo/processname.md)
  The name of the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/globallyuniquestring)*