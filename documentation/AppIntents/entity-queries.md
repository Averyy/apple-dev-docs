# Entity queries

**Framework**: App Intents

Help the system find the entities your app defines and use them to resolve parameters.

#### Overview

When the system needs to retrieve one or more specific instances of an app entity, it asks you to provide a relevant query type. The system uses queries during parameter resolution when the parameter of an intent contains an entity. The system also uses them to resolve information in a different format into one of your app’s entities. For example, it uses them to resolve natural spoken language into one of your app’s entities.

The system can sometimes determine which entities it needs and provide you with a list of corresponding identifiers. Provide an [`EntityQuery`](entityquery.md) type to supply the entities for those identifiers. Provide additional query types to perform more advanced searches, such as a search that matches specific properties of the entity.

## Topics

### Identifier-based queries
- [protocol EntityQuery](entityquery.md)
  An interface for locating entities using their identifiers.
- [protocol EnumerableEntityQuery](enumerableentityquery.md)
  An interface you use to provide a short list of entities that are relatively small in size.
### String-based queries
- [protocol EntityStringQuery](entitystringquery.md)
  An interface that locates entities using arbitrary string input.
### Property-matched queries
- [protocol EntityPropertyQuery](entitypropertyquery.md)
  An interface for locating entities by matching values against one or more of their properties.
- [struct EntityQueryProperties](entityqueryproperties.md)
  A type that provides the properties to include in a property-matched query.
- [class EntityQueryProperty](entityqueryproperty.md)
  An object that provides the supported comparators you use to describe the different ways users can query against a property of an app entity.
- [Property comparators](property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.
- [struct EntityQuerySortingOptions](entityquerysortingoptions.md)
  The potential properties you can use to sort the results of a query.
- [struct EntityQuerySortableByProperty](entityquerysortablebyproperty.md)
  Details about a specific property you use to sort the query results.
- [struct EntityQuerySort](entityquerysort.md)
  The properties to use to sort the results when the query runs.
### Unique entity queries
- [protocol UniqueAppEntityQuery](uniqueappentityquery.md)
  A query designed for only returning a single possible value, provided by `uniqueEntity`. Protocol extensions will provide the other required query methods based on that.
- [struct UniqueAppEntityProvider](uniqueappentityprovider.md)
  A simplified query type conforming to `UniqueAppEntityQuery`.  Use this as the value of the `defaultQuery` of an entity conforming to `UniqueAppEntity`.

## See Also

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
  Enable people to configure app intents with their custom input values.
- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)
  Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.
- [Parameter resolution](parameter-resolution.md)
  Define the required parameters for your app intents and specify how to resolve those parameters at runtime.
- [App entities](app-entities.md)
  Make core types or concepts discoverable to the system by declaring them as app entities.
- [Resolvers](resolvers.md)
  Resolve the parameters of your app intents, and extend the standard resolution types to include your app’s custom types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entity-queries)*