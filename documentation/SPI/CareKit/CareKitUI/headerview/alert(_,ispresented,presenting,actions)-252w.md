---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/alert(_:ispresented:presenting:actions:)-252w"
framework: "CareKit/CareKitUI"
---

# alert(_:isPresented:presenting:actions:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.alert(_:isPresented:presenting:actions:)`.

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
func alert<A, T>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, presenting data: T?, @ViewBuilder actions: (T) -> A) -> some View where A : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/alert(_:ispresented:presenting:actions:)-252w)*