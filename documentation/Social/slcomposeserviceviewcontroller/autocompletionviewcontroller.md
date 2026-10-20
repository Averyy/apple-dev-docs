# autoCompletionViewController

**Framework**: Social  
**Kind**: property  
**Role**: Instance Property

The view controller that manages an autocompletion view for suggesting common text completions while users type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var autoCompletionViewController: UIViewController! { get set }
```

```objc
@property (nonatomic, strong) UIViewController * autoCompletionViewController;
```

#### Discussion

An autocompletion view can appear in place of the list of configuration items, just below the text view in the compose view. The compose view controller allows only one autocompletion view controller to be present at a time.

Note that your custom autocompletion view controller should set its [`preferredContentSize`](../../UIKit/uiviewcontroller/preferredcontentsize.md) property to an appropriate value. `SLComposeServiceViewController` observes changes to the [`preferredContentSize`](../../UIKit/uiviewcontroller/preferredcontentsize.md) property and animates view size changes, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/autocompletionviewcontroller)*