# init(_:id:in:textRange:prepare:)

**Framework**: SwiftUI  
**Kind**: init

Create a Rotor entry with a specific label, identifier and namespace, and with an optional range.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(_ label: LocalizedStringResource, id: ID, in namespace: Namespace.ID, textRange: Range<String.Index>? = nil, prepare: @escaping () -> Void = {})
```

## Parameters

- `label`: Localized string used to show this Rotor entry   to users.
- `id`: Used to find the UI element associated with this   Rotor entry. This identifier and namespace should match a call to   .
- `namespace`: Namespace for this identifier. Should match a call   to  .
- `textRange`: Optional range of text associated with this Rotor   entry. This should be a range within text that is set as the   accessibility label or accessibility value of the associated   element.
- `prepare`: Optional closure to run before a Rotor entry   is navigated to, to prepare the UI as needed. This should be used to   bring the Accessibility element on-screen, if scrolling is needed to   get to it.

## See Also

- [init<L>(L, ID, in: Namespace.ID, textRange: Range<String.Index>?, prepare: () -> Void)](accessibilityrotorentry/init(_:_:in:textrange:prepare:).md)
  Create a Rotor entry with a specific label, identifier and namespace, and with an optional range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityrotorentry/init(_:id:in:textrange:prepare:))*