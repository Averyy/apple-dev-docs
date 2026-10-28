# init(_:image:role:intent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button with a specified role that performs an `AppIntent` and generates its label from a localized string resource and an image resource.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(_ titleResource: LocalizedStringResource, image: ImageResource, role: ButtonRole? = nil, intent: some AppIntent)
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
nonisolated
init(_ title: some StringProtocol, image: ImageResource, role: ButtonRole? = nil, intent: some AppIntent)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: ImageResource, role: ButtonRole? = nil, intent: some AppIntent)
```

## Discussion

This initializer creates a [`Label`](../label.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleResource`: The button’s localized title, that describes the purpose of the button’s `intent`.
- `image`: The image resource to lookup.
- `role`: An optional semantic role describing the button. A value of `nil` means that the button doesn’t have an assigned role.
- `intent`: The `AppIntent` to execute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:image:role:intent:)-4729z)*