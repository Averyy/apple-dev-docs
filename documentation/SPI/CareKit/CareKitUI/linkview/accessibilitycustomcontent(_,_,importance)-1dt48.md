---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/accessibilitycustomcontent(_:_:importance:)-1dt48"
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

## Declaration

```swift
nonisolated
func accessibilityCustomContent<V>(_ key: AccessibilityCustomContentKey, _ value: V, importance: AXCustomContent.Importance = .default) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where V : StringProtocol
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/accessibilitycustomcontent(_:_:importance:)-1dt48)*