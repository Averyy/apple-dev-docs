# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Create an `AccessibilityCustomContentKey` with the specified label.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(_ label: LocalizedStringResource)
```

**Other overloads**:

```swift
init(_ labelKey: LocalizedStringKey)
```

## Parameters

- `label`: Localized text describing to the user what is contained in this additional information entry. For example: “orientation”. This will also be used as the identifier.

## See Also

### Creating a key
- [init(_:id:)](./init%28_,id%29.md)
  Create an `AccessibilityCustomContentKey` with the specified label and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitycustomcontentkey/init(_:))*