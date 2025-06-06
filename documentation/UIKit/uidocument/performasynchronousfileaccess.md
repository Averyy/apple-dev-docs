# performAsynchronousFileAccess(_:)

**Framework**: UIKit  
**Kind**: method

Schedules a document-reading or document-writing operation on a concurrent background queue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func performAsynchronousFileAccess(_ block: @escaping () -> Void)
```

#### Discussion

A typical [`UIDocument`](uidocument.md) subclass — one that overrides [`contents(forType:)`](uidocument/contents(fortype:).md) and [`load(fromContents:ofType:)`](uidocument/load(fromcontents:oftype:).md) — doesn’t need to call this method.

The default implementations of [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) and [`open(completionHandler:)`](uidocument/open(completionhandler:).md) call this method to serialize file access. If you override these methods and don’t call `super`, you should call this method to serialize file access on a background queue. If you directly call the [`read(from:)`](uidocument/read(from:).md) method, you should wrap that call in the block passed into [`performAsynchronousFileAccess(_:)`](uidocument/performasynchronousfileaccess(_:).md).

## Parameters

- `block`: A block that’s invoked as the task to execute on the background queue. The block returns no value and takes no parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/performasynchronousfileaccess(_:))*