# importsGraphics

**Framework**: AppKit  
**Kind**: property

A Boolean value that controls whether the user can drag image files into the text field.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var importsGraphics: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the text field accepts dragged images; if [`false`](https://developer.apple.com/documentation/swift/false), it doesn’t. You can add images programmatically regardless of this setting.

## See Also

- [var allowsEditingTextAttributes: Bool](nstextfield/allowseditingtextattributes.md)
  A Boolean value that controls whether the user can change font attributes of the text field’s string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/importsgraphics)*