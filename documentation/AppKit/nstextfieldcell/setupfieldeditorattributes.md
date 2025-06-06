# setUpFieldEditorAttributes(_:)

**Framework**: AppKit  
**Kind**: method

Allows the cell to set up the field editor’s attributes before editing begins.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setUpFieldEditorAttributes(_ textObj: NSText) -> NSText
```

#### Return Value

A text object with customized attributes suitable for editing the text field cell’s content.

#### Discussion

You never invoke this method directly; by overriding it, however, you can customize the field editor. When you override this method, you should generally invoke the implementation of `super` and return the `textObj` argument. For information on field editors, see [`Using the Window’s Field Editor`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/UsingWindowFieldEditor.html#//apple_ref/doc/uid/20000238).

## Parameters

- `textObj`: A text object configured as a field editor.

## See Also

- [func setWantsNotificationForMarkedText(Bool)](nstextfieldcell/setwantsnotificationformarkedtext(_:).md)
  Directs the cell’s associated field editor to post text change notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/setupfieldeditorattributes(_:))*