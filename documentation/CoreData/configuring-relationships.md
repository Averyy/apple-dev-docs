# Configuring Relationships

**Framework**: Core Data

Specify how entities relate and how change propagates between them.

#### Overview

After you define at least two entities as described in [`Configuring Entities`](configuring-entities.md), you can add a relationship between the entities.

A relationship describes how an entity affects another entity. At minimum, a relationship specifies a name, a destination entity, a delete rule, a cardinality type (To One or To Many), settings for whether the relationship must be saved in the store (transient), and whether it is required to have a value when saved (optional). You must also configure every relationship with an inverse relationship.

##### Add Relationships

To add a relationship, do the following:

1. Select the graph editor style to view all your app’s entities.
2. Control-drag from one entity to another to create a pair of relationships. An arrow appears between the entities to indicate a relationship, and the editor creates a placeholder relationship with the name `newRelationship` in each entity.

![A screenshot showing two entities side-by-side in the Data Model editor when the Graph editor style is in a selected state. An arrow that represents a relationship joins the two entities.](https://docs-assets.developer.apple.com/published/a68ba0a099550c5f72d44874c93df11b/media-3842670%402x.png)

##### Configure Relationships

After creating a pair of relationships, configure each relationship as indicated in the screenshot and the steps that follow:

![A screenshot of Xcode’s Data model editor. The Quake entity is in a selected state, and the screenshot highlights the entity’s relationships. The Data Model inspector shows the attributes of a relationship with the name countries.](https://docs-assets.developer.apple.com/published/53dc5402512f6561f90b48591ea5a0c3/media-3845726%402x.png)

1. Select the table editor style to edit one entity at a time.
2. Open the Data Model inspector (choose View > Inspectors > Show Data Model Inspector).
3. Select the source entity from the Entities list, then select the new relationship in the Relationships list. Use the Data Model inspector to configure its name, destination, inverse, delete rule, and cardinality type, and to indicate if it is transient or optional.
4. Select the destination entity from the Entities list, then select the new relationship in the Relationships list. Use the Data Model inspector to configure its name, destination, inverse, delete rule, and cardinality type, and to indicate if it is transient or optional.

![A screenshot showing the countries relationship in the Data Model inspector. The destination is Country, the inverse is quakes, the delete rule is Nullify, and the relationship type is To Many.](https://docs-assets.developer.apple.com/published/6e71bb7023524882df35f6b029c6f390/media-3839160%402x.png)

The above example shows a `Quake` entity’s `countries` relationship, referring to one or more countries a given earthquake affects. It has an inverse relationship on the `Country` entity called `quakes`, referring to any earthquakes affecting that country.

Setting the same source and destination types creates a reflexive relationship. For example, an `Employee` may manage another `Employee`.

When creating relationships in the Graph editor, you add inverse relationships between entities in a single step. When creating relationships in the Table editor, you add inverse relationships to each entity individually.

Select No Action to delete the source object instance, but leave references to it in any destination object instances, which you update manually.

Select** **Nullify to delete the source object instance, and nullify references to it in any destination object instances.

Select Cascade to delete the source object instance, and with it, all of the destination object instances.

Select Deny to delete the source object only if it doesn’t point to any destination object instances.

Use To One relationships to connect the source with a single instance of the destination type.

Use To Many relationships to connect the source with a mutable set of the destination type, and to optionally specify an arrangement and count:

Arrangement—Select the Ordered checkbox to specify that the relationship has an inherent ordering, and to generate an  mutable set.

Count—You can also place upper and lower limits on the number of destination instances. For optional relationships, the number of instances can be zero or within these bounds.

## See Also

- [enum NSDeleteRule](nsdeleterule.md)
  Constants that determine what happens when you delete a relationship’s owning managed object.
- [Configuring Entities](configuring-entities.md)
  Model your app’s objects.
- [Configuring Attributes](configuring-attributes.md)
  Describe the properties that compose an entity.
- [Generating code](generating-code.md)
  Automatically or manually generate managed object subclasses from entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/configuring-relationships)*