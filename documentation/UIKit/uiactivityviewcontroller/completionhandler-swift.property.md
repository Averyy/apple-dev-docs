# completionHandler

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The completion handler to execute after the activity view controller is dismissed.

**Availability**:
- iOS 6.0+ - Deprecated in 8.0
- iPadOS 6.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`completionWithItemsHandler`](./completionwithitemshandler-swift.property.md) property instead.

## Declaration

```swift
var completionHandler: UIActivityViewController.CompletionHandler? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIActivityViewControllerCompletionHandler completionHandler;
```

## Discussion

When the user-selected service finishes operating on the data, or when the user dismisses the view controller, the view controller executes this completion handler to let your app know the final result of the operation.

## See Also

### Accessing the completion handler
- [var completionWithItemsHandler: UIActivityViewController.CompletionWithItemsHandler?](./completionwithitemshandler-swift.property.md)
  The completion handler to execute after the activity view controller is dismissed.
- [UIActivityViewController.CompletionWithItemsHandler](./completionwithitemshandler-swift.typealias.md)
  A completion handler to execute after the activity view controller is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionhandler-swift.property)*