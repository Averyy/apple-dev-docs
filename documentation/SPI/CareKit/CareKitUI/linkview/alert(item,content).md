---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/alert(item:content:)"
framework: "CareKit/CareKitUI"
---

# alert(item:content:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.alert(item:content:)`.

**Availability**:
- iOS 13.0+ - Deprecated in 100000.0
- iPadOS 13.0+ - Deprecated in 100000.0
- Mac Catalyst 13.0+ - Deprecated in 100000.0
- macOS 10.15+ - Deprecated in 100000.0
- tvOS 13.0+ - Deprecated in 100000.0
- visionOS 1.0+ - Deprecated in 100000.0
- watchOS 6.0+ - Deprecated in 100000.0

> **Deprecated**: use `alert(title:isPresented:presenting::actions:) instead.

## Declaration

```swift
nonisolated
func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some View where Item : Identifiable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/alert(item:content:))*