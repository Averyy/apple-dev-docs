# init(_:action:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button that generates its label from a localized string resource.

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
@preconcurrency
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, action: @escaping @MainActor () -> Void)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf. See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `titleResource`: Text resource for the button’s localized title, that describes the purpose of the button’s `action`.
- `action`: The action to perform when the user triggers the button.

## See Also

- [init(action: () -> Void, label: () -> Label)](button/init(action:label:).md)
  Creates a button that displays a custom label.
- [init(_:image:action:)](button/init(_:image:action:).md)
  Creates a button that generates its label from a localized string resource and image resource.
- [init(_:systemImage:action:)](button/init(_:systemimage:action:).md)
  Creates a button that generates its label from a localized string key and system image name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:action:))*