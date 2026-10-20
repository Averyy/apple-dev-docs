# browser(_:draggingSession:endedAt:operation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 27.0+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, draggingSession session: NSDraggingSession, endedAt screenPoint: NSPoint, operation: NSDragOperation)
```

```objc
- (void) browser:(NSBrowser *) browser draggingSession:(NSDraggingSession *) session endedAtPoint:(NSPoint) screenPoint operation:(NSDragOperation) operation;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:draggingsession:endedat:operation:))*