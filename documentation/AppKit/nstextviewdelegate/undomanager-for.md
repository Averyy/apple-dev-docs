# undoManager(for:)

**Framework**: AppKit  
**Kind**: method

Returns the undo manager for the specified text view.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func undoManager(for view: NSTextView) -> UndoManager?
```

#### Return Value

The undo manager for `view`.

#### Discussion

This method provides the flexibility to return a custom undo manager for the text view. Although `NSTextView` implements undo and redo for changes to text, applications may need a custom undo manager to handle interactions between changes to text and changes to other items in the application.

## Parameters

- `view`: The text view whose undo manager should be returned.

## See Also

- [Text System User Interface Layer Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextUILayer/TextUILayer.html#//apple_ref/doc/uid/10000090i)
- [Cocoa Text Architecture Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009459)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/undomanager(for:))*