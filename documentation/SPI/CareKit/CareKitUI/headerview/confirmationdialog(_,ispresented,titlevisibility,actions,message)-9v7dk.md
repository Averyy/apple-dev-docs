---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-9v7dk"
framework: "CareKit/CareKitUI"
---

# confirmationDialog(_:isPresented:titleVisibility:actions:message:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.confirmationDialog(_:isPresented:titleVisibility:actions:message:)`.

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
func confirmationDialog<A, M>(_ titleKey: LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility = .automatic, @ViewBuilder actions: () -> A, @ViewBuilder message: () -> M) -> some View where A : View, M : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-9v7dk)*