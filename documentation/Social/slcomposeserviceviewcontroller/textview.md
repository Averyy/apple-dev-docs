# textView

**Framework**: Social  
**Kind**: property  
**Role**: Instance Property

The editable text view in the compose view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
var textView: UITextView! { get }
```

*macOS*

```swift
var textView: NSTextView! { get }
```

*iOS, iPadOS, Mac Catalyst*

```objc
@property (nonatomic, readonly) UITextView * textView;
```

*macOS*

```objc
@property (readonly) NSTextView * textView;
```

## Discussion

When a user activates a Post or Send button, you can send their text by sending `self.textView.text`. Note that the `SLComposeServiceViewController` base class creates `textView` in its [`loadView()`](../../UIKit/uiviewcontroller/loadview%28%29.md) method and sets itself to be the `textView` delegate.

## See Also

### Managing the Contents of the Post
- [var contentText: String!](./contenttext.md)
  A string that represents the text which the user entered into the compose view’s text view.
- [var placeholder: String!](./placeholder.md)
  A string that’s displayed in the compose view’s text view when the text view is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/textview)*