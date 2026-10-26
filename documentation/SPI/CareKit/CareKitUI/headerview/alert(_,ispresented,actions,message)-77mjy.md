---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/alert(_:ispresented:actions:message:)-77mjy"
framework: "CareKit/CareKitUI"
---

# alert(_:isPresented:actions:message:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.alert(_:isPresented:actions:message:)`.

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
func alert<A, M>(_ title: Text, isPresented: Binding<Bool>, @ViewBuilder actions: () -> A, @ViewBuilder message: () -> M) -> some View where A : View, M : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/alert(_:ispresented:actions:message:)-77mjy)*