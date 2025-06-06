# Creating a Core Data model

**Framework**: Core Data

Define your app’s object structure with a data model file.

#### Overview

The first step in working with Core Data is to create a data model file to define the structure of your app’s objects, including their object types, properties, and relationships.

You can add a Core Data model file to your Xcode project when you create the project, or you can add it to an existing project.

##### Add Core Data to a New Xcode Project

In the dialog for creating a new project, select the Use Core Data checkbox, and click Next.

![Screenshot showing the Use Core Data checkbox in the options for creating a new Xcode project. The checkbox appears after the language dropdown, and before the checkboxes for including Unit Tests and UI Tests.](https://docs-assets.developer.apple.com/published/19ae17fc660e455d5244f4d43eedb41a/media-3039511%402x.png)

The resulting project includes an `.xcdatamodeld` file.

![Screenshot showing the .xcdatamodeld file highlighted in the project navigator.](https://docs-assets.developer.apple.com/published/bbbb08e2398531cf02bc029b3aa047e3/media-3080773%402x.png)

##### Add a Core Data Model to an Existing Project

Choose File > New > File and select the iOS platform tab. Scroll down to the Core Data section, select Data Model, and click Next.

![Screenshot showing the Data Model template in the Core Data section of the file template chooser.](https://docs-assets.developer.apple.com/published/9e07aa8d17ce31890e3262cb2434d297/media-3039513%402x.png)

Name your model file, select its group and targets, and click Create.

![Screenshot showing the dialog for saving a data model file. The filename is selected and immediately editable.](https://docs-assets.developer.apple.com/published/d04d51680b0977d684f13964ef908766/media-3122943%402x.png)

Xcode adds an `.xcdatamodeld` file with the specified name to your project.

![Screenshot of Xcode showing the new model file selected in the project navigator.](https://docs-assets.developer.apple.com/published/a7a34ec891b4f73305a50e61a313cd9f/media-3080772%402x.png)

## See Also

- [Configuring Attributes](configuring-attributes.md)
  Describe the properties that compose an entity.
- [Configuring Relationships](configuring-relationships.md)
  Specify how entities relate and how change propagates between them.
- [Generating code](generating-code.md)
  Automatically or manually generate managed object subclasses from entities.
- [Setting up a Core Data stack](setting-up-a-core-data-stack.md)
  Set up the classes that manage and persist your app’s objects.
- [Core Data stack](core-data-stack.md)
  Manage and persist your app’s model layer.
- [Handling Different Data Types in Core Data](handling-different-data-types-in-core-data.md)
  Create, store, and present records for a variety of data types.
- [Linking Data Between Two Core Data Stores](linking-data-between-two-core-data-stores.md)
  Organize data in two different stores and implement a link between them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/creating-a-core-data-model)*