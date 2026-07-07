# init(_:systemImage:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new control group with the specified content that generates its label from a string and image name.

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
nonisolated init<C, S>(_ title: S, systemImage: String, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View, S : StringProtocol
```

## Parameters

- `title`: A string that describes the contents of the group.
- `systemImage`: The name of the image resource to lookup.

## See Also

- [init(_:image:content:)](controlgroup/init(_:image:content:).md)
  Creates a new control group with the specified content that generates its label from a localized string resource and image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroup/init(_:systemimage:content:))*