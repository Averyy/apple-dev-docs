# NSManagedObjectModel

**Framework**: Core Data  
**Kind**: class

A programmatic representation of the `.xcdatamodeld` file describing your objects.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSManagedObjectModel
```

## Mentions

- [Setting up a Core Data stack manually](setting-up-a-core-data-stack-manually.md)
- [Setting up a Core Data stack](setting-up-a-core-data-stack.md)

#### Overview

The model contains one or more `NSEntityDescription` objects representing the entities in the schema. Each `NSEntityDescription` object has property description objects (instances of subclasses of [`NSPropertyDescription`](nspropertydescription.md)) that represent the properties (or fields) of the entity in the schema. The Core Data framework uses this description in several ways:

- Constraining UI creation in Interface Builder
- Validating attribute and relationship values at runtime
- Mapping between your managed objects and a database or file-based schema for object persistence

A managed object model maintains a mapping between each of its entity objects and a corresponding managed object class for use with the persistent storage mechanisms in the Core Data framework. You can determine the entity for a particular managed object with the `entity` method.

You typically create managed object models using the data modeling tool in Xcode, but it’s possible to build a model programmatically if needed.

##### Loading a Model File

Managed object model files are typically stored in a project or a framework. To load a model, you provide an URL to the constructor. Note that loading a model doesn’t have the effect of loading all of its entities.

##### Storing Fetch Requests

Frequently, you need a collection of objects that share features in common. Sometimes you can define those features (property values) in advance; sometimes you need to be able to supply values at runtime. For example, suppose you want to retrieve all movies owned by Pixar, or retrieve all movies that earned more than an amount specified by the user at runtime.

Fetch requests are often predefined in a managed object model as templates. They allow you to predefine named queries and their parameters in the model. Typically they contain variables that need to be substituted at runtime. `NSManagedObjectModel` provides an API to retrieve a stored fetch request by name, and to perform variable substitution—see [`fetchRequestTemplate(forName:)`](nsmanagedobjectmodel/fetchrequesttemplate(forname:).md) and [`fetchRequestFromTemplate(withName:substitutionVariables:)`](nsmanagedobjectmodel/fetchrequestfromtemplate(withname:substitutionvariables:).md).

You typically define fetch request templates using the Data Model editor in Xcode. You can also create fetch request templates programmatically, and associate them with a model using [`setFetchRequestTemplate(_:forName:)`](nsmanagedobjectmodel/setfetchrequesttemplate(_:forname:).md).

##### Supporting Multiple Configurations for the Same Model

You may want to specify different sets of entities for the same model to be used in different situations. For example, suppose certain entities should only be available if a user has administrative privileges. To support this requirement, a model may have more than one configuration. Each configuration is named, and has an associated set of entities. The sets may overlap. You establish configurations programmatically using [`setEntities(_:forConfigurationName:)`](nsmanagedobjectmodel/setentities(_:forconfigurationname:).md) or using the Xcode design tool, and retrieve the entities for a given configuration name using [`entities(forConfigurationName:)`](nsmanagedobjectmodel/entities(forconfigurationname:).md).

##### Changing Models

Because a model describes the structure of the data in a persistent store, changing any parts of a model that alters the schema renders it incompatible with (and so unable to open) the stores it previously created. If you change your schema, you therefore need to migrate the data in existing stores to new version (see [`Core Data Model Versioning and Data Migration Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)). For example, if you add a new entity or a new attribute to an existing entity, you  open old stores; if you add a validation constraint or set a new default value for an attribute, you  open old stores.

##### Editing Models at Runtime

Managed object models are editable until they are used by an object graph manager (a managed object context or a persistent store coordinator). This allows you to create or modify them dynamically until their first use. However, once a model is being used, it  be changed. This is enforced at runtime—when the object manager first fetches data using a model, the whole of that model becomes uneditable. Any attempt to mutate a model or any of its sub-objects after that point throws an exception. If you need to modify a model that’s in use, create a copy, modify the copy, and then discard the objects with the old model.

##### Enumerating Entities with Fast Enumeration

In macOS 10.5 and later and on iOS, `NSManagedObjectModel` supports the [`NSFastEnumeration`](https://developer.apple.com/documentation/Foundation/NSFastEnumeration) protocol. You can use this to enumerate over a model’s entities, as illustrated in the following example:

```objc
NSManagedObjectModel *aModel = ...;
for (NSEntityDescription *entity in aModel) {
    // entity is each instance of NSEntityDescription in aModel in turn
}
```

## Topics

### Creating a managed object model
- [convenience init?(contentsOf: URL)](nsmanagedobjectmodel/init(contentsof:).md)
  Initializes the managed object model using the model file at the specified URL.
- [init()](nsmanagedobjectmodel/init.md)
  Initializes an empty managed object model.
- [class func mergedModel(from: [Bundle]?) -> NSManagedObjectModel?](nsmanagedobjectmodel/mergedmodel(from:).md)
  Returns a model created by merging all the models found in given bundles.
- [class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) -> NSManagedObjectModel?](nsmanagedobjectmodel/mergedmodel(from:forstoremetadata:).md)
  Returns a merged model from a specified array for the version information in provided metadata.
