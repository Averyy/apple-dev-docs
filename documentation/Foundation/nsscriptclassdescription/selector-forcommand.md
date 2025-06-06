# selector(forCommand:)

**Framework**: Foundation  
**Kind**: method

Returns the selector associated with the receiver for the specified command description.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func selector(forCommand commandDescription: NSScriptCommandDescription) -> Selector?
```

#### Return Value

The selector from the receiver for the command specified by `commandDescription`. Searches in the receiver first, then in any superclass. Returns `NULL` if no matching selector is found.

## Parameters

- `commandDescription`: A description for a script command, such as  ,  , or  . Encapsulates the scriptability information for that command, such as its Objective-C selector, its argument names and types, and its return type (if any).

## See Also

- [func supportsCommand(NSScriptCommandDescription) -> Bool](nsscriptclassdescription/supportscommand(_:).md)
  Returns a Boolean value indicating whether the receiver or any superclass supports the specified command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/selector(forcommand:))*