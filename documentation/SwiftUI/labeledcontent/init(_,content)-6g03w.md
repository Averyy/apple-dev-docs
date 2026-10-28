# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a labeled view that generates its label from a string.

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
init<S>(_ title: S, @ContentBuilder content: () -> Content) where S : StringProtocol
```

Available when `Label` is `Text` and `Content` conforms to `View`.

**Other overloads**:

```swift
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```

```swift
init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content)
```

## Discussion

This initializer creates a [`Text`](../text.md) label on your behalf, and treats the title similar to [`init(_:)`](../text/init%28_%29.md). See `Text` for more information about localizing strings.

## Parameters

- `title`: A string that describes the purpose of the view.
- `content`: The value content being labeled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:content:)-6g03w)*