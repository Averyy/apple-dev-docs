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
init<S>(_ title: S, image: Image, icon: Icon) where S : StringProtocol
```

**Other overloads**:

```swift
@export(implementation)
init(_ titleResource: LocalizedStringResource, image: Image, icon: Icon)
```

```swift
init(_ title: Text, image: Image, icon: Icon)
```

```swift
init(_ titleKey: LocalizedStringKey, image: Image, icon: Icon)
```

## Parameters

- `title`: A title to show in a preview.
- `image`: An image to show in a preview.
- `icon`: An icon to show in a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharepreview/init(_:image:icon:)-39xn8)*