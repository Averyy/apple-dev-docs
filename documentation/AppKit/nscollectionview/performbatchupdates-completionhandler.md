# performBatchUpdates(_:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Encapsulates multiple insert, delete, reload, and move operations into a single animated operation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func performBatchUpdates(_ updates: (() -> Void)?) async -> Bool
```

#### Discussion

Use this method to make multiple changes to the collection view in one single animated operation. Normally, when you insert, delete, reload, or move items, the collection view animates each change separately. Making those same changes inside the `updates` block causes them to be animated at the same time. This method updates the current layout information as needed before and after performing the operations in the `updates` block.

The order in which you make calls to insert, delete, or otherwise modify the collection view is ignored. When executing your `updates` block, this method gathers information about the operations you requested without performing those operations. After it gathers that information, the method reorders the operations and performs all deletion operations first, followed by all insertion operations and then all move operations. (Reloading an item is treated as a delete operation followed by an insert operation at the same location.) As a result, the indexes you specify for each set of operations must reflect the changes made by any preceding operations.

You may call this method from inside your `updates` or `completionHandler` blocks.

## Parameters

- `updates`: The block that performs the needed inset, delete, reload, or move operations. This parameter may be  .
- `completionHandler`: A completion handler block to execute when the changes made in the   block have finished animating. This parameter may be  . This block takes the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/performbatchupdates(_:completionhandler:))*