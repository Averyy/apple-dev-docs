# simulateFocusUpdateRequest(from:)

**Framework**: UIKit  
**Kind**: method

Simulates a focus update request from the specified environment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func simulateFocusUpdateRequest(from environment: any UIFocusEnvironment) -> any UIFocusDebuggerOutput
```

#### Return Value

The [`UIFocusDebuggerOutput`](uifocusdebuggeroutput.md) object the focus debugger uses to output the diagnostic information to the debugger console.

#### Discussion

Call this method from the `lldb` debugger using the following command. In the example, `obj` corresponds to an object that adopts the [`UIFocusEnvironment`](uifocusenvironment.md) protocol.

The method simulates a focus update request, outlining each step of the process for determining the next focused item.

## Parameters

- `environment`: The object you want to generate a request for. Specify the focus system, view, view controller, or window whose state you want. You can also specify any other object that adopts the   protocol.

## See Also

- [class func status() -> any UIFocusDebuggerOutput](uifocusdebugger/status.md)
  Returns the state of the focus system, including information about the currently focused item.
- [class func checkFocusability(for: any UIFocusItem) -> any UIFocusDebuggerOutput](uifocusdebugger/checkfocusability(for:).md)
  Returns information about whether the item can become focused, including any known issues that would prevent the item from becoming focused.
- [class func focusGroups(for: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](uifocusdebugger/focusgroups(for:).md)
  Returns the focus group hierarchy for the specified environment object.
- [class func preferredFocusEnvironments(for: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](uifocusdebugger/preferredfocusenvironments(for:).md)
  Returns the hierarchy of preferred focus environments for the specified environment object.
- [protocol UIFocusDebuggerOutput](uifocusdebuggeroutput.md)
  An interface for specifying output from a focus debugger object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusdebugger/simulatefocusupdaterequest(from:))*