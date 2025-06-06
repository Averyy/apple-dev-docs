# allowsSelection

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the selectability type allows selection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static var allowsSelection: Bool { get }
```

#### Discussion

Conforming types, such as [`EnabledTextSelectability`](enabledtextselectability.md) and [`DisabledTextSelectability`](disabledtextselectability.md), return `true` or `false` for this property as appropriate. SwiftUI expects this value for a given selectability type to be constant, unaffected by global state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textselectability/allowsselection)*