# status()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns the state of the focus system, including information about the currently focused item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func status() -> any UIFocusDebuggerOutput
```

```objc
+ (id<UIFocusDebuggerOutput>) status;
```

## Return Value

An object the focus debugger uses to output information to the debugger console.

## Discussion

Call this method from the `lldb` debugger using the following command:

**Swift**:

```swift
po UIFocusDebugger.status()
```

**Objective-C**:

```objc
po [UIFocusDebugger status]
```

The method returns information about the focus system and the currently focused item.

## See Also

### Getting focus information
- [class func checkFocusability(for: any UIFocusItem) -> any UIFocusDebuggerOutput](./checkfocusability%28for%29.md)
  Returns information about whether the item can become focused, including any known issues that would prevent the item from becoming focused.
- [class func focusGroups(for: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](./focusgroups%28for%29.md)
  Returns the focus group hierarchy for the specified environment object.
- [class func preferredFocusEnvironments(for: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](./preferredfocusenvironments%28for%29.md)
  Returns the hierarchy of preferred focus environments for the specified environment object.
- [class func simulateFocusUpdateRequest(from: any UIFocusEnvironment) -> any UIFocusDebuggerOutput](./simulatefocusupdaterequest%28from%29.md)
  Simulates a focus update request from the specified environment.
- [protocol UIFocusDebuggerOutput](../uifocusdebuggeroutput.md)
  An interface for specifying output from a focus debugger object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusdebugger/status())*