# selectText(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the entry at the specified index.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use NSTextField directly instead, and consider NSStackView for layout assistance

## Declaration

```swift
func selectText(at index: Int)
```

```objc
- (void) selectTextAtIndex:(NSInteger) index;
```

## Parameters

- `index`: The index of the entry to select. If the specified index is invalid, this method does nothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/selecttext(at:))*