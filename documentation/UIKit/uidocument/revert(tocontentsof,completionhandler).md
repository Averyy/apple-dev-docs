# revert(toContentsOf:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reverts a document to the most recent document data stored on-disk.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func revert(toContentsOf url: URL, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

```swift
func revert(toContentsOf url: URL) async -> Bool
```

```objc
- (void) revertToContentsOfURL:(NSURL *) url completionHandler:(void (^)(BOOL success)) completionHandler;
```

## Discussion

You call this method to discard all unsaved document modifications and replace the document’s contents by reading the file or file package located by `url`. The default implementation brackets the reversion operation between [`disableEditing()`](./disableediting%28%29.md) and [`enableEditing()`](./enableediting%28%29.md)because the document shouldn’t accept user changes during this period. Subclasses that override this method must call the superclass implementation (`super`) or use the [`NSFileCoordinator`](../../Foundation/nsfilecoordinator.md) class to initiate a coordinated read.

## Parameters

- `url`: A file URL locating the most recent version of the document file in the application’s sandbox.
- `completionHandler`: A block with code to execute after the reversion operation concludes. The block returns no value and has one parameter:

  - **`success`**: [`true`](../../Swift/true.md) if the reversion operation succeeds, otherwise [`false`](../../Swift/false.md).

  The block is invoked on the main queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/revert(tocontentsof:completionhandler:))*