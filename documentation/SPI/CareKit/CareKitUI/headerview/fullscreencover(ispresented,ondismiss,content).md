---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/fullscreencover(ispresented:ondismiss:content:)"
framework: "CareKit/CareKitUI"
---

# fullScreenCover(isPresented:onDismiss:content:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.fullScreenCover(isPresented:onDismiss:content:)`.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)? = nil, @ViewBuilder content: @escaping () -> Content) -> some View where Content : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/fullscreencover(ispresented:ondismiss:content:))*