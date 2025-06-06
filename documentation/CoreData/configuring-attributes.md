# Configuring Attributes

**Framework**: Core Data

Describe the properties that compose an entity.

#### Overview

After you create an entity as described in [`Configuring Entities`](configuring-entities.md), you can add attributes to that entity.

An attribute describes a property of an entity. At minimum, you need to specify the property’s name and data type, whether it must be saved in the store, and whether it’s required to have a value when it’s saved.

For some attribute types, you can also choose whether to use a scalar type to represent the attribute in generated classes, as well as configure the attribute to have a default value, or to apply data validation rules.

##### Add Attributes

Add an attribute as indicated in the screenshot and the steps that follow:

![A screenshot of Xcode’s Data Model editor, highlighting the Attributes list in the middle, the Data Model inspector on the right, and the Add Attribute button in the toolbar at the bottom.](https://docs-assets.developer.apple.com/published/3d036ecc8efdd847459c86adbd950698/media-3842668%402x.png)

1. With an entity selected, click Add Attribute at the bottom of the editor area. A new attribute with the placeholder name `attribute`, of type `Undefined`, appears in the Attributes list.
2. In the Attributes list, double-click the newly added attribute, and rename it.
3. In the Attributes list, as shown in the second screenshot, click `Undefined` and choose the attribute’s data type from the Type pop-up menu.

![A screenshot showing the available data types for an attribute.](https://docs-assets.developer.apple.com/published/4cef780cefbb4daf270e60cce1acbf78/media-3839159%402x.png)

##### Configure Attributes

Use the data model inspector (choose View > Inspectors > Show Data Model Inspector) to configure attributes.

![Three screenshots of the Data Model inspector showing how the options vary depending on the attribute’s data type. The left screenshot displays the options for the Float data type, the middle screenshot displays the options for the Date data type, and the screenshot on the right displays the options for the String data type.](https://docs-assets.developer.apple.com/published/c04b3916473aadf8071c9ef469a804d5/media-3842666%402x.png)

For the full list of types, see [`NSAttributeType`](nsattributetype.md).

Core Data optionals aren’t the same as Swift optionals. You can use a Swift optional to represent a required attribute, for example, if you need flexibility to set its value during the time between the object’s initialization and its first save.

Supplying a default value, in combination with making the type non-optional, can provide performance benefits.

For the full list of types, including scalar variants, see [`NSAttributeType`](nsattributetype.md).

For more information, see [`Core Spotlight`](https://developer.apple.com/documentation/CoreSpotlight).

For more information, see [`Migrating your data model automatically`](migrating-your-data-model-automatically.md).

## See Also

- [Configuring Entities](configuring-entities.md)
  Model your app’s objects.
- [Configuring Relationships](configuring-relationships.md)
  Specify how entities relate and how change propagates between them.
- [Generating code](generating-code.md)
  Automatically or manually generate managed object subclasses from entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/configuring-attributes)*