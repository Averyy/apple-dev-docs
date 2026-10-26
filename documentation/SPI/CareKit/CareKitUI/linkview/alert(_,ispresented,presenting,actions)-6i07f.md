---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/alert(_:ispresented:presenting:actions:)-6i07f"
framework: "CareKit/CareKitUI"
---

# alert(_:isPresented:presenting:actions:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.alert(_:isPresented:presenting:actions:)`.

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
func alert<S, A, T>(_ title: S, isPresented: Binding<Bool>, presenting data: T?, @ViewBuilder actions: (T) -> A) -> some View where S : StringProtocol, A : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/alert(_:ispresented:presenting:actions:)-6i07f)*