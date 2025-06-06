# replaceTextStorage(_:)

**Framework**: AppKit  
**Kind**: method

Replaces the layout manager’s current text storage object with the specified object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func replaceTextStorage(_ newTextStorage: NSTextStorage)
```

#### Discussion

Use this method to update the text storage uniformly for a group of related layout manager objects. Unlike changing the value in the textStorage property, this method replaces the text storage for all [`NSLayoutManager`](nslayoutmanager.md) objects that share the current layout manager’s [`NSTextStorage`](nstextstorage.md) object.

## Parameters

- `newTextStorage`: The text storage object to set.

## See Also

- [var textStorage: NSTextStorage?](nslayoutmanager/textstorage.md)
  The text storage object that contains the content to lay out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/replacetextstorage(_:))*