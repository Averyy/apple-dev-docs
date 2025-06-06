# TabContentBuilder

**Framework**: SwiftUI  
**Kind**: struct

A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.

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
@resultBuilder
struct TabContentBuilder<TabValue> where TabValue : Hashable
```

## Topics

### Structures
- [TabContentBuilder.Content](tabcontentbuilder/content.md)
  A view representation of the content of a builder-based tab view with selection.
### Type Methods
- [static func buildBlock(some TabContent<TabValue>) -> some TabContent<TabValue>
](tabcontentbuilder/buildblock(_:).md)
- [static func buildBlock<C0, C1>(C0, C1) -> some TabContent<TabValue>
](tabcontentbuilder/buildblock(_:_:).md)
- [static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some TabContent<TabValue>
](tabcontentbuilder/buildblock(_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some TabContent<TabValue>
](tabcontentbuilder/buildblock(_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some TabContent<TabValue>
](tabcontentbuilder/buildblock(_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) -> some TabContent<TabValue>
](tabcontentbuilder/buildblock(_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5, C6) -> some TabContent<TabValue>
](tabcontentbuilder/buildblock(_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4, C5, C6, C7) -> some TabContent<TabValue>
](tabcontentbuilder/buildblock(_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3, C4, C5, C6, C7, C8) -> some TabContent<TabValue>
](tabcontentbuilder/buildblock(_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9) -> some TabContent<TabValue>
](tabcontentbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](tabcontentbuilder/buildeither(first:).md)
- [static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>](tabcontentbuilder/buildeither(second:).md)
- [static func buildExpression(some TabContent<TabValue>) -> some TabContent<TabValue>
](tabcontentbuilder/buildexpression(_:).md)
- [static func buildIf((some TabContent<TabValue>)?) -> (some TabContent<TabValue>)?
](tabcontentbuilder/buildif(_:).md)
- [static func buildLimitedAvailability<T>(T) -> AnyTabContent<T.TabValue>](tabcontentbuilder/buildlimitedavailability(_:).md)

## See Also

- [func sectionActions<Content>(content: () -> Content) -> some View](view/sectionactions(content:).md)
  Adds custom actions to a section.
- [struct TabPlacement](tabplacement.md)
  A place that a tab can appear.
- [protocol TabContent](tabcontent.md)
  A type that provides content for programmatically selectable tabs in a tab view.
- [struct AnyTabContent](anytabcontent.md)
  Type erased tab content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontentbuilder)*