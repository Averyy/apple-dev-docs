# init(_:id:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Create an `AccessibilityCustomContentKey` with the specified label and identifier.

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
@export(implementation)
init(_ label: LocalizedStringResource, id: String)
```

**Other overloads**:

```swift
init(_ label: Text, id: String)
```

```swift
init(_ labelKey: LocalizedStringKey, id: String)
```

## Parameters

- `label`: Localized text describing to the user what is contained in this additional information entry. For example: “orientation”.
- `id`: String used to identify the additional information entry to SwiftUI. Adding an entry will replace any previous value with the same identifier.

## See Also

### Creating a key
- [init(_:)](./init%28_%29.md)
  Create an `AccessibilityCustomContentKey` with the specified label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitycustomcontentkey/init(_:id:))*