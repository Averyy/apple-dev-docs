---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-4h5hs"
framework: "CareKit/CareKitUI"
---

# confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func confirmationDialog<A, M, T>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility = .automatic, presenting data: T?, @ViewBuilder actions: (T) -> A, @ViewBuilder message: (T) -> M) -> some View where A : View, M : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-4h5hs)*