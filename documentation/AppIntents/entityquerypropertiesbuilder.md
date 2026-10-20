# EntityQueryPropertiesBuilder

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

A result builder that allows you to declaratively describe the properties to include in a property-matched query.

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
enum EntityQueryPropertiesBuilder<Entity, ComparatorMappingType> where Entity : AppEntity
```

## Topics

### Building queryable properties
- [static func buildBlock(EntityQueryPropertyDeclaration<Entity, ComparatorMappingType>...) -> [EntityQueryPropertyDeclaration<Entity, ComparatorMappingType>]](./entityquerypropertiesbuilder/buildblock%28_%29.md)
- [class EntityQueryPropertyDeclaration](./entityquerypropertydeclaration.md)
  An object that identifies a specific entity property and the query comparators it supports.
### Type Methods
- [static func buildExpression(EntityQueryPropertyDeclaration<Entity, ComparatorMappingType>) -> EntityQueryPropertyDeclaration<Entity, ComparatorMappingType>](./entityquerypropertiesbuilder/buildexpression%28_%29.md)

## See Also

### Creating the query properties
- [init(properties: () -> [EntityQueryPropertyDeclaration<Entity, ComparatorMappingType>])](./entityqueryproperties/init%28properties%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerypropertiesbuilder)*