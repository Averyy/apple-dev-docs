---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/actionsheet(item:content:)"
framework: "CareKit/CareKitUI"
---

# actionSheet(item:content:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.actionSheet(item:content:)`.

**Availability**:
- iOS 13.0+ - Deprecated in 100000.0
- iPadOS 13.0+ - Deprecated in 100000.0
- Mac Catalyst 13.0+ - Deprecated in 100000.0
- tvOS 13.0+ - Deprecated in 100000.0
- visionOS 1.0+ - Deprecated in 100000.0
- watchOS 6.0+ - Deprecated in 100000.0

> **Deprecated**: use `confirmationDialog(title:isPresented:titleVisibility:presenting:actions:)`instead.

## Declaration

```swift
nonisolated
func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View where T : Identifiable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/actionsheet(item:content:))*