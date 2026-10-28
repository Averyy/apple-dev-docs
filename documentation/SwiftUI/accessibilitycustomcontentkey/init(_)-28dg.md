# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Create an `AccessibilityCustomContentKey` with the specified label.

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
init(_ labelKey: LocalizedStringKey)
```

**Other overloads**:

```swift
init(_ label: LocalizedStringResource)
```

## Parameters

- `labelKey`: Localized text describing to the user what is contained in this additional information entry. For example: “orientation”. This will also be used as the identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitycustomcontentkey/init(_:)-28dg)*