# UIFocusDebugger

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A runtime object for debugging focus-related interactions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIFocusDebugger
```

```objc
@interface UIFocusDebugger : NSObject
```

## Mentions

- [Debugging focus issues in your app](./debugging-focus-issues-in-your-app.md)

## Overview

You do not use this class or its methods directly from your code. During a debugging session, you can call the methods of this class from the `lldb` debugger command line to obtain information about the current state of the focus system.

## Topics

### Getting help
- [class func help() -> any UIFocusDebuggerOutput](./uifocusdebugger/help%28%29.md)
  Returns information about how to use the commands of the debugger object.
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
- [protocol UIFocusDebuggerOutput](./uifocusdebuggeroutput.md)
  An interface for specifying output from a focus debugger object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Focus debugging
- [Debugging focus issues in your app](./debugging-focus-issues-in-your-app.md)
  Find errors and determine why the next focused item isn’t what you expected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusdebugger)*