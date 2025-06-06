# Inspecting and Editing an iCloud Container’s Schema

**Framework**: CloudKit

Review and edit the schema for your app’s container using the CloudKit Database app.

#### Overview

Use the CloudKit Database app to verify existing record types, create new record types, edit fields, add search indexes, and delete unpublished record types.

To manage a schema’s record types, open the CloudKit Database app and select your app’s container.

##### Inspect Record Types

If you create a record programmatically through just-in-time schema creation, use the CloudKit Database app to verify that the record type appears in the schema with the name and fields you expect.

To view the fields for a record type:

1. Select Record Types in the CloudKit Database app Schema section for your app’s container.
2. On the main screen, select a record type. The app displays the field names and the field types for the record type you select. You can then add, modify, and remove unpublished fields.

![A screenshot showing a container’s record types on the schema management page of the CloudKit Database app. The screenshot highlights the Record Types menu item in the Schema section on the left, as well as the selected Record Type in the pane on the right.](https://docs-assets.developer.apple.com/published/4c3a86836ec5d4dfc9926bef5d2e774a/media-3699099%402x.png)

For more information about just-in-time schema creation, see the [`Save initial records to iCloud`](designing-and-creating-a-cloudkit-database#Save-initial-records-to-iCloud.md) section of [`Designing and Creating a CloudKit Database`](designing-and-creating-a-cloudkit-database.md).

##### Enable Querying for Your Record Type

When designing and debugging your database, you might find it useful to search for records with a particular record type. To enable searching for records by type, you must first add an index to a field on your record type.

When you create a record programmatically, iCloud creates a `recordName` metadata field in the corresponding record type. You add a `QUERYABLE` index to this field to enable searching for records by type in the CloudKit Database app and in code.

To enable querying:

1. From the CloudKit Database app schema management page for your app’s container, select Indexes from the Schema section in the navigation menu on the left.
2. To view or remove exisiting indexes, select a field name in the Indexes panel.
3. To add an index, click the plus icon at the top of the Indexes panel.
4. Set Record Type to the desired record type.
5. Enter a name for the new index.
6. Set Type to QUERYABLE.
7. Choose the field to index.
8. Click Add. The new index appears in Indexes main panel, and you can search for records using that field.

![A screenshot showing a container’s indexes on the schema management page of the CloudKit Dashboard app. The screenshot highlights the Indexes menu item in the Schema section on the left and the Add Index pane.](https://docs-assets.developer.apple.com/published/cd1d954320f5a477f44893402eb25094/media-3699101%402x.png)

##### Create a Record Type

In addition to creating record types programmatically using just-in-time schema creation, you can create new record types directly in the CloudKit Database app.

To create a new record type:

1. From the CloudKit Database app schema management page for your app’s container, select Record Types from the Schema section on the left.
2. Click the click the plus icon at the top of the Record Types panel provide a name and description for the new record type in the fields that appear.
3. Click the Create Record Type button. CloudKit adds the new record type to the schema.
4. To add a field, click the Add button next to Record Fields, enter a field name and description, and select a field type from the menu.
5. To delete a field, choose Delete in the option’s menu of that field’s row. You can’t delete fields that are in a production schema.
6. Click Save Changes. CloudKit adds the new fields to the schema.

![A screenshot showing a container’s record types on the schema management page of the CloudKit Dashboard app. The screenshot highlights the Record Types menu item in the Schema section on the left, as well as the New Record Type panel.](https://docs-assets.developer.apple.com/published/c3288df8dec299caee74d4a1e0be396a/media-3699108%402x.png)

##### Delete a Record Type

You can delete a record type only in the development environment and only when that record type isn’t in production. Deleting a record type also deletes any corresponding records from the database.

To delete a record type:

1. From the CloudKit Database App schema management page for your app’s container, select Record Types from the Schema section on the left.
2. In the Record Types panel, select the record type to delete.
3. When that type’s details appear, click the Delete button. You can’t delete record types that are part of a production schema.
4. Confirm that you want to delete the record type. CloudKit removes the record type and any corresponding records from the container.

![A screenshot showing a container’s record types on the schema management page of the CloudKit Database app. The screenshot highlights the Record Types menu item in the Schema section on the left, as well as the Record Type details dialog on the right.](https://docs-assets.developer.apple.com/published/cef088d0cb85a6b32603033158c08803/media-3699107%402x.png)

## See Also

- [Handling an iCloud Container’s Data](handling-an-icloud-container-s-data.md)
  Inspect and manage your app’s iCloud container data using the CloudKit Database app.
- [Deploying an iCloud Container’s Schema](deploying-an-icloud-container-s-schema.md)
  Reset your container’s state during development and deploy your container’s schema to production.
- [Obtaining an API Token for an iCloud Container](obtaining-an-api-token-for-an-icloud-container.md)
  Generate an API token to access CloudKit web services or use CloudKit JS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/inspecting-and-editing-an-icloud-container-s-schema)*