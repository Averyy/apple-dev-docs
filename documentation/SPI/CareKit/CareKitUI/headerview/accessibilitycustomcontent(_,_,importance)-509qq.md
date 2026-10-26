---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/accessibilitycustomcontent(_:_:importance:)-509qq"
framework: "CareKit/CareKitUI"
---

# accessibilityCustomContent(_:_:importance:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.accessibilityCustomContent(_:_:importance:)`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

> **Deprecated**: Using non-localized strings for labels is not directly supported. Instead, wrap both the label and the value in a Text struct.

## Declaration

```swift
nonisolated
func accessibilityCustomContent<L, V>(_ label: L, _ value: V, importance: AXCustomContent.Importance = .default) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where L : StringProtocol, V : StringProtocol
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/accessibilitycustomcontent(_:_:importance:)-509qq)*