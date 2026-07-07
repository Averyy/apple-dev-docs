# init(_:systemImage:)

**Framework**: SwiftUI  
**Kind**: init

Creates a label with a system icon image and a title generated from a localized string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage name: String)
```

## Parameters

- `titleResource`: A title generated from a localized string.

## See Also

- [init(_:image:)](label/init(_:image:).md)
  Creates a label with an icon image and a title generated from a localized string.
- [init(title: () -> Title, icon: () -> Icon)](label/init(title:icon:).md)
  Creates a label with a custom title and icon.
- [init(_:)](label/init(_:).md)
  Creates a label representing a family activity application.
- [init(_:image:)](label/init(_:image:).md)
  Creates a label with an icon image and a title generated from a localized string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/label/init(_:systemimage:))*