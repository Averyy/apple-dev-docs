# textView

**Framework**: Social  
**Kind**: property

The editable text view in the compose view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
@MainActor
var textView: NSTextView! { get }
```

#### Discussion

When a user activates a Post or Send button, you can send their text by sending `self.textView.text`. Note that the `SLComposeServiceViewController` base class creates `textView` in its [`loadView()`](https://developer.apple.com/documentation/UIKit/UIViewController/loadView()) method and sets itself to be the `textView` delegate.

## See Also

- [var contentText: String!](slcomposeserviceviewcontroller/contenttext.md)
  A string that represents the text which the user entered into the compose view’s text view.
- [var placeholder: String!](slcomposeserviceviewcontroller/placeholder.md)
  A string that’s displayed in the compose view’s text view when the text view is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/textview)*