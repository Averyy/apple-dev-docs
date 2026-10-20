# isiOSAppOnVision

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isiOSAppOnVision) BOOL iOSAppOnVision;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) only when the process is an iOS app running on a visionOS device. The value of the property is [`false`](../../Swift/false.md) for all other apps on visionOS. The property is also [`false`](../../Swift/false.md) for processes running on platforms other than visonOS.

## See Also

### Accessing process information
- [var arguments: [String]](./arguments.md)
  Array of strings with the command-line arguments for the process.
- [var environment: [String : String]](./environment.md)
  The variable names (keys) and their values in the environment from which the process was launched.
- [var globallyUniqueString: String](./globallyuniquestring.md)
  Global unique identifier for the process.
- [var isMacCatalystApp: Bool](./ismaccatalystapp.md)
  A Boolean value that indicates whether the process originated as an iOS app and runs on macOS.
- [var isiOSAppOnMac: Bool](./isiosapponmac.md)
  A Boolean value that indicates whether the process is an iPhone or iPad app running on a Mac.
- [var processIdentifier: Int32](./processidentifier.md)
  The identifier of the process (often called process ID).
- [var processName: String](./processname.md)
  The name of the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/isiosapponvision)*