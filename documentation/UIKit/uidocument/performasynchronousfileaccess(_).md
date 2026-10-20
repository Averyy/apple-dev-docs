# performAsynchronousFileAccess(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Schedules a document-reading or document-writing operation on a concurrent background queue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func performAsynchronousFileAccess(_ block: @escaping () -> Void)
```

```objc
- (void) performAsynchronousFileAccessUsingBlock:(void (^)()) block;
```

#### Discussion

A typical [`UIDocument`](../uidocument.md) subclass — one that overrides [`contents(forType:)`](./contents%28fortype%29.md) and [`load(fromContents:ofType:)`](./load%28fromcontents,oftype%29.md) — doesn’t need to call this method.

The default implementations of [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md) and [`open(completionHandler:)`](./open%28completionhandler%29.md) call this method to serialize file access. If you override these methods and don’t call `super`, you should call this method to serialize file access on a background queue. If you directly call the [`read(from:)`](./read%28from%29.md) method, you should wrap that call in the block passed into [`performAsynchronousFileAccess(_:)`](./performasynchronousfileaccess%28_%29.md).

## Parameters

- `block`: A block that’s invoked as the task to execute on the background queue. The block returns no value and takes no parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/performasynchronousfileaccess(_:))*