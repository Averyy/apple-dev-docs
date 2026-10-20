# init(_:image:icon:)

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
init(_ titleResource: LocalizedStringResource, image: Image, icon: Icon)
```

**Other overloads**:

```swift
init(_ title: Text, image: Image, icon: Icon)
```

```swift
init(_ titleKey: LocalizedStringKey, image: Image, icon: Icon)
```

```swift
init<S>(_ title: S, image: Image, icon: Icon) where S : StringProtocol
```

## Parameters

- `titleResource`: A resource for the title to show in a preview.
- `image`: An image to show in a preview.
- `icon`: An icon to show in a preview.

## See Also

### Creating a preview
- [init(_:)](./init%28_%29.md)
  Creates a preview representation.
- [init(_:image:)](./init%28_,image%29.md)
  Creates a preview representation.
- [init(_:icon:)](./init%28_,icon%29.md)
  Creates a preview representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharepreview/init(_:image:icon:))*