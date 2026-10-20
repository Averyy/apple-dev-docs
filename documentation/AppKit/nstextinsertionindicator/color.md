# color

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color of this indicator.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@NSCopying
var color: NSColor! { get set }
```

```objc
@property (copy, null_resettable) NSColor * color;
```

#### Discussion

If set to [`nil`](../../ObjectiveC/nil-227m0.md), returns [`textInsertionPointColor`](../nscolor/textinsertionpointcolor.md). Defaults to [`textInsertionPointColor`](../nscolor/textinsertionpointcolor.md).

## See Also

### Configuring indicators
- [var effectsViewInserter: ((NSView) -> Void)?](./effectsviewinserter.md)
  An optional closure the system calls during dictation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinsertionindicator/color)*