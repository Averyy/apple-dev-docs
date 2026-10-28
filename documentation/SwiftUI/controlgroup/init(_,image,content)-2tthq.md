# init(_:image:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new control group with the specified content that generates its label from a localized string key and image resource.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<C>(_ titleKey: LocalizedStringKey, image: ImageResource, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View
```

Available when `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<C>(_ titleResource: LocalizedStringResource, image: ImageResource, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View
```

```swift
nonisolated
init<C, S>(_ title: S, image: ImageResource, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View, S : StringProtocol
```

## Parameters

- `titleKey`: The key for the group’s localized title, that describes the contents of the group.
- `image`: The name of the image resource to look up.
- `content`: The content to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroup/init(_:image:content:)-2tthq)*