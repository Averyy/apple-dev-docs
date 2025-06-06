# completionHandler

**Framework**: UIKit  
**Kind**: property

The completion handler to execute after the activity view controller is dismissed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var completionHandler: UIActivityViewController.CompletionHandler? { get set }
```

#### Discussion

When the user-selected service finishes operating on the data, or when the user dismisses the view controller, the view controller executes this completion handler to let your app know the final result of the operation.

## See Also

- [UIActivityViewController.CompletionHandler](uiactivityviewcontroller/completionhandler-swift.typealias.md)
  A completion handler to execute after the activity view controller is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionhandler-swift.property)*