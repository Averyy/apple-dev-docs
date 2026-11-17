# handler

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The closure to run when someone interacts with any part of the row.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var handler: ((any CPSelectableListItem, @escaping () -> Void) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^)(id<CPSelectableListItem>, void (^)(void)) handler;
```

## Discussion

After creating a `CPListImageRowItem`, set the value of this property to the closure you want CarPlay to run when someone interacts with the row. Define your closure to return no value and receive the following parameters:

The row the person selected, which is typically a `CPListImageRowItem` object. A completion closure to call when you finish processing the selection

In your closure, perform any necessary work and call the provided completion closure. CarPlay runs the closure on your app’s main queue, so finish your tasks as quickly as possible. If you need to perform work that might take longer to finish, perform that work asynchronously or on a background queue to avoid tying up the main queue.

As soon as you complete all your work, including any asynchronous work, call the provided completion closure to let CarPlay know you’re done. Until you run the completion closure, CarPlay displays an asynchronous progress indicator in your list item. Running the closure removes this indicator so that people know the task finished.

The following example shows the handler for a row that pushes a new page onto the app’s navigation stack. The owning type stores the current [`CPInterfaceController`](../cpinterfacecontroller.md)  object in the `interfaceController` property and stores the template for the new page in the `newListPage` variable.

```swift
myImageRow.handler = { row, completion in
    guard self.interfaceController != nil else {
        completion()
        return
    }
            
    self.interfaceController!.pushTemplate(newListPage, animated: true) { displayed, error in
        let result = displayed ? "appeared" : "returned an error"
        Swift.print(“Page \(result)")
    }
    completion()
}
```

To detect which of the row’s elements someone selected, provide a closure in the [`listImageRowHandler`](./listimagerowhandler.md) property.

## See Also

### Responding to interactions
- [var listImageRowHandler: ((CPListImageRowItem, Int, () -> Void) -> Void)?](./listimagerowhandler.md)
  The closure to run when someone interacts with one of the elements in the row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/handler)*