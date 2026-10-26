---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/onscrolltargetvisibilitychange(idtype:threshold:_:)"
framework: "CareKit/CareKitUI"
---

# onScrollTargetVisibilityChange(idType:threshold:_:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.onScrollTargetVisibilityChange(idType:threshold:_:)`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double = 0.5, _ action: @escaping ([ID]) -> Void) -> some View where ID : Hashable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/onscrolltargetvisibilitychange(idtype:threshold:_:))*