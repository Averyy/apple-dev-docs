# listImageRowHandler

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The closure to run when someone interacts with one of the elements in the row.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var listImageRowHandler: ((CPListImageRowItem, Int, @escaping () -> Void) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^listImageRowHandler)(CPListImageRowItem *item, NSInteger index, dispatch_block_t completionBlock);
```

## Discussion

After creating a `CPListImageRowItem`, set the value of this property to the closure you want CarPlay to run when someone interacts with one of the row’s elements. Define your closure to return no value and receive the following parameters:

The row the person selected. The zero-based index of the element the person selected. Use this value to fetch the element from the row’s [`elements`](./elements.md) array. A completion closure to call when you finish processing the selection

In your closure, perform any necessary work and call the provided completion closure. CarPlay runs the closure on your app’s main queue, so finish your tasks as quickly as possible. If you need to perform work that might take longer to finish, perform that work asynchronously or on a background queue to avoid tying up the main queue.

As soon as you complete all your work, including any asynchronous work, call the provided completion closure to let CarPlay know you’re done. Until you run the completion closure, CarPlay displays an asynchronous progress indicator in your list item. Running the closure removes this indicator so that people know the task finished.

The following example shows a handler for a row that contains [`CPListImageRowItemRowElement`](../cplistimagerowitemrowelement.md) types. When someone selects an element, the handler validates the selected item and processes the selection before running the completion closure.

```swift
row1.listImageRowHandler = { item, index, completion in
    guard let selectedItem = item.elements[index] as? CPListImageRowItemRowElement else {
        Swift.print("Expected a row element but got an unknown type.")
        completion()
        return
    }

    // Process the selected item...

    // Call the completion closure.
    completion()
}
```

## See Also

### Responding to interactions
- [var handler: ((any CPSelectableListItem, () -> Void) -> Void)?](./handler.md)
  The closure to run when someone interacts with any part of the row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/listimagerowhandler)*