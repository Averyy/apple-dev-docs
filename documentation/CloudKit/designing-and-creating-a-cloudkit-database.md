# Designing and Creating a CloudKit Database

**Framework**: CloudKit

Create a schema to store your app’s objects as records in iCloud using CloudKit.

#### Overview

After you enable CloudKit in your app, you create a  for your container that describes how to store your objects. A schema defines  and the possible relationships between them. A record type is a template for the allowed keys and values of a record. This relationship is analogous to how a class (record type) defines the properties an instance (record) can have.

##### Design Your Objects As Records

CloudKit allows you to store your data as [`CKRecord`](ckrecord.md) objects, and relationships between those objects as [`CKRecord.Reference`](ckrecord/reference.md) associations. Separate your data into record types by grouping objects of the same type together. If you’ve already separated your model data into classes, these classes might have the same record type in iCloud. Choose which objects and which of their properties and relationships you want to persist to iCloud.

Each object property that you persist maps to a key-value pair, known as a , within a [`CKRecord`](ckrecord.md). [`CKRecord`](ckrecord.md) supports value types for your fields, such as [`String`](https://developer.apple.com/documentation/Swift/String), or more complex types, such as [`Data`](https://developer.apple.com/documentation/Foundation/Data).

For example, a “to-do item” might have the following record type:

|  |  |  |
| --- | --- | --- |
| title | [`String`](https://developer.apple.com/documentation/Swift/String) | “Get apples” |
| dueDate | [`Date`](https://developer.apple.com/documentation/Foundation/Date) | October 28, 2019 |
| isCompleted | [`Bool`](https://developer.apple.com/documentation/Swift/Bool) | false |

For information on additional supported value types, see [`CKRecord`](ckrecord.md).

##### Create Records Programmatically

Create a [`CKRecord`](ckrecord.md) object with a string representing the type of record you want to store, using [`initWithRecordType:`](ckrecord/initwithrecordtype:.md). Every record type must have a unique string name.

```swift
let record = CKRecord(recordType: "ToDoItem")
```

Then set the record’s fields. Because [`CKRecord`](ckrecord.md) is key-value coding compliant, you can use [`setValuesForKeys(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/setValuesForKeys(_:)). The values you set could be from a details sheet that the user fills out.

```swift
record.setValuesForKeys([
    "title": "Get apples",
    "dueDate": DateComponents(
        calendar: Calendar.current,
        year: 2019,
        month: 10,
        day: 28).date!,
    "isCompleted": false // Stored as Int(64)
])
```

##### Save Initial Records to Icloud

You can create a schema using CloudKit Dashboard, or you can create a  by writing records programmatically.

To save a record to your container, you must pick a database to save the record to. Each container has a single  database accessible to all app users, and  databases for each user of your app. Also, a user may have a  database if that user is accessing another user’s shared private data. Note that every database within your app’s container shares the same schema.

Although an app can have multiple containers or can share a container, each app has one default container. You access the default container using [`default()`](ckcontainer/default().md) on [`CKContainer`](ckcontainer.md). The following example uses the current user’s private database within the app’s default container and exists in an action handler for a Save button.

```swift
let container = CKContainer.default()
let database = container.privateCloudDatabase
```

Save the record to the user’s private database in the app’s container.

```swift
database.save(record) { record, error in
    if let error = error {
        // Handle error.
        return
    }
    // Record saved successfully.
}
```

When you run your app, it adds that record type to the schema and saves the record. If the record type already exists in the schema, iCloud uses the existing type. Saving a record works only if the user has signed into their iCloud account on their device.

If saving the record to iCloud succeeds, `error` is `nil`. (If `error` is non-`nil`, see [`CKError`](ckerror.md) for possible values of `error.)`

> ❗ **Important**:  During development, you can change your schema as much as you want, but once it’s deployed to production, you can’t delete any part of it. You can only make additive changes, such as adding a new field to a record type, or adding new record types.

##### Handle or Prevent Errors Gracefully

When designing your app, consider how to handle or prevent error conditions. For example, an error occurs if your app attempts to save a record to a user’s private database and the user hasn’t yet signed in to iCloud. You might handle this scenario by checking whether the user has signed in before the app saves the record. If the user hasn’t signed in, present an alert. If they’re signed in, save the record.

The following example demonstrates preventing the error condition in this manner.

```swift
CKContainer.default().accountStatus { accountStatus, error in
    if accountStatus == .noAccount {
        DispatchQueue.main.async {
            let message = 
                """
                Sign in to your iCloud account to write records.
                On the Home screen, launch Settings, tap Sign in to your
                iPhone/iPad, and enter your Apple ID. Turn iCloud Drive on.
                """
            let alert = UIAlertController(
                title: "Sign in to iCloud",
                message: message,
                preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "OK", style: .cancel))
            self.present(alert, animated: true)
        }
    }
    else {
        // Save your record here.
    }
}
```

##### Run Your App

In Xcode, run your app to execute the code that saves records and creates the schema in the database. To verify success, see [`Inspecting and Editing an iCloud Container’s Schema`](inspecting-and-editing-an-icloud-container-s-schema.md).

## See Also

- [Managing iCloud Containers with CloudKit Database App](managing-icloud-containers-with-cloudkit-database-app.md)
  Inspect and modify the schema and data for your app’s iCloud container.
- [class CKRecordZone](ckrecordzone.md)
  A database partition that contains related records.
- [class CKRecord](ckrecord.md)
  A collection of key-value pairs that store your app’s data.
- [CKRecord.Reference](ckrecord/reference.md)
  A relationship between two records in a record zone.
- [class CKAsset](ckasset.md)
  An external file that belongs to a record.
- [Integrating a Text-Based Schema into Your Workflow](integrating-a-text-based-schema-into-your-workflow.md)
  Define and update your schema with the CloudKit Schema Language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/designing-and-creating-a-cloudkit-database)*