# viewWithTag(_:)

**Framework**: AppKit  
**Kind**: method

Returns the view’s nearest descendant (including itself) with a specific tag, or `nil` if no subview has that tag.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func viewWithTag(_ tag: Int) -> NSView?
```

## Parameters

- `tag`: An integer identifier associated with a view object.

## See Also

- [var tag: Int](nsview/tag.md)
  The view’s tag, which is an integer that you use to identify the view within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewwithtag(_:))*