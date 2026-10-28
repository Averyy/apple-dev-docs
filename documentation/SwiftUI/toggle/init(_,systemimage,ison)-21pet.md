# init(_:systemImage:isOn:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a toggle that generates its label from a localized string resource and system image.

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
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, isOn: Binding<Bool>)
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, isOn: Binding<Bool>)
```

```swift
@export(implementation)
nonisolated init<S>(_ title: S, systemImage: String, isOn: Binding<Bool>) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See `Text` for more information about localizing strings.

## Parameters

- `titleResource`: Text resource for the toggle’s localized title, that describes the purpose of the toggle.
- `systemImage`: The name of the image resource to lookup.
- `isOn`: A binding to a property that indicates whether the toggle is on or off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:systemimage:ison:)-21pet)*