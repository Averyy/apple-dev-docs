# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a labeled view that generates its label from a localized string key.

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
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```

Available when `Label` is `Text` and `Content` conforms to `View`.

**Other overloads**:

```swift
init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content)
```

```swift
init<S>(_ title: S, @ContentBuilder content: () -> Content) where S : StringProtocol
```

#### Discussion

This initializer creates a [`Text`](../text.md) label on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See `Text` for more information about localizing strings.

## Parameters

- `titleKey`: The key for the view’s localized title, that describes the purpose of the view.
- `content`: The value content being labeled.

## See Also

### Creating labeled content
- [init(content: () -> Content, label: () -> Label)](./init%28content,label%29.md)
  Creates a standard labeled element, with a view that conveys the value of the element and a label.
- [init(_:value:)](./init%28_,value%29.md)
  Creates a labeled informational view.
- [init(_:value:format:)](./init%28_,value,format%29.md)
  Creates a labeled informational view from a formatted value.
- [init(LabeledContentStyleConfiguration)](./init%28_%29.md)
  Creates labeled content based on a labeled content style configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:content:))*