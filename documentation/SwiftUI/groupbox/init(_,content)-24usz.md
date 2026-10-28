# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a group box with the provided view content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, @ContentBuilder content: () -> Content) where S : StringProtocol
```

Available when `Label` is `Text` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```

## Parameters

- `title`: A string that describes the content of the group box.
- `content`: A [`ContentBuilder`](../contentbuilder.md) that produces the content for the group box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupbox/init(_:content:)-24usz)*