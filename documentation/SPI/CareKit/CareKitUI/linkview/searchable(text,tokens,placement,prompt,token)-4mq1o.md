---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/searchable(text:tokens:placement:prompt:token:)-4mq1o"
framework: "CareKit/CareKitUI"
---

# searchable(text:tokens:placement:prompt:token:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.searchable(text:tokens:placement:prompt:token:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
nonisolated
func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringResource, @ViewBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/searchable(text:tokens:placement:prompt:token:)-4mq1o)*