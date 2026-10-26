---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/onreceive(_:perform:)"
framework: "CareKit/CareKitUI"
---

# onReceive(_:perform:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.onReceive(_:perform:)`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func onReceive<P>(_ publisher: P, perform action: @escaping (P.Output) -> Void) -> some View where P : Publisher, P.Failure == Never
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/onreceive(_:perform:))*