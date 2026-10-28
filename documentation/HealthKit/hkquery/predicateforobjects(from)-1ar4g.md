# predicateForObjects(from:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSPredicate *) predicateForObjectsFromSourceRevisions:(NSSet<HKSourceRevision *> *) sourceRevisions;
```

## Return Value

A predicate that matches all the objects created by any of the provided source revisions.

## Discussion

The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

**Swift**:

```swift
let fromSourceRevisions = HKQuery.predicateForObjectsFromSourceRevisions(sourceRevisions)
 
let explicitFromSourceRevisions = NSPredicate(format: "%K IN %@", HKPredicateKeyPathSourceRevision, sourceRevisions)
```

**Objective-C**:

```objc
NSPredicate *fromSourceRevisions = [HKQuery predicateForObjectsFromSourceRevisions:sourceRevisions];
 
NSPredicate *explicitFromSourceRevisions = [NSPredicate predicateWithFormat:@"%K IN %@",
                                            HKPredicateKeyPathSourceRevision,
                                            sourceRevisions];
```

## Parameters

- `sourceRevisions`: A set of source revisions that have saved data to the HealthKit store.

## See Also

### Creating object predicates
- [class func predicateForObject(with: UUID) -> NSPredicate](./predicateforobject%28with%29.md)
  Returns a predicate that matches an object with the specified universally unique identifier (UUID).
- [class func predicateForObjects(with: Set<UUID>) -> NSPredicate](./predicateforobjects%28with%29.md)
  Returns a predicate that matches the objects with the specified  universally unique identifiers (UUIDs).
- [class func predicateForObjects(from: HKSource) -> NSPredicate](./predicateforobjects%28from%29-7j3p2.md)
  Returns a predicate that matches all the objects that were created by the provided source.
- [class func predicateForObjects(from: Set<HKSource>) -> NSPredicate](./predicateforobjects%28from%29-89b4t.md)
  Returns a predicate that matches all the objects that were created by any of the provided sources.
- [class func predicateForObjects(from: Set<HKDevice>) -> NSPredicate](./predicateforobjects%28from%29-9h87f.md)
  Returns a predicate that matches all the objects that were created by any of the provided devices.
- [class func predicateForObjects(withDeviceProperty: String, allowedValues: Set<String>) -> NSPredicate](./predicateforobjects%28withdeviceproperty,allowedvalues%29.md)
  Returns a predicate that matches all objects created by devices with the specified properties.
- [class func predicateForObjects(withMetadataKey: String) -> NSPredicate](./predicateforobjects%28withmetadatakey%29.md)
  Returns a predicate that matches any object whose metadata contains the provided key.
- [class func predicateForObjects(withMetadataKey: String, allowedValues: [Any]) -> NSPredicate](./predicateforobjects%28withmetadatakey,allowedvalues%29.md)
  Returns a predicate that matches objects based on the provided metadata key and an array of target values.
- [class func predicateForObjects(withMetadataKey: String, operatorType: NSComparisonPredicate.Operator, value: Any) -> NSPredicate](./predicateforobjects%28withmetadatakey,operatortype,value%29.md)
  Returns a predicate that matches objects based on the provided metadata key, value, and operator.
- [class func predicateForObjectsWithNoCorrelation() -> NSPredicate](./predicateforobjectswithnocorrelation%28%29.md)
  Returns a predicate that matches all objects that are not associated with a HealthKit correlation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforobjects(from:)-1ar4g)*