# EntityQuerySortingOptionsBuilder

**Framework**: App Intents  
**Kind**: enum

A result builder that allows you to declaratively describe the sorting options for an entity query.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
@resultBuilder
enum EntityQuerySortingOptionsBuilder<Entity> where Entity : AppEntity
```

## Topics

### Building sorting options
- [static func buildBlock(EntityQuerySortableByProperty<Entity>...) -> [EntityQuerySortableByProperty<Entity>]](entityquerysortingoptionsbuilder/buildblock(_:).md)
### Type Methods
- [static func buildExpression(EntityQuerySortableByProperty<Entity>) -> EntityQuerySortableByProperty<Entity>](entityquerysortingoptionsbuilder/buildexpression(_:).md)

## See Also

- [init(content: () -> [EntityQuerySortableByProperty<Entity>])](entityquerysortingoptions/init(content:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerysortingoptionsbuilder)*