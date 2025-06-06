# readableDraggedTypes

**Framework**: AppKit  
**Kind**: property

An array containing dragged file types that are readable.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class var readableDraggedTypes: [String] { get }
```

#### Discussion

A view must register what types it accepts via [`registerForDraggedTypes(_:)`](nsview/registerfordraggedtypes(_:).md).  Use that class method to get the file promise drag types that [`NSFilePromiseReceiver`](nsfilepromisereceiver.md) can accept, in order to register a view to accept promised files. [`NSFilePromiseReceiver`](nsfilepromisereceiver.md) can accept file promises from both the item-based [`NSFilePromiseProvider`](nsfilepromiseprovider.md) and the non-item based API. If you don’t register all these drag types, you might not be notified about some file promise drags. Register using the following code:


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfilepromisereceiver/readabledraggedtypes)*