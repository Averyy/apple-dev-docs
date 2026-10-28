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
init<S>(_ title: S, image: Image) where S : StringProtocol
```

Available when `Image` conforms to `Transferable` and `Icon` is `Never`.

**Other overloads**:

```swift
@export(implementation)
init(_ titleResource: LocalizedStringResource, image: Image)
```

```swift
init(_ title: Text, image: Image)
```

```swift
init(_ titleKey: LocalizedStringKey, image: Image)
```

## Parameters

- `title`: A title to show in a preview.
- `image`: An image to show in a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharepreview/init(_:image:)-91j4s)*