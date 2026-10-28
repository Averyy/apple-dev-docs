# quaternaryLabelColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The quaternary color to use for text labels and separators.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class var quaternaryLabelColor: NSColor { get }
```

```objc
@property (class, strong, readonly) NSColor * quaternaryLabelColor;
```

## Discussion

Use this color for the least important text in your interface and for separators between text items. For example, you would use this color for secondary text that is disabled. You can also use it for other types of quaternary app content.

## See Also

### Label colors
- [class var labelColor: NSColor](./labelcolor.md)
  The primary color to use for text labels.
- [class var secondaryLabelColor: NSColor](./secondarylabelcolor.md)
  The secondary color to use for text labels.
- [class var tertiaryLabelColor: NSColor](./tertiarylabelcolor.md)
  The tertiary color to use for text labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/quaternarylabelcolor)*