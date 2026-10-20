# contentText

**Framework**: Social  
**Kind**: property  
**Role**: Instance Property

A string that represents the text which the user entered into the compose view’s text view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
var contentText: String! { get }
```

*iOS, iPadOS, Mac Catalyst*

```objc
@property (nonatomic, readonly) NSString * contentText;
```

*macOS*

```objc
@property (atomic, readonly) NSString * contentText;
```

## See Also

### Managing the Contents of the Post
- [var placeholder: String!](./placeholder.md)
  A string that’s displayed in the compose view’s text view when the text view is empty.
- [var textView: UITextView!](./textview.md)
  The editable text view in the compose view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/contenttext)*