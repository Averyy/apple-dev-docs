---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/keyframeanimator(initialvalue:repeating:content:keyframes:)"
framework: "CareKit/CareKitUI"
---

# keyframeAnimator(initialValue:repeating:content:keyframes:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.keyframeAnimator(initialValue:repeating:content:keyframes:)`.

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
func keyframeAnimator<Value>(initialValue: Value, repeating: Bool = true, @ViewBuilder content: @escaping @Sendable (PlaceholderContentView<Self>, Value) -> some View, @KeyframesBuilder<Value> keyframes: @escaping (Value) -> some Keyframes) -> some View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/keyframeanimator(initialvalue:repeating:content:keyframes:))*