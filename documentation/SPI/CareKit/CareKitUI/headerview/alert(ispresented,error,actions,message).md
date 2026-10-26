---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/alert(ispresented:error:actions:message:)"
framework: "CareKit/CareKitUI"
---

# alert(isPresented:error:actions:message:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.alert(isPresented:error:actions:message:)`.

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
func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, @ViewBuilder actions: (E) -> A, @ViewBuilder message: (E) -> M) -> some View where E : LocalizedError, A : View, M : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/alert(ispresented:error:actions:message:))*