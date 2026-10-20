# isiOSAppOnMac

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isiOSAppOnMac) BOOL iOSAppOnMac;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) only when the process is an iOS app running on a Mac. The value of the property is [`false`](../../Swift/false.md) for all other apps on the Mac, including Mac apps built using Mac Catalyst. The property is also [`false`](../../Swift/false.md) for processes running on platforms other than macOS.

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
- [var isiOSAppOnVision: Bool](./isiosapponvision.md)
  A Boolean value that indicates whether the process is an iPhone or iPad app running on visionOS.
- [var processIdentifier: Int32](./processidentifier.md)
  The identifier of the process (often called process ID).
- [var processName: String](./processname.md)
  The name of the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/isiosapponmac)*