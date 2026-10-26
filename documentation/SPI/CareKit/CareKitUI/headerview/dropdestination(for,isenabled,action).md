---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/dropdestination(for:isenabled:action:)"
framework: "CareKit/CareKitUI"
---

# dropDestination(for:isEnabled:action:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.dropDestination(for:isEnabled:action:)`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func dropDestination<T>(for type: T.Type = T.self, isEnabled: Bool = true, action: @escaping ([T], DropSession) -> Void) -> some View where T : Transferable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/dropdestination(for:isenabled:action:))*