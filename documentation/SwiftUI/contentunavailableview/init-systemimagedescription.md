# init(_:systemImage:description:)

**Framework**: SwiftUI  
**Kind**: init

Creates an interface, consisting of a title generated from a localized string, a system icon image and additional content, that you display when the content of your app is unavailable to users.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(_ title: LocalizedStringKey, systemImage name: String, description: Text? = nil)
```

## Parameters

- `title`: A title generated from a localized string.
- `description`: The view that describes the interface.

## See Also

- [init(label: () -> Label, description: () -> Description, actions: () -> Actions)](contentunavailableview/init(label:description:actions:).md)
  Creates an interface, consisting of a label and additional content, that you display when the content of your app is unavailable to users.
- [init(_:image:description:)](contentunavailableview/init(_:image:description:).md)
  Creates an interface, consisting of a title generated from a localized string, an image and additional content, that you display when the content of your app is unavailable to users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentunavailableview/init(_:systemimage:description:))*