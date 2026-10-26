---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/phaseanimator(_:trigger:content:animation:)"
framework: "CareKit/CareKitUI"
---

# phaseAnimator(_:trigger:content:animation:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.phaseAnimator(_:trigger:content:animation:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func phaseAnimator<Phase>(_ phases: some Sequence, trigger: some Equatable, @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View, animation: @escaping (Phase) -> Animation? = { _ in .default }) -> some View where Phase : Equatable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/phaseanimator(_:trigger:content:animation:))*