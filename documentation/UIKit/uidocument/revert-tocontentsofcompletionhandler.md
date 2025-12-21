# revert(toContentsOf:completionHandler:)

**Framework**: UIKit  
**Kind**: method

Reverts a document to the most recent document data stored on-disk.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func revert(toContentsOf url: URL) async -> Bool
```

#### Discussion

You call this method to discard all unsaved document modifications and replace the document’s contents by reading the file or file package located by `url`. The default implementation brackets the reversion operation between [`disableEditing()`](uidocument/disableediting().md) and [`enableEditing()`](uidocument/enableediting().md)because the document shouldn’t accept user changes during this period. Subclasses that override this method must call the superclass implementation (`super`) or use the [`NSFileCoordinator`](https://developer.apple.com/documentation/Foundation/NSFileCoordinator) class to initiate a coordinated read.

## Parameters

- `url`: A file URL locating the most recent version of the document file in the application’s sandbox.
- `completionHandler`: The block is invoked on the main queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/revert(tocontentsof:completionhandler:))*