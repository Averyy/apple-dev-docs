# init(_:systemImage:selection:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a picker that generates its label from a localized string key and system image.

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
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to `Hashable`, and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

```swift
@export(implementation)
nonisolated init<S>(_ title: S, systemImage: String, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleKey`: A localized string key that describes the purpose of selecting an option.
- `systemImage`: The name of the image resource to lookup.
- `selection`: A binding to a property that determines the currently-selected option.
- `content`: A view that contains the set of options.

## See Also

### Creating a picker with an image label
- [init(_:image:selection:content:)](./init%28_,image,selection,content%29.md)
  Creates a picker that generates its label from a localized string resource and image resource
- [init(_:image:sources:selection:content:)](./init%28_,image,sources,selection,content%29.md)
  Creates a picker that generates its label from a localized string resource and image resource.
- [init(_:systemImage:sources:selection:content:)](./init%28_,systemimage,sources,selection,content%29.md)
  Creates a picker bound to a collection of bindings that generates its label from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:systemimage:selection:content:))*