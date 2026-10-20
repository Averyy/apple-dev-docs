# range

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier of the context object.

**Availability**:
- macOS 15.2+

## Declaration

```swift
var range: NSRange { get }
```

```objc
@property (readonly) NSRange range;
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](../../adding-writing-tools-support-to-a-custom-nsview.md)

#### Discussion

The [`NSWritingToolsCoordinator.Context`](../context.md) object initializes the value of this property at creation time. Use this value to identify the context object within your app.

## See Also

### Getting the source text details
- [var attributedString: NSAttributedString](./attributedstring.md)
  The portion of your view’s text to evaluate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/context/range)*