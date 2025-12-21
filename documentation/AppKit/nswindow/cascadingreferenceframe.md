# cascadingReferenceFrame

**Framework**: AppKit  
**Kind**: property

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
var cascadingReferenceFrame: NSRect { get }
```

#### Discussion

The frame to use when cascading or sizing a new window based on the receiver’s position or size. This may be different from `frame` when the receiver is positioned by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/cascadingreferenceframe)*