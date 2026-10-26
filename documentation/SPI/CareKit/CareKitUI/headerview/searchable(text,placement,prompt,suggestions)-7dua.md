---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/searchable(text:placement:prompt:suggestions:)-7dua"
framework: "CareKit/CareKitUI"
---

# searchable(text:placement:prompt:suggestions:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.searchable(text:placement:prompt:suggestions:)`.

**Availability**:
- iOS 15.0+ - Deprecated in 100000.0
- iPadOS 15.0+ - Deprecated in 100000.0
- Mac Catalyst 15.0+ - Deprecated in 100000.0
- macOS 12.0+ - Deprecated in 100000.0
- tvOS 15.0+ - Deprecated in 100000.0
- watchOS 8.0+ - Deprecated in 100000.0

> **Deprecated**: Use the searchable modifier with the searchSuggestions modifier

## Declaration

```swift
nonisolated
func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: S, @ViewBuilder suggestions: () -> V) -> some View where V : View, S : StringProtocol
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/searchable(text:placement:prompt:suggestions:)-7dua)*