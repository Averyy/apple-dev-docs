# checkFocusability(for:)

**Framework**: UIKit  
**Kind**: method

Returns information about whether the item can become focused, including any known issues that would prevent the item from becoming focused.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func checkFocusability(for item: any UIFocusItem) -> any UIFocusDebuggerOutput
```

#### Return Value

An object the focus debugger uses to store the results that it will format for display.

#### Discussion

Call this method from the `lldb` debugger using the following command. In the example, `item` corresponds to an object that adopts the [`UIFocusItem`](uifocusitem.md) protocol.

The method returns the focus-related information, including known issues.

## Parameters

- `item`: The focus item to evaluate.

## See Also

- [class func status() -> any UIFocusDebuggerOutput](uifocusdebugger/status.md)
  Returns the state of the focus system, including information about the currently focused item.
- [class func focusGroups(for: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](uifocusdebugger/focusgroups(for:).md)
  Returns the focus group hierarchy for the specified environment object.
- [class func preferredFocusEnvironments(for: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](uifocusdebugger/preferredfocusenvironments(for:).md)
  Returns the hierarchy of preferred focus environments for the specified environment object.
- [class func simulateFocusUpdateRequest(from: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](uifocusdebugger/simulatefocusupdaterequest(from:).md)
  Simulates a focus update request from the specified environment.
- [protocol UIFocusDebuggerOutput](uifocusdebuggeroutput.md)
  An interface for specifying output from a focus debugger object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusdebugger/checkfocusability(for:))*