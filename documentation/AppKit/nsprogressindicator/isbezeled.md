# isBezeled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the progress indicator’s frame has a three-dimensional bezel.

**Availability**:
- macOS 10.0+ - Deprecated in 14.0

> **Deprecated**: The bezeled property is not respected on 10.15 and later

## Declaration

```swift
var isBezeled: Bool { get set }
```

```objc
@property (getter=isBezeled) BOOL bezeled;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the progress indicator is bezeled.

## See Also

### Deprecated properties
- [var controlTint: NSControlTint](./controltint.md)
  The progress indicator’s control tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/isbezeled)*