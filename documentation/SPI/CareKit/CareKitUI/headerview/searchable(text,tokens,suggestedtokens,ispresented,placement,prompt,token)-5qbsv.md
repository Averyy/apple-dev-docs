---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-5qbsv"
framework: "CareKit/CareKitUI"
---

# searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: S, @ViewBuilder token: @escaping (C.Element) -> T) -> some View where C : MutableCollection, C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, S : StringProtocol, C.Element : Identifiable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-5qbsv)*