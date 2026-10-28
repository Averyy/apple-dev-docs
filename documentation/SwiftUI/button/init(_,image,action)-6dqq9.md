# init(_:image:action:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button that generates its label from a localized string key and image resource.

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
@preconcurrency
nonisolated init(_ titleKey: LocalizedStringKey, image: ImageResource, action: @escaping @MainActor () -> Void)
```

Available when `Label` is `Label<Text, Image>`.

**Other overloads**:

```swift
@preconcurrency
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, action: @escaping @MainActor () -> Void)
```

```swift
@preconcurrency
nonisolated init<S>(_ title: S, image: ImageResource, action: @escaping @MainActor () -> Void) where S : StringProtocol
```

## Discussion

This initializer creates a [`Label`](../label.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleKey`: The key for the button’s localized title, that describes the purpose of the button’s `action`.
- `image`: The image resource to lookup.
- `action`: The action to perform when the user triggers the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:image:action:)-6dqq9)*