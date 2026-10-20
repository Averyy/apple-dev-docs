# UIFocusDebuggerOutput

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

An interface for specifying output from a focus debugger object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIFocusDebuggerOutput : NSObjectProtocol
```

```objc
@protocol UIFocusDebuggerOutput <NSObject>
```

#### Overview

Don’t use this protocol directly in your code. When debugging your app from the `lldb` command line, the methods of [`UIFocusDebugger`](./uifocusdebugger.md) output their results to an object that adopts this protocol. The debugger takes the output and formats it for display.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Getting focus information
- [class func status() -> any UIFocusDebuggerOutput](./uifocusdebugger/status%28%29.md)
  Returns the state of the focus system, including information about the currently focused item.
- [class func checkFocusability(for: any UIFocusItem) -> any UIFocusDebuggerOutput](./uifocusdebugger/checkfocusability%28for%29.md)
  Returns information about whether the item can become focused, including any known issues that would prevent the item from becoming focused.
- [class func focusGroups(for: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](./uifocusdebugger/focusgroups%28for%29.md)
  Returns the focus group hierarchy for the specified environment object.
- [class func preferredFocusEnvironments(for: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](./uifocusdebugger/preferredfocusenvironments%28for%29.md)
  Returns the hierarchy of preferred focus environments for the specified environment object.
- [class func simulateFocusUpdateRequest(from: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](./uifocusdebugger/simulatefocusupdaterequest%28from%29.md)
  Simulates a focus update request from the specified environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusdebuggeroutput)*