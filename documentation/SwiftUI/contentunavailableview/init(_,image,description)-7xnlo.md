# init(_:image:description:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an interface, consisting of a title generated from a string, an image and additional content, that you display when the content of your app is unavailable to users.

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
init<S>(_ title: S, image name: String, description: Text? = nil) where S : StringProtocol
```

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and `Actions` is `EmptyView`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ title: LocalizedStringResource, image name: String, description: Text? = nil)
```

```swift
nonisolated
init(_ title: LocalizedStringKey, image name: String, description: Text? = nil)
```

## Parameters

- `title`: A string used as the title.
- `name`: The name of the image resource to lookup.
- `description`: The view that describes the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentunavailableview/init(_:image:description:)-7xnlo)*