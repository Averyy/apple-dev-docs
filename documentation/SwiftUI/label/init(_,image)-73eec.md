# init(_:image:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a label with an icon image and a title generated from a localized string.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image name: String)
```

Available when `Title` is `Text` and `Icon` is `Image`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image name: String)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image resource: ImageResource)
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

- `titleKey`: A title generated from a localized string.
- `name`: The name of the image resource to lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/label/init(_:image:)-73eec)*