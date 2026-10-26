---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-9ucwa"
framework: "CareKit/CareKitUI"
---

# searchable(text:tokens:suggestedTokens:placement:prompt:token:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.searchable(text:tokens:suggestedTokens:placement:prompt:token:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
nonisolated
func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey, @ViewBuilder token: @escaping (C.Element) -> T) -> some View where C : MutableCollection, C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-9ucwa)*