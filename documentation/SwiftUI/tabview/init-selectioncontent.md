# init(selection:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a tab view that uses a builder to create and specify selection values for its tabs.

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
init<C>(selection: Binding<SelectionValue>, @TabContentBuilder<SelectionValue> content: () -> C) where Content == TabContentBuilder<SelectionValue>.Content<C>, C : TabContent
```

## Parameters

- `selection`: The selection in the TabView. The value of this   binding must match the   of the tabs in  .
- `content`: The   content.

## See Also

- [init(content:)](tabview/init(content:).md)
  Creates a tab view that uses a builder to create its tabs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabview/init(selection:content:))*