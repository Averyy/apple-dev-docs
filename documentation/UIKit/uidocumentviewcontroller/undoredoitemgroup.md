# undoRedoItemGroup

**Framework**: UIKit  
**Kind**: property

The group that contains the undo/redo buttons that this view controller adds to the navigation bar.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var undoRedoItemGroup: UIBarButtonItemGroup { get }
```

#### Discussion

If you want undo and redo buttons to appear in your `UIDocumentViewController`, add an `undoRedoItemGroup` to the navigation bar and ensure that your custom `UIDocument` has an undo manager assigned to it. `UIDocumentViewController` sets the hidden property of this group, depending on the availability of an undo manager. It automatically enables or disables the buttons inside the group, as necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/undoredoitemgroup)*