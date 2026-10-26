---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/searchable(text:tokens:ispresented:placement:prompt:token:)-8yz0i"
framework: "CareKit/CareKitUI"
---

# searchable(text:tokens:isPresented:placement:prompt:token:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.searchable(text:tokens:isPresented:placement:prompt:token:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey, @ViewBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/searchable(text:tokens:ispresented:placement:prompt:token:)-8yz0i)*