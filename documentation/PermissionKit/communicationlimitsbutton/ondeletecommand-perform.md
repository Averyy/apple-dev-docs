# onDeleteCommand(perform:)

**Framework**: PermissionKit  
**Kind**: method

Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func onDeleteCommand(perform action: (() -> Void)?) -> some View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/ondeletecommand(perform:))*