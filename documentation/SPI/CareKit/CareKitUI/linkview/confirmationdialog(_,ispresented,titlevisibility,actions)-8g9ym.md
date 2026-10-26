---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/confirmationdialog(_:ispresented:titlevisibility:actions:)-8g9ym"
framework: "CareKit/CareKitUI"
---

# confirmationDialog(_:isPresented:titleVisibility:actions:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.confirmationDialog(_:isPresented:titleVisibility:actions:)`.

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
func confirmationDialog<S, A>(_ title: S, isPresented: Binding<Bool>, titleVisibility: Visibility = .automatic, @ViewBuilder actions: () -> A) -> some View where S : StringProtocol, A : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/confirmationdialog(_:ispresented:titlevisibility:actions:)-8g9ym)*