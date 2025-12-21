# endSheet(_:)

**Framework**: AppKit  
**Kind**: method

Ends a SwiftUI hosted sheet presentation.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func endSheet<V>(_ host: NSWindow.HostingSheetRepresentation<V>) where V : View
```

#### Discussion

If the hosting sheet representation was invalid or no longer presented, no effect happens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/endsheet(_:)-6af2u)*