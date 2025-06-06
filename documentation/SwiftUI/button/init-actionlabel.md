# init(action:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button that displays a custom label.

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
@preconcurrency
init(action: @escaping @MainActor () -> Void, @ViewBuilder label: () -> Label)
```

## Parameters

- `action`: The action to perform when the user triggers the button.
- `label`: A view that describes the purpose of the button’s  .

## See Also

- [init(_:action:)](button/init(_:action:).md)
  Creates a button that generates its label from a localized string key.
- [init(_:image:action:)](button/init(_:image:action:).md)
  Creates a button that generates its label from a localized string key and image resource.
- [init(_:systemImage:action:)](button/init(_:systemimage:action:).md)
  Creates a button that generates its label from a localized string key and system image name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(action:label:))*