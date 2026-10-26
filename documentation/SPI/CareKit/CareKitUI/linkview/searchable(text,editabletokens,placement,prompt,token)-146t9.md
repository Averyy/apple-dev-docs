---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/searchable(text:editabletokens:placement:prompt:token:)-146t9"
framework: "CareKit/CareKitUI"
---

# searchable(text:editableTokens:placement:prompt:token:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.searchable(text:editableTokens:placement:prompt:token:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement = .automatic, prompt: Text? = nil, @ViewBuilder token: @escaping (Binding<C.Element>) -> some View) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, C.Element : Identifiable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/searchable(text:editabletokens:placement:prompt:token:)-146t9)*