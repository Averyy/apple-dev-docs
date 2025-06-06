# init(content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a tab view that uses a builder to create its tabs.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init<C>(@TabContentBuilder<Never> content: () -> C) where SelectionValue == Never, Content == TabContentBuilder<Never>.Content<C>, C : TabContent
```

## Parameters

- `content`: The   content.

## See Also

- [init(selection:content:)](tabview/init(selection:content:).md)
  Creates a tab view that uses a builder to create and specify selection values for its tabs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabview/init(content:))*