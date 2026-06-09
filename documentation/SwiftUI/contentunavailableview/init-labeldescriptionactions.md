# init(label:description:actions:)

**Framework**: SwiftUI  
**Kind**: init

Creates an interface, consisting of a label and additional content, that you display when the content of your app is unavailable to users.

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
init(@ContentBuilder label: () -> Label, @ContentBuilder description: () -> Description = { EmptyView() }, @ContentBuilder actions: () -> Actions = { EmptyView() })
```

## Parameters

- `label`: The label that describes the view.
- `description`: The view that describes the interface.
- `actions`: The content of the interface actions.

## See Also

- [init(_:image:description:)](contentunavailableview/init(_:image:description:).md)
  Creates an interface, consisting of a title generated from a localized string, an image and additional content, that you display when the content of your app is unavailable to users.
- [init(_:systemImage:description:)](contentunavailableview/init(_:systemimage:description:).md)
  Creates an interface, consisting of a title generated from a localized string, a system icon image and additional content, that you display when the content of your app is unavailable to users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentunavailableview/init(label:description:actions:))*