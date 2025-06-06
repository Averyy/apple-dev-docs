# menu()

**Framework**: InputMethodKit  
**Kind**: method

Returns a menu of commands that are specific to an input method.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func menu() -> NSMenu!
```

#### Return Value

The menu object.

#### Discussion

This method is called whenever the menu needs to be drawn so that an input method can update the menu to reflect the current state.

## See Also

- [func doCommand(by: Selector!, command: [AnyHashable : Any]!)](imkinputcontroller/docommand(by:command:).md)
  Passes commands that are not generated as part of the text input process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/menu())*