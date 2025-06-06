# readSelection(from:)

**Framework**: AppKit  
**Kind**: method

Reads data from the pasteboard and uses it to replace the current selection.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func readSelection(from pboard: NSPasteboard) -> Bool
```

## Mentions

- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)
- [Supporting Continuity Camera in Your Mac App](supporting-continuity-camera-in-your-mac-app.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if your implementation was able to read the pasteboard data successfully; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

You implement this method to replace your application’s current selection (that is, the text or objects that are currently selected) with the data on the pasteboard. The data would have been placed in the pasteboard by another application in response to a remote message from the Services menu. A [`readSelection(from:)`](nsservicesmenurequestor/readselection(from:).md) message is sent to the same object that previously received a [`writeSelection(to:types:)`](nsservicesmenurequestor/writeselection(to:types:).md) message.

## Parameters

- `pboard`: The pasteboard containing the data to read.

## See Also

- [Services Implementation Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SysServices/introduction.html#//apple_ref/doc/uid/10000101i)
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](nsservicesmenurequestor/writeselection(to:types:).md)
  Writes the current selection to the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsservicesmenurequestor/readselection(from:))*