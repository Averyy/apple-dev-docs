# init(_:image:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a label with an icon image and a title generated from a localized string.

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
nonisolated init(_ titleResource: LocalizedStringResource, image name: String)
```

Available when `Title` is `Text` and `Icon` is `Image`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image resource: ImageResource)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image name: String)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image resource: ImageResource)
```

```swift
nonisolated
init<S>(_ title: S, image name: String) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, image resource: ImageResource) where S : StringProtocol
```

## Parameters

- `titleResource`: A title generated from a localized string.
- `name`: The name of the image resource to lookup.

## See Also

### Creating a label
- [init(_:systemImage:)](./init%28_,systemimage%29.md)
  Creates a label with a system icon image and a title generated from a localized string.
- [init(title: () -> Title, icon: () -> Icon)](./init%28title,icon%29.md)
  Creates a label with a custom title and icon.
- [init(_:)](./init%28_%29.md)
  Creates a label representing a family activity application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/label/init(_:image:))*