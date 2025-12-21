# color

**Framework**: AppKit  
**Kind**: property

The color of this indicator.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@NSCopying
@MainActor var color: NSColor! { get set }
```

#### Discussion

If set to [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0), returns [`textInsertionPointColor`](nscolor/textinsertionpointcolor.md). Defaults to [`textInsertionPointColor`](nscolor/textinsertionpointcolor.md).

## See Also

- [var effectsViewInserter: ((NSView) -> Void)?](nstextinsertionindicator/effectsviewinserter.md)
  An optional closure the system calls during dictation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinsertionindicator/color)*