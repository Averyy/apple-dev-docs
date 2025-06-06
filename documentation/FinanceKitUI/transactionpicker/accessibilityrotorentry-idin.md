# accessibilityRotorEntry(id:in:)

**Framework**: FinanceKitUI  
**Kind**: method

Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.

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
func accessibilityRotorEntry<ID>(id: ID, in namespace: Namespace.ID) -> some View where ID : Hashable
```

#### Discussion

Use this when creating an AccessibilityRotorEntry without a namespace does not allow SwiftUI to automatically find and reveal the element, or when the Rotor entry should be associated with a sub-element of a complex view generated in a ForEach, for example.

## Parameters

- `id`: An arbitrary hashable identifier. Pass this same value   when initializing an AccessibilityRotorEntry.
- `namespace`: A namespace created with  . Pass this   same namespace when initializing an  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/accessibilityrotorentry(id:in:))*