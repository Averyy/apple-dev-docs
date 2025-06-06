# setAccessibilityFrame(_:)

**Framework**: AppKit  
**Kind**: method

Sets the accessibility element’s frame.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func setAccessibilityFrame(_ frame: NSRect)
```

#### Discussion

This method is the setter method for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityFrame`](nsaccessibility-c.protocol/accessibilityframe.md) property. By implementing this method, you allow accessibility clients to modify this element’s frame.

## Parameters

- `frame`: The new frame in screen coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitylayoutitem/setaccessibilityframe(_:))*