- [init?(byMerging: [NSManagedObjectModel]?)](nsmanagedobjectmodel/init(bymerging:).md)
  Creates a single model from an array of existing models.
- [init?(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])](nsmanagedobjectmodel/init(bymerging:forstoremetadata:).md)
  Returns, for the version information in given metadata, a model merged from a given array of models.
### Managing entities and configurations
- [var entities: [NSEntityDescription]](nsmanagedobjectmodel/entities.md)
  The entities in the model.
- [var entitiesByName: [String : NSEntityDescription]](nsmanagedobjectmodel/entitiesbyname.md)
  The entities of the model, keyed by name.
- [var configurations: [String]](nsmanagedobjectmodel/configurations.md)
  All the available configuration names of the model.
- [func entities(forConfigurationName: String?) -> [NSEntityDescription]?](nsmanagedobjectmodel/entities(forconfigurationname:).md)
  Returns the entities of the model for a specified configuration.
- [func setEntities([NSEntityDescription], forConfigurationName: String)](nsmanagedobjectmodel/setentities(_:forconfigurationname:).md)
  Associates the specified entities with the model using the given configuration name.
### Manipulating fetch request templates
- [var fetchRequestTemplatesByName: [String : NSFetchRequest<any NSFetchRequestResult>]](nsmanagedobjectmodel/fetchrequesttemplatesbyname.md)
  A dictionary of the receiver’s fetch request templates, keyed by name.
- [func fetchRequestTemplate(forName: String) -> NSFetchRequest<any NSFetchRequestResult>?](nsmanagedobjectmodel/fetchrequesttemplate(forname:).md)
  Returns the fetch request with a specified name.
- [func fetchRequestFromTemplate(withName: String, substitutionVariables: [String : Any]) -> NSFetchRequest<any NSFetchRequestResult>?](nsmanagedobjectmodel/fetchrequestfromtemplate(withname:substitutionvariables:).md)
  Returns a copy of the fetch request template with the variables substituted by values from the substitutions dictionary.
- [func setFetchRequestTemplate(NSFetchRequest<any NSFetchRequestResult>?, forName: String)](nsmanagedobjectmodel/setfetchrequesttemplate(_:forname:).md)
  Associates the specified fetch request with the receiver using the given name.
### Handling localization
- [var localizationDictionary: [String : String]?](nsmanagedobjectmodel/localizationdictionary.md)
  The localization dictionary of the model.
### Versioning and migrating entities
- [var versionChecksum: String](nsmanagedobjectmodel/versionchecksum.md)
  The Base64-encoded 128-bit model version hash.
- [var versionIdentifiers: Set<AnyHashable>](nsmanagedobjectmodel/versionidentifiers.md)
  The set of developer-defined version identifiers for the object model.
- [var entityVersionHashesByName: [String : Data]](nsmanagedobjectmodel/entityversionhashesbyname.md)
  The dictionary of the model’s entity names and their corresponding version hashes.
- [func isConfiguration(withName: String?, compatibleWithStoreMetadata: [String : Any]) -> Bool](nsmanagedobjectmodel/isconfiguration(withname:compatiblewithstoremetadata:).md)
  Returns a Boolean value that indicates whether a given configuration in the model is compatible with given metadata from a persistent store.
### Working with indexes
- [enum NSFetchIndexElementType](nsfetchindexelementtype.md)
  Defines the possible types of index elements.
- [class NSFetchIndexDescription](nsfetchindexdescription.md)
  The description of the index.
- [class NSFetchIndexElementDescription](nsfetchindexelementdescription.md)
  Description of an Index Element
### Instance Methods
- [func makeManagedObjectModel(for: Schema, mergedWith: NSManagedObjectModel?) -> NSManagedObjectModel?](nsmanagedobjectmodel/makemanagedobjectmodel(for:mergedwith:)-swift.method.md)
### Type Methods
- [static func makeManagedObjectModel(for: any PersistentModel.Type..., mergedWith: NSManagedObjectModel?) -> NSManagedObjectModel?](nsmanagedobjectmodel/makemanagedobjectmodel(for:mergedwith:)-2tc31.md)
- [static func makeManagedObjectModel(for: [any PersistentModel.Type], mergedWith: NSManagedObjectModel?) -> NSManagedObjectModel?](nsmanagedobjectmodel/makemanagedobjectmodel(for:mergedwith:)-37opo.md)
- [static func makeManagedObjectModel(for: Schema, mergedWith: NSManagedObjectModel?) -> NSManagedObjectModel?](nsmanagedobjectmodel/makemanagedobjectmodel(for:mergedwith:)-7lqq9.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSFastEnumeration](../Foundation/NSFastEnumeration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSEntityDescription](nsentitydescription.md)
  A description of a Core Data entity.
- [class NSPropertyDescription](nspropertydescription.md)
  A description of a single property belonging to an entity.
- [class NSAttributeDescription](nsattributedescription.md)
  A description of a single attribute belonging to an entity.
- [class NSDerivedAttributeDescription](nsderivedattributedescription.md)
  A description of an attribute that derives its value by performing a calculation on a related attribute.
- [class NSRelationshipDescription](nsrelationshipdescription.md)
  A description of a relationship between two entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel)*