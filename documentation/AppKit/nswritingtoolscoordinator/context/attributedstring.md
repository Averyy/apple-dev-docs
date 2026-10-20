# attributedString

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The portion of your view’s text to evaluate.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@NSCopying
var attributedString: NSAttributedString { get }
```

```objc
@property (copy, readonly) NSAttributedString * attributedString;
```

#### Discussion

The [`NSWritingToolsCoordinator.Context`](../context.md) object initializes the value of this property at creation time and doesn’t change it during the course of an operation. Instead, it suggests changes to the text in the indicated range and reports those changes to your [`NSWritingToolsCoordinator.Delegate`](../delegate-swift.protocol.md) object. Use the methods of your delegate object to integrate those changes back into your view’s text storage.

It’s your responsibility to track the location of this text in your view’s text storage object. When Writing Tools reports changes, it provides range values relative to this string. If you initialize this property with a subset of your view’s content, you must adjust any ranges that Writing Tools provides to get the correct location in your text storage.

## See Also

### Getting the source text details
- [var range: NSRange](./range.md)
  The unique identifier of the context object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/context/attributedstring)*