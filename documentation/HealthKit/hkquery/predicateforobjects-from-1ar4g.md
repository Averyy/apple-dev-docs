# predicateForObjects(from:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate that matches all the objects that were created by any of the provided source revisions.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func predicateForObjects(from sourceRevisions: Set<HKSourceRevision>) -> NSPredicate
```

#### Return Value

A predicate that matches all the objects created by any of the provided source revisions.

#### Discussion

The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

## Parameters

- `sourceRevisions`: A set of source revisions that have saved data to the HealthKit store.

## See Also

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
- [class func predicateForObjects(withMetadataKey: String) -> NSPredicate](hkquery/predicateforobjects(withmetadatakey:).md)
  Returns a predicate that matches any object whose metadata contains the provided key.
- [class func predicateForObjects(withMetadataKey: String, allowedValues: [Any]) -> NSPredicate](hkquery/predicateforobjects(withmetadatakey:allowedvalues:).md)
  Returns a predicate that matches objects based on the provided metadata key and an array of target values.
- [class func predicateForObjects(withMetadataKey: String, operatorType: NSComparisonPredicate.Operator, value: Any) -> NSPredicate](hkquery/predicateforobjects(withmetadatakey:operatortype:value:).md)
  Returns a predicate that matches objects based on the provided metadata key, value, and operator.
- [class func predicateForObjectsWithNoCorrelation() -> NSPredicate](hkquery/predicateforobjectswithnocorrelation.md)
  Returns a predicate that matches all objects that are not associated with a HealthKit correlation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforobjects(from:)-1ar4g)*