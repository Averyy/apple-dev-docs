# DynamicPropertyPathCollection

**Framework**: App Intents Testing  
**Kind**: struct

Indexed result items from an intent value query.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct DynamicPropertyPathCollection
```

#### Overview

Access query results by index and navigate their properties using dynamic member lookup:

```swift
let result = try await searchQuery.values(for: "Arizona")

XCTAssertEqual(result.items.count, 3)
XCTAssertEqual(try result.items[0].name, "Botanical Garden")
```

## Topics

### Instance Properties
- [var count: Int](dynamicpropertypathcollection/count.md)
  The number of items in the collection.
- [var isEmpty: Bool](dynamicpropertypathcollection/isempty.md)
  A Boolean value that indicates whether the collection is empty.
### Subscripts
- [subscript<T>(Int) -> T](dynamicpropertypathcollection/subscript(_:)-6t8mq.md)
  Accesses typed properties from the intent value at the given index.
- [subscript(Int) -> DynamicPropertyPath](dynamicpropertypathcollection/subscript(_:)-700kp.md)
  Creates a dynamic path for navigating into the item’s properties.
- [subscript(Int) -> (any IntentValueExpressing)?](dynamicpropertypathcollection/subscript(_:)-8h9mv.md)
  Accesses an item for nil checking and assigning to intent parameters without casting.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol AppIntentTypeDefinition](appintenttypedefinition.md)
  A protocol that associates a definition type with its corresponding instance type.
- [struct DynamicPropertyPath](dynamicpropertypath.md)
  A type-safe, dynamic path to access nested intent values.
- [struct IntentValuePropertiesCallable](intentvaluepropertiescallable.md)
  A callable wrapper that creates app intent instances from keyword arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/dynamicpropertypathcollection)*