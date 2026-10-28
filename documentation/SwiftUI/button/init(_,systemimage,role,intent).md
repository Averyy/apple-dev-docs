# init(_:systemImage:role:intent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button with a specified role that generates its label from a string and a system image.

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
init(_ title: some StringProtocol, systemImage: String, role: ButtonRole? = nil, intent: some AppIntent)
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, systemImage: String, role: ButtonRole? = nil, intent: some AppIntent)
```

```swift
nonisolated
init(_ titleResource: LocalizedStringResource, systemImage: String, role: ButtonRole? = nil, intent: some AppIntent)
```

## Discussion

This initializer creates a [`Label`](../label.md) view on your behalf, and treats the title similar to [`init(_:)`](../text/init%28_%29-9d1g4.md). See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `title`: A string that describes the purpose of the button’s `intent`.
- `systemImage`: The name of the image resource to lookup.
- `role`: An optional semantic role describing the button. A value of `nil` means that the button doesn’t have an assigned role.
- `intent`: The `AppIntent` to execute.

## See Also

### Creating a button to perform an App Intent
- [init(_:intent:)](./init%28_,intent%29.md)
  Creates a button that performs an `AppIntent` and generates its label from a localized string key.
- [init<I>(intent: I, label: () -> Label)](./init%28intent,label%29.md)
  Creates a button that performs an `AppIntent`.
- [init(_:role:intent:)](./init%28_,role,intent%29.md)
  Creates a button with a specified role that performs an `AppIntent` and generates its label from a string.
- [init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)](./init%28role,intent,label%29.md)
  Creates a button with a specified role that performs an `AppIntent`.
- [init(_:image:role:intent:)](./init%28_,image,role,intent%29.md)
  Creates a button with a specified role that generates its label from a string and an image resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:systemimage:role:intent:))*