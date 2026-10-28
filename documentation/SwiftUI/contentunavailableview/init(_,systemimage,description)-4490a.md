# init(_:systemImage:description:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an interface, consisting of a title generated from a localized string, a system icon image and additional content, that you display when the content of your app is unavailable to users.

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
init(_ title: LocalizedStringKey, systemImage name: String, description: Text? = nil)
```

Available when `Label` is `Label<Text, Image>`, `Description` is `Text?`, and `Actions` is `EmptyView`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ title: LocalizedStringResource, systemImage name: String, description: Text? = nil)
```

```swift
nonisolated
init<S>(_ title: S, systemImage name: String, description: Text? = nil) where S : StringProtocol
```

## Parameters

- `title`: A title generated from a localized string.
- `name`: The name of the system symbol image resource to lookup. Use the SF Symbols app to look up the names of system symbol images.
- `description`: The view that describes the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentunavailableview/init(_:systemimage:description:)-4490a)*