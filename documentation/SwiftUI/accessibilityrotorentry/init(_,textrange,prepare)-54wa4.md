# init(_:textRange:prepare:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Create a Rotor entry with a specific label and range. This Rotor entry will be associated with the Accessibility element that owns the Rotor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(_ label: Text? = nil, textRange: Range<String.Index>, prepare: @escaping () -> Void = {}) where ID == Never
```

**Other overloads**:

```swift
@export(implementation)
init(_ label: LocalizedStringResource, textRange: Range<String.Index>, prepare: @escaping () -> Void = {}) where ID == Never
```

```swift
init(_ labelKey: LocalizedStringKey, textRange: Range<String.Index>, prepare: @escaping () -> Void = {})
```

```swift
init<L>(_ label: L, textRange: Range<String.Index>, prepare: @escaping () -> Void = {}) where ID == Never, L : StringProtocol
```

## Parameters

- `label`: Optional localized string used to show this Rotor entry to users. If no label is specified, the Rotor entry will be labeled based on the text at that range.
- `textRange`: Range of text associated with this Rotor entry.
- `prepare`: Optional closure to run before a Rotor entry is navigated to, to prepare the UI as needed. This can be used to bring the UI element or text on-screen if it isn’t already, and SwiftUI not able to automatically scroll to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityrotorentry/init(_:textrange:prepare:)-54wa4)*