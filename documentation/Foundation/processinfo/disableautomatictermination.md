# disableAutomaticTermination(_:)

**Framework**: Foundation  
**Kind**: method

Disables automatic termination for the application.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func disableAutomaticTermination(_ reason: String)
```

#### Discussion

This method increments the automatic termination counter. When the counter is greater than `0`, the application is considered active and ineligible for automatic termination. For example, you could disable automatic termination when the user of an instant messaging application signs on, because the application requires a background connection to be maintained even if the application is otherwise inactive.

The reason parameter is used to track why an application is or is not automatically terminable and can be inspected by debugging tools. For example, you could pass the string `@"file transfer in progress"` if you disable automatic termination before transferring a file over the network. When you reenable automatic termination after the transfer is complete using [`enableAutomaticTermination(_:)`](processinfo/enableautomatictermination(_:).md), you should pass the matching string. A given reason can be used more than once at the same time; for example, if two files were being transferred at the same time, automatic termination could be disabled for each, passing the same reason string.

## Parameters

- `reason`: The reason why automatic termination is being disabled.

## See Also

- [func enableAutomaticTermination(String)](processinfo/enableautomatictermination(_:).md)
  Enables automatic termination for the application.
- [var automaticTerminationSupportEnabled: Bool](processinfo/automaticterminationsupportenabled.md)
  A Boolean value indicating whether the app supports automatic termination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/disableautomatictermination(_:))*