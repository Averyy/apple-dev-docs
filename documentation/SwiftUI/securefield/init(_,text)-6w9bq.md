# init(_:text:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a secure field with a prompt generated from a `Text`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@export(implementation)
nonisolated init<S>(_ title: S, text: Binding<String>) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, text: Binding<String>)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, text: Binding<String>)
```

## Discussion

Use the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) modifier to invoke an action whenever someone submits this secure field — for example, by pressing the Return key.

## Parameters

- `title`: A string that describes the purpose of the field.
- `text`: A binding to the text that the field displays and edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/securefield/init(_:text:)-6w9bq)*