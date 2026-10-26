---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/alert(ispresented:error:actions:)"
framework: "CareKit/CareKitUI"
---

# alert(isPresented:error:actions:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.alert(isPresented:error:actions:)`.

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
func alert<E, A>(isPresented: Binding<Bool>, error: E?, @ViewBuilder actions: () -> A) -> some View where E : LocalizedError, A : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/alert(ispresented:error:actions:))*