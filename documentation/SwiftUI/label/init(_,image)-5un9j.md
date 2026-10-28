# init(_:image:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a label with an icon image and a title generated from a localized string.

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
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image resource: ImageResource)
```

Available when `Title` is `Text` and `Icon` is `Image`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image name: String)
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
- `resource`: The image resource to lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/label/init(_:image:)-5un9j)*