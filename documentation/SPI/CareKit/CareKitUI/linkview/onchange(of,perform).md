---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/onchange(of:perform:)"
framework: "CareKit/CareKitUI"
---

# onChange(of:perform:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.onChange(of:perform:)`.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0
- visionOS - Deprecated in 1.0
- watchOS 7.0+ - Deprecated in 10.0

> **Deprecated**: Use `onChange` with a two or zero parameter action closure instead.

## Declaration

```swift
nonisolated
func onChange<V>(of value: V, perform action: @escaping (V) -> Void) -> some View where V : Equatable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/onchange(of:perform:))*