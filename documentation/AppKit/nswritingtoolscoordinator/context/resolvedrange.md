# resolvedRange

**Framework**: AppKit  
**Kind**: property

The actual range of text that Writing Tools might change, which can be different than the range of text you supplied.

**Availability**:
- macOS 15.2+

## Declaration

```swift
var resolvedRange: NSRange { get }
```

#### Discussion

After analyzing the text in your context object, Writing Tools sets this property to the portion of [`attributedString`](nswritingtoolscoordinator/context/attributedstring.md) it might modify. Initially, this property has a location of [`NSNotFound`](https://developer.apple.com/documentation/Foundation/NSNotFound-4qp9h) and a length of `0`, but Writing Tools updates those values before making any changes to the text.

While the Writing Tools operation is active, make sure Writing Tools has exclusive access to the text in this range. Your [`NSWritingToolsCoordinator.Delegate`](nswritingtoolscoordinator/delegate-swift.protocol.md) object can make changes to the text as part of incorporating Writing Tools results, but don’t allow changes to come from other sources. For example, don’t let someone edit the text in this range directly until Writing Tools finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/context/resolvedrange)*