# sourceInstances(forEntityMappingName:destinationInstances:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the managed object instances in the source store used to create the given destination instances for the passed in property mapping.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func sourceInstances(forEntityMappingName mappingName: String, destinationInstances: [NSManagedObject]?) -> [NSManagedObject]
```

```objc
- (NSArray<__kindof NSManagedObject *> *) sourceInstancesForEntityMappingNamed:(NSString *) mappingName destinationInstances:(NSArray<__kindof NSManagedObject *> *) destinationInstances;
```

#### Return Value

An array containing the managed object instances in the source store used to create `destinationInstances` using the entity mapping named `mappingName`. If `destinationInstances` is `nil`, all of the source instances used to create the destination instance for this property mapping are returned.

#### Discussion

This method throws an `NSInvalidArgumentException` exception if `mappingName` is not a valid mapping name.

## Parameters

- `mappingName`: The name of an entity mapping in use.
- `destinationInstances`: A array of managed objects in the destination store.

## See Also

### Managing Sources and Destinations
- [func associate(sourceInstance: NSManagedObject, withDestinationInstance: NSManagedObject, for: NSEntityMapping)](./associate%28sourceinstance,withdestinationinstance,for%29.md)
  Associates a given source managed object instance with an array of destination instances for a given property mapping.
- [func destinationInstances(forEntityMappingName: String, sourceInstances: [NSManagedObject]?) -> [NSManagedObject]](./destinationinstances%28forentitymappingname,sourceinstances%29.md)
  Returns the managed object instances created in the destination store for the named entity mapping for the given array of source instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/sourceinstances(forentitymappingname:destinationinstances:))*