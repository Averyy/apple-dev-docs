# backgroundColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The background color of the action button.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@NSCopying
var backgroundColor: NSColor! { get set }
```

```objc
@property (copy, null_resettable) NSColor * backgroundColor;
```

## Discussion

Use this property to specify the background color for your button. If you do not specify a value for this property, AppKit assigns a default color based on the value in the [`style`](./style-swift.property.md) property. Generally, this color is red for destructive actions and blue for nondestructive actions.

## See Also

### Configuring the Action’s Appearance
- [var style: NSTableViewRowAction.Style](./style-swift.property.md)
  The style applied to the action button.
- [var title: String](./title.md)
  The title of the action button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewrowaction/backgroundcolor)*