# EntityPropertyQuery.QueryProperties

**Framework**: App Intents  
**Kind**: typealias

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
typealias QueryProperties = EntityQueryProperties<Self.Entity, Self.ComparatorMappingType>
```

## See Also

- [static var properties: Self.QueryProperties](entitypropertyquery/properties.md)
  The set of query properties supported by this query.
- [EntityPropertyQuery.Property](entitypropertyquery/property.md)
- [associatedtype ComparatorMappingType](entitypropertyquery/comparatormappingtype.md)
  Type produced by `EntityQueryComparator` mapping closures and supplied as input to `results`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitypropertyquery/queryproperties)*