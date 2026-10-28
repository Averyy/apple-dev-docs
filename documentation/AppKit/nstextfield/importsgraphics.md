# importsGraphics

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether the user can drag image files into the text field.

**Availability**:
- macOS

## Declaration

```swift
var importsGraphics: Bool { get set }
```

```objc
@property BOOL importsGraphics;
```

## Discussion

If [`true`](../../Swift/true.md), the text field accepts dragged images; if [`false`](../../Swift/false.md), it doesn’t. You can add images programmatically regardless of this setting.

## See Also

### Controlling rich text behavior
- [var allowsEditingTextAttributes: Bool](./allowseditingtextattributes.md)
  A Boolean value that controls whether the user can change font attributes of the text field’s string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/importsgraphics)*