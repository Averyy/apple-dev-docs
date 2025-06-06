# associate(sourceInstance:withDestinationInstance:for:)

**Framework**: Core Data  
**Kind**: method

Associates a given source managed object instance with an array of destination instances for a given property mapping.

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
func associate(sourceInstance: NSManagedObject, withDestinationInstance destinationInstance: NSManagedObject, for entityMapping: NSEntityMapping)
```

#### Discussion

Data migration is performed as a three-stage process (first create the data, then relate the data, then validate the data). You use this method to associate data between the source and destination stores, in order to allow for relationship creation or fix-up after the creation stage.

This method is called in the default implementation of `NSEntityMigrationPolicy`’s [`createDestinationInstances(forSource:in:manager:)`](nsentitymigrationpolicy/createdestinationinstances(forsource:in:manager:).md) method.

## Parameters

- `sourceInstance`: A source managed object.
- `destinationInstance`: The destination manage object for  .
- `entityMapping`: The entity mapping to use to associate   with the object in  .

## See Also

- [func destinationInstances(forEntityMappingName: String, sourceInstances: [NSManagedObject]?) -> [NSManagedObject]](nsmigrationmanager/destinationinstances(forentitymappingname:sourceinstances:).md)
  Returns the managed object instances created in the destination store for the named entity mapping for the given array of source instances.
- [func sourceInstances(forEntityMappingName: String, destinationInstances: [NSManagedObject]?) -> [NSManagedObject]](nsmigrationmanager/sourceinstances(forentitymappingname:destinationinstances:).md)
  Returns the managed object instances in the source store used to create the given destination instances for the passed in property mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/associate(sourceinstance:withdestinationinstance:for:))*