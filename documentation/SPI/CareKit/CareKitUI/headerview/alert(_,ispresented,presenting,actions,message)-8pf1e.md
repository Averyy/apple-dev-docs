---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/alert(_:ispresented:presenting:actions:message:)-8pf1e"
framework: "CareKit/CareKitUI"
---

# alert(_:isPresented:presenting:actions:message:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.alert(_:isPresented:presenting:actions:message:)`.

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
func alert<S, A, M, T>(_ title: S, isPresented: Binding<Bool>, presenting data: T?, @ViewBuilder actions: (T) -> A, @ViewBuilder message: (T) -> M) -> some View where S : StringProtocol, A : View, M : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/alert(_:ispresented:presenting:actions:message:)-8pf1e)*