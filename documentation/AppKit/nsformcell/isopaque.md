# isOpaque

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the title is empty and an opaque bezel is set.

**Availability**:
- macOS

## Declaration

```swift
var isOpaque: Bool { get }
```

```objc
@property (readonly, getter=isOpaque) BOOL opaque;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the cell is completely opaque or [`false`](../../Swift/false.md) if it contains some transparency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/isopaque)*