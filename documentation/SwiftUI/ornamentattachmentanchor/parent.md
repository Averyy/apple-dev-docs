# parent(_:)

**Framework**: SwiftUI  
**Kind**: method

The anchor point for the ornament expressed as a 3D unit point relative to its parent.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func parent(_ anchor: UnitPoint3D) -> OrnamentAttachmentAnchor
```

#### Discussion

The parent depends on where the ornament modifier is placed. When used inside another ornament context, that ornament is the parent. Otherwise, it’s the Scene itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/ornamentattachmentanchor/parent(_:))*