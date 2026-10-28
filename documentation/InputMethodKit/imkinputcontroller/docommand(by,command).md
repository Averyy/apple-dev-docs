# doCommand(by:command:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Passes commands that are not generated as part of the text input process.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func doCommand(by aSelector: Selector!, command infoDictionary: [AnyHashable : Any]!)
```

```objc
- (void) doCommandBySelector:(SEL) aSelector commandDictionary:(NSDictionary *) infoDictionary;
```

## Discussion

The default implementation checks if the input controller object (that is, self) responds to the selector. If so, it sends the message [`perform(_:with:)`](../../ObjectiveC/nsobjectprotocol/perform%28_,with%29.md) to the input controller class. The object parameter in that case is the `infoDictionary` parameter.

This method is called when a user selects a command from the text input menu. To support this, an input method must provide actions for each menu item that is placed in the menu. For example, `(void)menuAction:(id)sender`. Note that the sender in this instance is the info dictionary.

## Parameters

- `aSelector`: A selector that represents a command from the text input menu.
- `infoDictionary`: A dictionary that contains two key-value pairs:

  - [`kIMKCommandMenuItemName`](../kimkcommandmenuitemname.md), whose value is an `NSMenuItem` object. That is, the item selected by the user.
  - [`kIMKCommandClientName`](../kimkcommandclientname.md), whose value is the current client—`id<IMKTextInput, NSObject>`.

## See Also

### Working with Custom Commands
- [func menu() -> NSMenu!](./menu%28%29.md)
  Returns a menu of commands that are specific to an input method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/docommand(by:command:))*