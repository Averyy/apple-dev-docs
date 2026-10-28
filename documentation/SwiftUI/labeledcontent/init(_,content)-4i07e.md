# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a labeled view that generates its label from a localized string resource.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content)
```

Available when `Label` is `Text` and `Content` conforms to `View`.

**Other overloads**:

```swift
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```

```swift
init<S>(_ title: S, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) label on your behalf. See `Text` for more information about localizing strings.

## Parameters

- `titleResource`: Text resource for the view’s localized title, that describes the purpose of the view.
- `content`: The value content being labeled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:content:)-4i07e)*