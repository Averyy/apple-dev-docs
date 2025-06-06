# destinationInstances(forEntityMappingName:sourceInstances:)

**Framework**: Core Data  
**Kind**: method

Returns the managed object instances created in the destination store for the named entity mapping for the given array of source instances.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func destinationInstances(forEntityMappingName mappingName: String, sourceInstances: [NSManagedObject]?) -> [NSManagedObject]
```

#### Return Value

An array containing the managed object instances created in the destination store for the entity mapping named `mappingName` for `sourceInstances`. If `sourceInstances` is `nil`, all of the destination instances created by the specified property mapping are returned.

#### Discussion

This method throws an `NSInvalidArgumentException` exception if `mappingName` is not a valid mapping name.

## Parameters

- `mappingName`: The name of an entity mapping in use.
- `sourceInstances`: A array of managed objects in the source store.

## See Also

- [func associate(sourceInstance: NSManagedObject, withDestinationInstance: NSManagedObject, for: NSEntityMapping)](nsmigrationmanager/associate(sourceinstance:withdestinationinstance:for:).md)
  Associates a given source managed object instance with an array of destination instances for a given property mapping.
- [func sourceInstances(forEntityMappingName: String, destinationInstances: [NSManagedObject]?) -> [NSManagedObject]](nsmigrationmanager/sourceinstances(forentitymappingname:destinationinstances:).md)
  Returns the managed object instances in the source store used to create the given destination instances for the passed in property mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/destinationinstances(forentitymappingname:sourceinstances:))*