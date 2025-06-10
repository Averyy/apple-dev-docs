# Providing User Access to CloudKit Data

**Framework**: CloudKit

Provide users access to the data your app stores on their behalf.

#### Overview

User data in CloudKit belongs to the user. For this reason, apps that integrate with CloudKit need to provide users with a way to view and export their data.

##### Identify Containers and Record Types

To be sure that you’re querying all of the data that your app stores, cross-reference the list of containers your app has access to in Xcode, and assemble a list of those containers’ identifiers.

The CloudKit Dashboard lists the different record types you define for each container in your app. Assemble a list of these types and make sure that each type has a queryable index on its `recordName` field.

##### Associate Record Types with Containers

Associate the record types with the container they appear in. The example below uses a dictionary to represent the relationship between containers and the record types they contain:

```swift
let defaultContainer = CKContainer.default()
let documents = CKContainer(identifier: "iCloud.com.example.myexampleapp.documents")
let settings = CKContainer(identifier: "iCloud.com.example.myexampleapp.settings")

let containerRecordTypes: [CKContainer: [String]] = [
    defaultContainer: ["log", "verboseLog"],
    documents: ["textDocument", "spreadsheet"],
    settings: ["preference", "profile"]
]

let containers = Array(containerRecordTypes.keys)
```

##### Find and List All Records

Store user data in a container’s private database. Use the containers in the example above to find all record zones in the private database for each container that your app uses.

The example below shows how to iterate over the containers, record zones, and records. It also shows how to list the fields for each record, which you use to show the data in those records:

```swift
// Utility function to display records.
// Customize it to display records appropriately
// according to your app's unique record types.
func printRecords(_ records: [CKRecord]) {
    for record in records {
        for key in record.allKeys() {
            let value = record[key]
            print(key + " = " + (value?.description ?? "") + ")")
        }
    }
}

for container in containers {
    // User data should be stored in the private database.
    let database = container.privateCloudDatabase
    
    database.fetchAllRecordZones { zones, error in
        guard let zones = zones, error == nil else {
            print(error!)
            return
        }
        
        // The true predicate represents a query for all records.
        let alwaysTrue = NSPredicate(value: true)
        for zone in zones {
            for recordType in containerRecordTypes[container] ?? [] {
                let query = CKQuery(recordType: recordType, predicate: alwaysTrue)
                database.perform(query, inZoneWith: zone.zoneID) { records, error in
                    guard let records = records, error == nil else {
                        print("An error occurred fetching these records.")
                        return
                    }
                    
                    printRecords(records)
                }
            }
        }
    }
}
```

Use each field’s keys and values to give users an accessible report of the data your app stores in CloudKit.

> **Note**:  If your app uses CloudKit subscriptions to maintain an on-device copy of user data, you can use that copy to generate the report rather than querying CloudKit.

## See Also

- [Encrypting User Data](encrypting-user-data.md)
  Deploy industry-standard security technologies using CloudKit encryption.
- [Changing Access Controls on User Data](changing-access-controls-on-user-data.md)
  Restrict access to or remove restrictions from a user’s data at their request.
- [class CKFetchWebAuthTokenOperation](ckfetchwebauthtokenoperation.md)
  An operation that creates an authentication token for use with CloudKit web services.
- [Responding to Requests to Delete Data](responding-to-requests-to-delete-data.md)
  Provide options for users to delete their CloudKit data from your app.
- [Identifying an App’s Containers](identifying-an-app-s-containers.md)
  Use Xcode’s Project navigator to find the identifiers of active CloudKit containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/providing-user-access-to-cloudkit-data)*