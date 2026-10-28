# init(_:isOn:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a toggle that generates its label from a localized string resource.

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
nonisolated init(_ titleResource: LocalizedStringResource, isOn: Binding<Bool>)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, isOn: Binding<Bool>)
```

```swift
nonisolated
init<S>(_ title: S, isOn: Binding<Bool>) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See `Text` for more information about localizing strings.

## Parameters

- `titleResource`: Text resource for the toggle’s localized title, that describes the purpose of the toggle.
- `isOn`: A binding to a property that indicates whether the toggle is on or off.

## See Also

### Creating a toggle
- [init(isOn: Binding<Bool>, label: () -> Label)](./init%28ison,label%29.md)
  Creates a toggle that displays a custom label.
- [init(_:image:isOn:)](./init%28_,image,ison%29.md)
  Creates a toggle that generates its label from a localized string resource and image resource.
- [init(_:systemImage:isOn:)](./init%28_,systemimage,ison%29.md)
  Creates a toggle that generates its label from a localized string key and system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:ison:))*