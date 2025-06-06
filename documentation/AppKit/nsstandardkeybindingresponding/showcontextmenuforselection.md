# showContextMenuForSelection(_:)

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
optional func showContextMenuForSelection(_ sender: Any?)
```

#### Discussion

```None
@method        `showContextMenuForSelection`
@abstract      Present a context menu at the text cursor position, selection, or wherever is appropriate for your responder.
@discussion    NSView has a default implementation of this method. For any view that returns a non-nil value from `-menuForEvent:`, the default implementation will display that menu automatically. The NSView implementation uses the `selectionAnchorRect` method in the `NSViewContentSelectionInfo` protocol to determine the location of the selection and of the menu. The NSView implementation determines the menu to display by calling `menuForEvent:` with a right-mouse-down event that is centered on the anchor rect. If `selectionAnchorRect` is not implemented, then the NSView implementation calls `menuForEvent` with a right-mouse-down event that is centered on the view's bounds, and also displays the menu at that location.

You should only override this method in a custom view if you need full control over the display of a context menu from the keyboard or Accessibility, beyond what is provided by default by NSView.

If the view does not support a context menu, then you should call `[[self nextResponder] tryToPerform:_cmd with:sender]` to pass the request up the responder chain.

@note          In some cases, this method will be called without a prior call to `contextMenuKeyDown:`. This occurs when a view receives an Accessibility ShowMenu action, or when the user has created a Cocoa Text key binding to map a different key combination to the `showContextMenuForSelection:` action.

@param         sender
               The object that originated the display of the context menu.

@seealso       `menuForEvent:`
@seealso       `selectionAnchorRect`
@seealso       `contextMenuKeyDown:`
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstandardkeybindingresponding/showcontextmenuforselection(_:))*