# init(_:systemImage:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a label with a system icon image and a title generated from a string.

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
init<S>(_ title: S, systemImage name: String) where S : StringProtocol
```

Available when `Title` is `Text` and `Icon` is `Image`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage name: String)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, systemImage name: String)
```

## Parameters

- `title`: A string used as the label’s title.
- `name`: The name of the image resource to lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/label/init(_:systemimage:)-2z97t)*