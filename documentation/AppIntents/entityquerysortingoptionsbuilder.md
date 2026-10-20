# EntityQuerySortingOptionsBuilder

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

A result builder that allows you to declaratively describe the sorting options for an entity query.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
@resultBuilder
enum EntityQuerySortingOptionsBuilder<Entity> where Entity : AppEntity
```

## Topics

### Building sorting options
- [static func buildBlock(EntityQuerySortableByProperty<Entity>...) -> [EntityQuerySortableByProperty<Entity>]](./entityquerysortingoptionsbuilder/buildblock%28_%29.md)
### Type Methods
- [static func buildExpression(EntityQuerySortableByProperty<Entity>) -> EntityQuerySortableByProperty<Entity>](./entityquerysortingoptionsbuilder/buildexpression%28_%29.md)

## See Also

### Creating the sorting options
- [init(content: () -> [EntityQuerySortableByProperty<Entity>])](./entityquerysortingoptions/init%28content%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerysortingoptionsbuilder)*