# undoManager

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The undo manager for this responder.

**Availability**:
- macOS

## Declaration

```swift
var undoManager: UndoManager? { get }
```

```objc
@property (strong, readonly, nullable) NSUndoManager * undoManager;
```

#### Discussion

The  `NSResponder` implementation simply invokes this property on the next responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/undomanager)*