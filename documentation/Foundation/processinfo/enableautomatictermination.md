# enableAutomaticTermination(_:)

**Framework**: Foundation  
**Kind**: method

Enables automatic termination for the application.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func enableAutomaticTermination(_ reason: String)
```

#### Discussion

This method decrements the automatic termination counter. When the counter is `0`, the application is eligible for automatic termination.

The reason parameter is used to track why an application is or is not automatically terminable and can be inspected by debugging tools. For example, you could pass the string `@"file transfer in progress"` if you disable automatic termination before transferring a file over the network. When you reenable automatic termination after the transfer is complete using [`enableAutomaticTermination(_:)`](processinfo/enableautomatictermination(_:).md), you should pass the matching string. A given reason can be used more than once at the same time; for example, if two files were being transferred at the same time, automatic termination could be disabled for each, passing the same reason string.

## Parameters

- `reason`: The reason why automatic termination is being enabled.

## See Also

- [func disableAutomaticTermination(String)](processinfo/disableautomatictermination(_:).md)
  Disables automatic termination for the application.
- [var automaticTerminationSupportEnabled: Bool](processinfo/automaticterminationsupportenabled.md)
  A Boolean value indicating whether the app supports automatic termination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/enableautomatictermination(_:))*