# init(_:id:)

**Framework**: SwiftUI  
**Kind**: init

Create an `AccessibilityCustomContentKey` with the specified label and identifier.

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
init(_ label: Text, id: String)
```

## Parameters

- `label`: Localized text describing to the user what   is contained in this additional information entry. For example:   “orientation”.
- `id`: String used to identify the additional information entry   to SwiftUI. Adding an entry will replace any previous value with the   same identifier.

## See Also

- [init(LocalizedStringKey)](accessibilitycustomcontentkey/init(_:).md)
  Create an `AccessibilityCustomContentKey` with the specified label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitycustomcontentkey/init(_:id:))*