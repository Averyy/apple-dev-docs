# init(_:image:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a preview representation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
init(_ titleResource: LocalizedStringResource, image: Image)
```

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

**Other overloads**:

```swift
init(_ title: Text, image: Image)
```

```swift
init(_ titleKey: LocalizedStringKey, image: Image)
```

```swift
init<S>(_ title: S, image: Image) where S : StringProtocol
```

## Parameters

- `titleResource`: A resource for the title to show in a preview.
- `image`: An image to show in a preview.

## See Also

### Creating a preview
- [init(_:)](./init%28_%29.md)
  Creates a preview representation.
- [init(_:icon:)](./init%28_,icon%29.md)
  Creates a preview representation.
- [init(_:image:icon:)](./init%28_,image,icon%29.md)
  Creates a preview representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharepreview/init(_:image:))*