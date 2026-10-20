# predicateForObjects(withMetadataKey:allowedValues:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate that matches objects based on the provided metadata key and an array of target values.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func predicateForObjects(withMetadataKey key: String, allowedValues: [Any]) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForObjectsWithMetadataKey:(NSString *) key allowedValues:(NSArray *) allowedValues;
```

#### Return Value

A predicate that matches objects based on the provided metadata key and an array of target values..

#### Discussion

Use this convenience method to create a predicate that matches objects based on their metadata. When this predicate is evaluated, it gets the metadata’s value for the provided key. Then the predicate checks that value against the `allowedValues` array. If the array contains a matching value, the predicate returns [`true`](../../Swift/true.md); otherwise, it returns [`false`](../../Swift/false.md).

The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

**Swift**:

```swift
let metadataValues =
    HKQuery.predicateForObjectsWithMetadataKey(HKMetadataKeyFoodType,
                                               allowedValues: ["Pizza", "Tofu"])
 
 
let explicitMetadataKey = NSPredicate(format: "%K.%K IN %@",
                                      HKPredicateKeyPathMetadata, HKMetadataKeyFoodType, ["Pizza", "Tofu"])
```

**Objective-C**:

```objc
NSPredicate *metadataValues =
    [HKQuery predicateForObjectsWithMetadataKey:HKMetadataKeyFoodType
                                  allowedValues:@[@"Pizza", @"Tofu"]];
 
NSPredicate *explicitMetadataValues =
    [NSPredicate predicateWithFormat:@"%K.%K in %@",
     HKPredicateKeyPathMetadata,
     HKMetadataKeyFoodType,
     @[@"Pizza", @"Tofu"]];
```

## Parameters

- `key`: The metadata key for the value to be matched. For a list of preset keys, see Metadata Keys. You may also search using custom keys.
- `allowedValues`: An array of valid values. These values must be [`NSString`](../../Foundation/nsstring.md), [`NSNumber`](../../Foundation/nsnumber.md), or [`NSDate`](../../Foundation/nsdate.md) instances.

## See Also

### Related Documentation
- [let HKPredicateKeyPathMetadata: String](../hkpredicatekeypathmetadata.md)
  The key path for accessing the object’s metadata dictionary inside a predicate format string.
- [var metadata: [String : Any]?](../hkobject/metadata.md)
  The metadata for this HealthKit object.
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
- [class func predicateForObjects(from: Set<HKSourceRevision>) -> NSPredicate](./predicateforobjects%28from%29-1ar4g.md)
  Returns a predicate that matches all the objects that were created by any of the provided source revisions.
- [class func predicateForObjects(withMetadataKey: String) -> NSPredicate](./predicateforobjects%28withmetadatakey%29.md)
  Returns a predicate that matches any object whose metadata contains the provided key.
- [class func predicateForObjects(withMetadataKey: String, operatorType: NSComparisonPredicate.Operator, value: Any) -> NSPredicate](./predicateforobjects%28withmetadatakey,operatortype,value%29.md)
  Returns a predicate that matches objects based on the provided metadata key, value, and operator.
- [class func predicateForObjectsWithNoCorrelation() -> NSPredicate](./predicateforobjectswithnocorrelation%28%29.md)
  Returns a predicate that matches all objects that are not associated with a HealthKit correlation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforobjects(withmetadatakey:allowedvalues:))*