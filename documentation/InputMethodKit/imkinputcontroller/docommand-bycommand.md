# doCommand(by:command:)

**Framework**: InputMethodKit  
**Kind**: method

Passes commands that are not generated as part of the text input process.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func doCommand(by aSelector: Selector!, command infoDictionary: [AnyHashable : Any]!)
```

#### Discussion

The default implementation checks if the input controller object (that is, self) responds to the selector. If so, it sends the message [`perform(_:with:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/perform(_:with:)) to the input controller class. The object parameter in that case is the `infoDictionary` parameter.

This method is called when a user selects a command from the text input menu. To support this, an input method must provide actions for each menu item that is placed in the menu. For example, `(void)menuAction:(id)sender`. Note that the sender in this instance is the info dictionary.

## Parameters

- `aSelector`: A selector that represents a command from the text input menu.
- `infoDictionary`: A dictionary that contains two key-value pairs:

## See Also

- [func menu() -> NSMenu!](imkinputcontroller/menu.md)
  Returns a menu of commands that are specific to an input method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/docommand(by:command:))*