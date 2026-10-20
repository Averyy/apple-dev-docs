# browser(_:pasteboardWriterForRow:column:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 27.0+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, pasteboardWriterForRow row: Int, column: Int) -> (any NSPasteboardWriting)?
```

```objc
- (id<NSPasteboardWriting>) browser:(NSBrowser *) browser pasteboardWriterForRow:(NSInteger) row column:(NSInteger) column;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:pasteboardwriterforrow:column:))*