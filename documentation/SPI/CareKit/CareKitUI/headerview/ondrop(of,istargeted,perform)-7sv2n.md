---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/ondrop(of:istargeted:perform:)-7sv2n"
framework: "CareKit/CareKitUI"
---

# onDrop(of:isTargeted:perform:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.onDrop(of:isTargeted:perform:)`.

**Availability**:
- iOS 13.4+ - Deprecated in 100000.0
- iPadOS 13.4+ - Deprecated in 100000.0
- Mac Catalyst 13.4+ - Deprecated in 100000.0
- macOS 10.15+ - Deprecated in 100000.0
- visionOS 1.0+ - Deprecated in 100000.0

> **Deprecated**: Provide `UTType`s as the `supportedContentTypes` instead.

## Declaration

```swift
nonisolated
func onDrop(of supportedTypes: [String], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider], CGPoint) -> Bool) -> some View
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/ondrop(of:istargeted:perform:)-7sv2n)*