# focusGroups(for:)

**Framework**: Uikit  
**Kind**: method

Returns the focus group hierarchy for the specified environment object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func focusGroups(for environment: any UIFocusEnvironment) -> any UIFocusDebuggerOutput
```

#### Return Value

An object the focus debugger uses to store the results that it formats for display.

#### Discussion

Call this method from the `lldb` debugger using the following command. In the example, `obj` corresponds to an object that adopts the [`UIFocusEnvironment`](uifocusenvironment.md) protocol.

The method returns the full hierarchy of focus groups for the focus environment object provided.

> **Note**:  This method replaces the `checkFocusGroup(for:)` method, which is functionally equivalent.

## Parameters

- `environment`: The object you want to generate a focus group hierarchy for. Specify the focus system, view, view controller, or window whose state you want. You can also specify any other object that adopts the   protocol.

## See Also

- [class func status() -> any UIFocusDebuggerOutput](uifocusdebugger/status.md)
  Returns the state of the focus system, including information about the currently focused item.
- [class func checkFocusability(for: any UIFocusItem) -> any UIFocusDebuggerOutput](uifocusdebugger/checkfocusability(for:).md)
  Returns information about whether the item can become focused, including any known issues that would prevent the item from becoming focused.
- [class func preferredFocusEnvironments(for: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](uifocusdebugger/preferredfocusenvironments(for:).md)
  Returns the hierarchy of preferred focus environments for the specified environment object.
- [class func simulateFocusUpdateRequest(from: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](uifocusdebugger/simulatefocusupdaterequest(from:).md)
  Simulates a focus update request from the specified environment.
- [protocol UIFocusDebuggerOutput](uifocusdebuggeroutput.md)
  An interface for specifying output from a focus debugger object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusdebugger/focusgroups(for:))*