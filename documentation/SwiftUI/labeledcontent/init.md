# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates labeled content based on a labeled content style configuration.

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
init(_ configuration: LabeledContentStyleConfiguration)
```

#### Discussion

You can use this initializer within the [`makeBody(configuration:)`](labeledcontentstyle/makebody(configuration:).md) method of a [`LabeledContentStyle`](labeledcontentstyle.md) to create a labeled content instance. This is useful for custom styles that only modify the current style, as opposed to implementing a brand new style.

For example, the following style adds a red border around the labeled content, but otherwise preserves the current style:

```swift
struct RedBorderLabeledContentStyle: LabeledContentStyle {
    func makeBody(configuration: Configuration) -> some View {
        LabeledContent(configuration)
            .border(.red)
    }
}
```

## Parameters

- `configuration`: The properties of the labeled content

## See Also

- [init(_:content:)](labeledcontent/init(_:content:).md)
  Creates a labeled view that generates its label from a localized string key.
- [init(content: () -> Content, label: () -> Label)](labeledcontent/init(content:label:).md)
  Creates a standard labeled element, with a view that conveys the value of the element and a label.
- [init(_:value:)](labeledcontent/init(_:value:).md)
  Creates a labeled informational view.
- [init(_:value:format:)](labeledcontent/init(_:value:format:).md)
  Creates a labeled informational view from a formatted value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:))*