---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/confirmationdialog(_:ispresented:titlevisibility:actions:)-32vvv"
framework: "CareKit/CareKitUI"
---

# confirmationDialog(_:isPresented:titleVisibility:actions:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.confirmationDialog(_:isPresented:titleVisibility:actions:)`.

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
func confirmationDialog<A>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility = .automatic, @ViewBuilder actions: () -> A) -> some View where A : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/confirmationdialog(_:ispresented:titlevisibility:actions:)-32vvv)*