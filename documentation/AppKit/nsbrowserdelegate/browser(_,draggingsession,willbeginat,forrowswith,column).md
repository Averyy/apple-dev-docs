# browser(_:draggingSession:willBeginAt:forRowsWith:column:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 27.0+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, draggingSession session: NSDraggingSession, willBeginAt screenPoint: NSPoint, forRowsWith rowIndexes: IndexSet, column: Int)
```

```objc
- (void) browser:(NSBrowser *) browser draggingSession:(NSDraggingSession *) session willBeginAtPoint:(NSPoint) screenPoint forRowsWithIndexes:(NSIndexSet *) rowIndexes column:(NSInteger) column;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:draggingsession:willbeginat:forrowswith:column:))*