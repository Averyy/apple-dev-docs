# supportsCommand(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether the receiver or any superclass supports the specified command.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func supportsCommand(_ commandDescription: NSScriptCommandDescription) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if an the receiver or the instance of `NSScriptClassDescription` of any superclass of the receiver’s class lists the command described by `commandDesc` among its supported commands; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `commandDescription`: A description for a script command, such as  ,  , or  . Encapsulates the scriptability information for that command, such as its Objective-C selector, its argument names and types, and its return type (if any).

## See Also

- [func selector(forCommand: NSScriptCommandDescription) -> Selector?](nsscriptclassdescription/selector(forcommand:).md)
  Returns the selector associated with the receiver for the specified command description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/supportscommand(_:))*