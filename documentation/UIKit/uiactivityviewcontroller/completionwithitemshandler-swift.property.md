# completionWithItemsHandler

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The completion handler to execute after the activity view controller is dismissed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var completionWithItemsHandler: UIActivityViewController.CompletionWithItemsHandler? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIActivityViewControllerCompletionWithItemsHandler completionWithItemsHandler;
```

#### Discussion

When the user-selected service finishes operating on the data, or when the user dismisses the view controller, the view controller executes this completion handler to let your app know the final result of the operation.

## See Also

### Accessing the completion handler
- [UIActivityViewController.CompletionWithItemsHandler](./completionwithitemshandler-swift.typealias.md)
  A completion handler to execute after the activity view controller is dismissed.
- [var completionHandler: UIActivityViewController.CompletionHandler?](./completionhandler-swift.property.md)
  The completion handler to execute after the activity view controller is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionwithitemshandler-swift.property)*