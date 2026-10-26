---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/accessibilityrotor(_:entries:entryid:entrylabel:)-9iz29"
framework: "CareKit/CareKitUI"
---

# accessibilityRotor(_:entries:entryID:entryLabel:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.accessibilityRotor(_:entries:entryID:entryLabel:)`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityRotor<EntryModel, ID>(_ systemRotor: AccessibilitySystemRotor, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View where ID : Hashable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/accessibilityrotor(_:entries:entryid:entrylabel:)-9iz29)*