# storyboard

**Framework**: AppKit  
**Kind**: property

The storyboard from which the view controller was loaded.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var storyboard: NSStoryboard? { get }
```

#### Discussion

If the view controller was not loaded from a storyboard, the value of this property is `nil`.

## See Also

- [func dismiss(Any?)](nsviewcontroller/dismiss(_:)-3n76y.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/storyboard)*