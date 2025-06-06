# init(content:label:)

**Framework**: SwiftUI  
**Kind**: init

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
init(@ViewBuilder content: () -> Content, @ViewBuilder label: () -> Label)
```

## Parameters

- `content`: The view that conveys the value of the resulting labeled   element.
- `label`: The label that describes the purpose of the result.

## See Also

- [init(_:content:)](labeledcontent/init(_:content:).md)
  Creates a labeled view that generates its label from a localized string key.
- [init(_:value:)](labeledcontent/init(_:value:).md)
  Creates a labeled informational view.
- [init(_:value:format:)](labeledcontent/init(_:value:format:).md)
  Creates a labeled informational view from a formatted value.
- [init(LabeledContentStyleConfiguration)](labeledcontent/init(_:).md)
  Creates labeled content based on a labeled content style configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontent/init(content:label:))*