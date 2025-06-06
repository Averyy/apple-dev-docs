# range

**Framework**: AppKit  
**Kind**: property

The unique identifier of the context object.

**Availability**:
- macOS 15.2+

## Declaration

```swift
var range: NSRange { get }
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)

#### Discussion

The [`NSWritingToolsCoordinator.Context`](nswritingtoolscoordinator/context.md) object initializes the value of this property at creation time. Use this value to identify the context object within your app.

## See Also

- [var attributedString: NSAttributedString](nswritingtoolscoordinator/context/attributedstring.md)
  The portion of your view’s text to evaluate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/context/range)*