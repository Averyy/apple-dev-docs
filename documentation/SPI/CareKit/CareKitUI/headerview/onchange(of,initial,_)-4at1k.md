---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/onchange(of:initial:_:)-4at1k"
framework: "CareKit/CareKitUI"
---

# onChange(of:initial:_:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.onChange(of:initial:_:)`.

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
func onChange<V>(of value: V, initial: Bool = false, _ action: @escaping (V, V) -> Void) -> some View where V : Equatable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/onchange(of:initial:_:)-4at1k)*