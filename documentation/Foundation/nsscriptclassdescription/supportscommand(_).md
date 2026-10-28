# supportsCommand(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the receiver or any superclass supports the specified command.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func supportsCommand(_ commandDescription: NSScriptCommandDescription) -> Bool
```

```objc
- (BOOL) supportsCommand:(NSScriptCommandDescription *) commandDescription;
```

## Return Value

[`true`](../../Swift/true.md) if an the receiver or the instance of `NSScriptClassDescription` of any superclass of the receiver’s class lists the command described by `commandDesc` among its supported commands; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `commandDescription`: A description for a script command, such as `duplicate`, `make`, or `move`. Encapsulates the scriptability information for that command, such as its Objective-C selector, its argument names and types, and its return type (if any).

## See Also

### Getting command information
- [func selector(forCommand: NSScriptCommandDescription) -> Selector?](./selector%28forcommand%29.md)
  Returns the selector associated with the receiver for the specified command description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/supportscommand(_:))*