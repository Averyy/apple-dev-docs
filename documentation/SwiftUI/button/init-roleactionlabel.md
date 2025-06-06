# init(role:action:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button with a specified role that displays a custom label.

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
@preconcurrency
nonisolated init(role: ButtonRole?, action: @escaping @MainActor () -> Void, @ViewBuilder label: () -> Label)
```

## Parameters

- `role`: An optional semantic role that describes the button. A value of    means that the button doesn’t have an assigned role.
- `action`: The action to perform when the user interacts with the button.
- `label`: A view that describes the purpose of the button’s  .

## See Also

- [init(_:role:action:)](button/init(_:role:action:).md)
  Creates a button with a specified role that generates its label from a localized string key.
- [init(_:image:role:action:)](button/init(_:image:role:action:).md)
  Creates a button with a specified role that generates its label from a localized string key and an image resource.
- [init(_:systemImage:role:action:)](button/init(_:systemimage:role:action:).md)
  Creates a button with a specified role that generates its label from a localized string key and a system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(role:action:label:))*