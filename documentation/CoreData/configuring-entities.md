# Configuring Entities

**Framework**: Core Data

Model your app’s objects.

#### Overview

An entity describes an object, including its name, attributes, and relationships. Create an entity for each of your app’s objects.

##### Add Entities

After you create a Core Data model as described in [`Creating a Core Data model`](creating-a-core-data-model.md), add an entity to your project’s `.xcdatamodeld` file:

1. Click Add Entity at the bottom of the editor area. A new entity with placeholder name `Entity` appears in the Entities list.
2. In the Entities list, double-click the newly added entity and rename it. This step updates both the entity name and class name visible in the Data Model inspector.

![A screenshot of Xcode’s Data Model editor, highlighting the Entities list on the left, the Data Model inspector on the right, and the Add Entity button in the toolbar at the bottom.](https://docs-assets.developer.apple.com/published/03b919c6f4246db81536152209fc34e2/media-3842665%402x.png)

In addition to the required name and class name fields, entities have a default setting for the required code generation field. If you need to add inheritance, unique constraints, versioning, or other optional information, configure your entity as described below. Otherwise, add the properties that compose your entity as described in [`Configuring Attributes`](configuring-attributes.md).

##### Configure Entities

Use the data model inspector (choose View > Inspectors > Show Data Model Inspector) to configure your entity.

For information about the options for code generation, see [`Generating code`](generating-code.md).

Unique constraints prevent duplicate records in the store. When saving a new record, the store checks whether any record already exists with the same value for the constrained attribute. In the case of a conflict, [`NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType`](nsmergepolicytype/mergebypropertyobjecttrumpmergepolicytype.md) causes the new record to overwrite all fields in the existing record.

For more information, see [`Core Spotlight`](https://developer.apple.com/documentation/CoreSpotlight).

For more information, see [`Migrating your data model automatically`](migrating-your-data-model-automatically.md).

## See Also

- [Configuring Attributes](configuring-attributes.md)
  Describe the properties that compose an entity.
- [Configuring Relationships](configuring-relationships.md)
  Specify how entities relate and how change propagates between them.
- [Generating code](generating-code.md)
  Automatically or manually generate managed object subclasses from entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/configuring-entities)*