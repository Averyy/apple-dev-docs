# allowsCutCopyPaste

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the image view lets the user cut, copy, and paste the image contents.

**Availability**:
- macOS

## Declaration

```swift
var allowsCutCopyPaste: Bool { get set }
```

```objc
@property BOOL allowsCutCopyPaste;
```

## Discussion

When the value of this property is YES, the user can cut, copy, or paste the image in the image view.

## See Also

### Responding to user events
- [var isEditable: Bool](./iseditable.md)
  A Boolean value indicating whether the user can drag a new image into the image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/allowscutcopypaste)*