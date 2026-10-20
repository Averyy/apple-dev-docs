# tag

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view’s tag, which is an integer that you use to identify the view within your app.

**Availability**:
- macOS

## Declaration

```swift
var tag: Int { get }
```

```objc
@property (readonly) NSInteger tag;
```

#### Discussion

The default value of this property is `–1`. Subclasses can override this property to provide individual tags for views, possibly redefining the property as `readwrite` so that you can modify it more easily.

## See Also

### Identifying Views by Tag
- [func viewWithTag(Int) -> NSView?](./viewwithtag%28_%29.md)
  Returns the view’s nearest descendant (including itself) with a specific tag, or `nil` if no subview has that tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/tag)*