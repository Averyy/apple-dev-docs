---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/transaction(_:body:)"
framework: "CareKit/CareKitUI"
---

# transaction(_:body:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.transaction(_:body:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func transaction<V>(_ transform: @escaping (inout Transaction) -> Void, @ViewBuilder body: (PlaceholderContentView<Self>) -> V) -> some View where V : View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/transaction(_:body:))*