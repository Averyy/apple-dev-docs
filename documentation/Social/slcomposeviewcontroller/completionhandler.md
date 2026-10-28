# completionHandler

**Framework**: Social  
**Kind**: property  
**Role**: Instance Property

The handler to call when the user is done composing a post.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var completionHandler: SLComposeViewControllerCompletionHandler! { get set }
```

```objc
@property (nonatomic, copy) SLComposeViewControllerCompletionHandler completionHandler;
```

## Discussion

The handler has a single parameter that indicates whether the user finished or cancelled composing the post. This block is not guaranteed to be called on any particular thread. Do not dismiss the [`SLComposeViewController`](../slcomposeviewcontroller.md) in your completion handler—the system will do so automatically.

## See Also

### Processing the Results
- [typealias SLComposeViewControllerCompletionHandler](../slcomposeviewcontrollercompletionhandler.md)
  Defines a handler to call when the user finishes composing a post.
- [enum SLComposeViewControllerResult](../slcomposeviewcontrollerresult.md)
  Possible values for the `result` parameter of the [`completionHandler`](./completionhandler.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller/completionhandler)*