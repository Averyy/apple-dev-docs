# init(_:image:isOn:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a toggle that generates its label from a localized string key and image resource.

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
init(_ titleKey: LocalizedStringKey, image: ImageResource, isOn: Binding<Bool>)
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, isOn: Binding<Bool>)
```

```swift
nonisolated
init<S>(_ title: S, image: ImageResource, isOn: Binding<Bool>) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See `Text` for more information about localizing strings.

## Parameters

- `titleKey`: The key for the toggle’s localized title, that describes the purpose of the toggle.
- `image`: The name of the image resource to lookup.
- `isOn`: A binding to a property that indicates whether the toggle is on or off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:image:ison:)-4o679)*