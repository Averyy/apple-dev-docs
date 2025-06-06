# backgroundColor

**Framework**: AppKit  
**Kind**: property

The background color of the action button.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@NSCopying
var backgroundColor: NSColor! { get set }
```

#### Discussion

Use this property to specify the background color for your button. If you do not specify a value for this property, AppKit assigns a default color based on the value in the [`style`](nstableviewrowaction/style-swift.property.md) property. Generally, this color is red for destructive actions and blue for nondestructive actions.

## See Also

- [var style: NSTableViewRowAction.Style](nstableviewrowaction/style-swift.property.md)
  The style applied to the action button.
- [var title: String](nstableviewrowaction/title.md)
  The title of the action button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewrowaction/backgroundcolor)*