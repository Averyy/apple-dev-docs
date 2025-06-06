# predicateForObjectsWithNoCorrelation()

**Framework**: HealthKit  
**Kind**: method

Returns a predicate that matches all objects that are not associated with a HealthKit correlation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func predicateForObjectsWithNoCorrelation() -> NSPredicate
```

#### Return Value

A predicate that matches all objects that are not associated with any HealthKit correlations.

#### Discussion

Use this convenience method to create a predicate that matches all objects not associated with a [`HKCorrelation`](hkcorrelation.md) object. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

## See Also

- [let HKPredicateKeyPathCorrelation: String](hkpredicatekeypathcorrelation.md)
  The key path for accessing the object’s correlation inside a predicate format string.
- [class HKCorrelation](hkcorrelation.md)
  A sample that groups multiple related samples into a single entry.
- [class func predicateForObject(with: UUID) -> NSPredicate](hkquery/predicateforobject(with:).md)
  Returns a predicate that matches an object with the specified universally unique identifier (UUID).
- [class func predicateForObjects(with: Set<UUID>) -> NSPredicate](hkquery/predicateforobjects(with:).md)
  Returns a predicate that matches the objects with the specified  universally unique identifiers (UUIDs).
- [class func predicateForObjects(from: HKSource) -> NSPredicate](hkquery/predicateforobjects(from:)-7j3p2.md)
  Returns a predicate that matches all the objects that were created by the provided source.
- [class func predicateForObjects(from: Set<HKSource>) -> NSPredicate](hkquery/predicateforobjects(from:)-89b4t.md)
  Returns a predicate that matches all the objects that were created by any of the provided sources.
- [class func predicateForObjects(from: Set<HKDevice>) -> NSPredicate](hkquery/predicateforobjects(from:)-9h87f.md)
  Returns a predicate that matches all the objects that were created by any of the provided devices.
- [class func predicateForObjects(withDeviceProperty: String, allowedValues: Set<String>) -> NSPredicate](hkquery/predicateforobjects(withdeviceproperty:allowedvalues:).md)
  Returns a predicate that matches all objects created by devices with the specified properties.
- [class func predicateForObjects(from: Set<HKSourceRevision>) -> NSPredicate](hkquery/predicateforobjects(from:)-1ar4g.md)
  Returns a predicate that matches all the objects that were created by any of the provided source revisions.
- [class func predicateForObjects(withMetadataKey: String) -> NSPredicate](hkquery/predicateforobjects(withmetadatakey:).md)
  Returns a predicate that matches any object whose metadata contains the provided key.
- [class func predicateForObjects(withMetadataKey: String, allowedValues: [Any]) -> NSPredicate](hkquery/predicateforobjects(withmetadatakey:allowedvalues:).md)
  Returns a predicate that matches objects based on the provided metadata key and an array of target values.
- [class func predicateForObjects(withMetadataKey: String, operatorType: NSComparisonPredicate.Operator, value: Any) -> NSPredicate](hkquery/predicateforobjects(withmetadatakey:operatortype:value:).md)
  Returns a predicate that matches objects based on the provided metadata key, value, and operator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforobjectswithnocorrelation())*