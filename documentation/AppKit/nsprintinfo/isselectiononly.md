# isSelectionOnly

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether only the currently selected contents should be printed.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var isSelectionOnly: Bool { get set }
```

```objc
@property (getter=isSelectionOnly) BOOL selectionOnly;
```

## Discussion

[`true`](../../Swift/true.md) if only the currently selected contents should be printed, otherwise [`false`](../../Swift/false.md).

## See Also

### Print Settings Convenience Methods
- [var scalingFactor: CGFloat](./scalingfactor.md)
  The current scaling factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/isselectiononly)*