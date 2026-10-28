# init(_:systemImage:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new control group with the specified content that generates its label from a localized string key and image name.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init<C>(_ titleKey: LocalizedStringKey, systemImage: String, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View
```

Available when `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<C, S>(_ title: S, systemImage: String, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View, S : StringProtocol
```

```swift
@export(implementation)
nonisolated init<C>(_ titleResource: LocalizedStringResource, systemImage: String, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View
```

## Parameters

- `titleKey`: The key for the group’s localized title, that describes the contents of the group.
- `systemImage`: The name of the image resource to lookup.
- `content`: The content to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroup/init(_:systemimage:content:)-7x2jd)*