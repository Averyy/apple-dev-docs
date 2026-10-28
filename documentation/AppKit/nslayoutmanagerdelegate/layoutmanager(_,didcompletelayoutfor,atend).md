# layoutManager(_:didCompleteLayoutFor:atEnd:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate when the layout manager finishes laying out text in the specified text container.

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, didCompleteLayoutFor textContainer: NSTextContainer?, atEnd layoutFinishedFlag: Bool)
```

```objc
- (void) layoutManager:(NSLayoutManager *) layoutManager didCompleteLayoutForTextContainer:(NSTextContainer *) textContainer atEnd:(BOOL) layoutFinishedFlag;
```

## Discussion

This message is sent whenever a text container has been filled. This method can be useful for paginating.

## Parameters

- `layoutManager`: The layout manager doing the layout.
- `textContainer`: The text container in which layout is complete. If `nil`, if there aren’t enough containers to hold all the text; the delegate can use this information as a cue to add another text container.
- `layoutFinishedFlag`: If [`true`](../../Swift/true.md), `aLayoutManager` is finished laying out its text—this also means that `aTextContainer` is the final text container used by the layout manager. Delegates can use this information to show an indicator or background or to enable or disable a button that forces immediate layout of text.

## See Also

### Responding to text container layout
- [func layoutManager(NSLayoutManager, textContainer: NSTextContainer, didChangeGeometryFrom: NSSize)](./layoutmanager%28_,textcontainer,didchangegeometryfrom%29.md)
  Informs the delegate when the layout manager invalidates layout due to a change in the geometry of the specified text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/layoutmanager(_:didcompletelayoutfor:atend:))*