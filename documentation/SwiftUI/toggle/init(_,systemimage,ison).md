# init(_:systemImage:isOn:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a toggle that generates its label from a localized string key and system image.

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
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, isOn: Binding<Bool>)
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, isOn: Binding<Bool>)
```

```swift
@export(implementation)
nonisolated init<S>(_ title: S, systemImage: String, isOn: Binding<Bool>) where S : StringProtocol
```

#### Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See `Text` for more information about localizing strings.

## Parameters

- `titleKey`: The key for the toggle’s localized title, that describes the purpose of the toggle.
- `systemImage`: The name of the image resource to lookup.
- `isOn`: A binding to a property that indicates whether the toggle is on or off.

## See Also

### Creating a toggle
- [init(_:isOn:)](./init%28_,ison%29.md)
  Creates a toggle that generates its label from a localized string resource.
- [init(isOn: Binding<Bool>, label: () -> Label)](./init%28ison,label%29.md)
  Creates a toggle that displays a custom label.
- [init(_:image:isOn:)](./init%28_,image,ison%29.md)
  Creates a toggle that generates its label from a localized string resource and image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:systemimage:ison:))*