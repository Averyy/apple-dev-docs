# init(_:image:selection:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to `Hashable`, and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: ImageResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init<S>(_ title: S, image: ImageResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleResource`: A localized string resource that describes the purpose of selecting an option.
- `image`: The name of the image resource to lookup.
- `selection`: A binding to a property that determines the currently-selected option.
- `content`: A view that contains the set of options.

## See Also

### Creating a picker with an image label
- [init(_:image:sources:selection:content:)](./init%28_,image,sources,selection,content%29.md)
  Creates a picker that generates its label from a localized string resource and image resource.
- [init(_:systemImage:selection:content:)](./init%28_,systemimage,selection,content%29.md)
  Creates a picker that generates its label from a localized string key and system image.
- [init(_:systemImage:sources:selection:content:)](./init%28_,systemimage,sources,selection,content%29.md)
  Creates a picker bound to a collection of bindings that generates its label from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:image:selection:content:))*