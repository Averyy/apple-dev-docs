---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/accessibilityrotor(_:entries:entryid:entrylabel:)-7z9ma"
framework: "CareKit/CareKitUI"
---

# accessibilityRotor(_:entries:entryID:entryLabel:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.accessibilityRotor(_:entries:entryID:entryLabel:)`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accessibilityRotor<EntryModel, ID>(_ rotorLabelResource: LocalizedStringResource, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View where ID : Hashable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/linkview/accessibilityrotor(_:entries:entryid:entrylabel:)-7z9ma)*