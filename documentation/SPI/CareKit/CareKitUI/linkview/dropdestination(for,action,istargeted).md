---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/dropdestination(for:action:istargeted:)"
framework: "CareKit/CareKitUI"
---

# dropDestination(for:action:isTargeted:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.dropDestination(for:action:isTargeted:)`.

**Availability**:
- iOS 16.0+ - Deprecated in 100000.0
- iPadOS 16.0+ - Deprecated in 100000.0
- Mac Catalyst 16.0+ - Deprecated in 100000.0
- macOS 13.0+ - Deprecated in 100000.0

> **Deprecated**: Use `dropDestination(for:isEnabled:action:)` with an `action` that takes a `DropSession` parameter instead.

## Declaration

```swift
nonisolated
func dropDestination<T>(for payloadType: T.Type = T.self, action: @escaping ([T], CGPoint) -> Bool, isTargeted: @escaping (Bool) -> Void = { _ in }) -> some View where T : Transferable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/dropdestination(for:action:istargeted:))*