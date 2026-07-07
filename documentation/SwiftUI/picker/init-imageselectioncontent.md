# init(_:image:selection:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a picker that generates its label from a localized string resource and image resource

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
nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf. See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `titleResource`: A localized string resource that describes the purpose of selecting an option.
- `image`: The name of the image resource to lookup.
- `selection`: A binding to a property that determines the currently-selected option.
- `content`: A view that contains the set of options.

## See Also

- [init(_:image:sources:selection:content:)](picker/init(_:image:sources:selection:content:).md)
  Creates a picker that generates its label from a localized string resource and image resource.
- [init(_:systemImage:selection:content:)](picker/init(_:systemimage:selection:content:).md)
  Creates a picker that generates its label from a localized string key and system image.
- [init(_:systemImage:sources:selection:content:)](picker/init(_:systemimage:sources:selection:content:).md)
  Creates a picker bound to a collection of bindings that generates its label from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:image:selection:content:))*