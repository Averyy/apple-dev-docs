# init(content:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a standard labeled element, with a view that conveys the value of the element and a label.

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
nonisolated
init(@ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

Available when `Label` conforms to `View` and `Content` conforms to `View`.

## Parameters

- `content`: The view that conveys the value of the resulting labeled element.
- `label`: The label that describes the purpose of the result.

## See Also

### Creating labeled content
- [init(_:content:)](./init%28_,content%29.md)
  Creates a labeled view that generates its label from a localized string key.
- [init(_:value:)](./init%28_,value%29.md)
  Creates a labeled informational view.
- [init(_:value:format:)](./init%28_,value,format%29.md)
  Creates a labeled informational view from a formatted value.
- [init(LabeledContentStyleConfiguration)](./init%28_%29.md)
  Creates labeled content based on a labeled content style configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontent/init(content:label:))*