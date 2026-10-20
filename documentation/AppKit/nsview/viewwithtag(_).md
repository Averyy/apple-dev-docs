# viewWithTag(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the view’s nearest descendant (including itself) with a specific tag, or `nil` if no subview has that tag.

**Availability**:
- macOS

## Declaration

```swift
func viewWithTag(_ tag: Int) -> NSView?
```

```objc
- (NSView *) viewWithTag:(NSInteger) tag;
```

## Parameters

- `tag`: An integer identifier associated with a view object.

## See Also

### Identifying Views by Tag
- [var tag: Int](./tag.md)
  The view’s tag, which is an integer that you use to identify the view within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewwithtag(_:))*