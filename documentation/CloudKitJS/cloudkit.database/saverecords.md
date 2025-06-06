# saveRecords

**Framework**: CloudKit JS  
**Kind**: method

Saves records to the database.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.RecordsResponse, CloudKit.CKError> saveRecords(
	CloudKit.Record|CloudKit.Record[] records,
	optional Object options
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.RecordZonesResponse`](cloudkit.recordzonesresponse.md) object, or if the operation fails, a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

Before saving records, create the record dictionaries with the appropriate key-value pairs. For `Asset` field types, provide a handler to upload the asset file separately. After fetching a record containing an `Asset` field type, you download the asset file separately.

Creating Records

Create a record represented by a [`CloudKit.Record`](cloudkit.record.md) dictionary. If you are creating a new record, the `recordType` is required. (If the record exists, the `recordChangeTag` key is required. ) If you omit the `recordName` key, the record is assigned a random UUID. Don’t include the other keys in the [`CloudKit.Record`](cloudkit.record.md) dictionary when creating a record for the first time. This code fragment shows a new `Artwork` record:

```javascript
var record = {
    recordName: '115',
    recordType: 'Artwork',
    fields: {
        title: {
            value: 'MacKerricher State Park'
        },
        address: {
            value: 'Fort Bragg, CA'
        }
    }
};
```

Saving Records

To get the record that was saved in the response, use the [`records`](cloudkit.recordsresponse/records.md) property in the [`CloudKit.RecordsResponse`](cloudkit.recordsresponse.md) class. Otherwise, handle any errors that occur appropriately.

```javascript
database.saveRecords(record).then(function(response) {
    if (response.hasErrors) {
        var ckError = response.errors[0];
        // Insert error handling or throw the error and handle it using catch() later
        throw ckError;
    } else {
        // Insert successfully saved record code
        var record = response.records[0];
    }
});
```

Saving Records with Asset Fields

Use an `Asset` field type in your schema to store large data files separately from the associated record. In CloudKit JS, the value of an `Asset` field is an `Asset` dictionary, described in [`Asset Dictionary`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/Types.html#//apple_ref/doc/uid/TP40015240-CH3-SW3).

To save a record with an asset field, set a handler for uploading the asset file in HTML.

```javascript
<input type="file" onchange="handleFileSelect">
```

In JavaScript, implement the handler to save the record with the uploaded data. For example, save the `image` property (`Asset`) of an `Artwork` record.

```javascript
function handleFileSelect(event) {
   var assetFile = event.target.files[0];
   database.saveRecords({
       recordType: 'Artwork',
       fields: {
           image: { value: assetFile }
       }
   }).then(function(response) {
       if (response.hasErrors) {
           // Insert error handling
           throw response.errors[0];
       } else {
           // Insert successfully saved record code
           var savedRecord = response.records[0];
       }
   });
}
```

In a record that is being saved to the database, the value of an `Asset` field must be a `window.Blob` type. In the code fragment above, the type of the `assetFile` variable is `window.File`.

Downloading Assets

To download an asset, use the `downloadURL` key in the returned or fetched `Asset` dictionary. The `downloadURL` key is included in the `Asset` dictionary in the response when you successfully save a record and later, when fetching a record.

```javascript
var asset = record.fields[__'__image__'__];
var assetURL = asset.value.downloadURL;
```

The `downloadURL` contains a placeholder (`${f}`) for the filename. If you allow the user to download an asset to their computer, replace the placeholder with a filename.

```javascript
assetURL.replace('${f}', 'image.png');
```

## Parameters

- `records`: Possible values are:
- `options`: A dictionary containing options to use when saving records. Possible dictionary keys are:

## See Also

- [fetchRecords](cloudkit.database/fetchrecords.md)
  Fetches one or more records.
- [deleteRecords](cloudkit.database/deleterecords.md)
  Deletes one or more records.
- [performQuery](cloudkit.database/performquery.md)
  Fetches records by using a query.
- [newRecordsBatch](cloudkit.database/newrecordsbatch.md)
  Creates records batch builder object for modifying multiple records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/saverecords)*