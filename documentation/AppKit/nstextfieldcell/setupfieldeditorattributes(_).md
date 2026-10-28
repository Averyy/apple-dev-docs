# setUpFieldEditorAttributes(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the cell to set up the field editor’s attributes before editing begins.

**Availability**:
- macOS

## Declaration

```swift
func setUpFieldEditorAttributes(_ textObj: NSText) -> NSText
```

```objc
- (NSText *) setUpFieldEditorAttributes:(NSText *) textObj;
```

## Return Value

A text object with customized attributes suitable for editing the text field cell’s content.

## Discussion

You never invoke this method directly; by overriding it, however, you can customize the field editor. When you override this method, you should generally invoke the implementation of `super` and return the `textObj` argument. For information on field editors, see [Using the Window’s Field Editor](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Tasks/UsingWindowFieldEditor.html#//apple_ref/doc/uid/20000238).

## Parameters

- `textObj`: A text object configured as a field editor.

## See Also

### Managing the Field Editor
- [func setWantsNotificationForMarkedText(Bool)](./setwantsnotificationformarkedtext%28_%29.md)
  Directs the cell’s associated field editor to post text change notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/setupfieldeditorattributes(_:))*