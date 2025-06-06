# performQuery

**Framework**: CloudKit JS  
**Kind**: method

Fetches records by using a query.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.QueryResponse, CloudKit.CKError> performQuery(
	CloudKit.Query|CloudKit.QueryResponse query,
	optional Object options
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.QueryResponse`](cloudkit.queryresponse.md) object if the operation succeeds; otherwise, a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

To fetch records that match some criteria, create a [`CloudKit.Query`](cloudkit.query.md) dictionary.

```javascript
var query = {
    recordType: 'Artwork',
    filterBy: [{
        comparator: 'EQUALS',
        fieldName: 'address',
        fieldValue: { value: 'Fort Bragg, CA' }
    }]
}
```

Execute the query using the [`performQuery`](cloudkit.database/performquery.md) method. To get the records that were fetched, use the [`records`](cloudkit.recordsresponse/records.md) property in the [`CloudKit.QueryResponse`](cloudkit.queryresponse.md) class. Otherwise, handle any errors appropriately.

```javascript
database.performQuery(query).then(function(response) {
    if (response.hasErrors) {
        // Insert error handling
        throw response.errors[0];
    } else {
        // Insert successfully fetched record code
    }
});
```

Creating Queries That Search by Location

You can fetch records whose `Location` field lies within a circular region by specifying the center and radius of a circle in a [`CloudKit.Query`](cloudkit.query.md) dictionary. The `Location` field specified in the query must be indexed for the fetch to succeed.

```javascript
var query = {
    recordType: 'Artwork',
    filterBy: [{
        fieldName: 'location',
        distance: 100000,
        fieldValue: {
           latitude: 37.7749300,
           longitude: -122.4194200
       }
    }]
};
```

Execute this query using the [`performQuery`](cloudkit.database/performquery.md) method.

Handling Large Numbers of Results

If the results of a fetch exceeds the maximum number of records allowed in a response, perform the fetch again until all the records are fetched. You can also specify the results limit when performing a query.

To set a results limit, pass a dictionary as the `options` parameter to the [`performQuery`](cloudkit.database/performquery.md) method. In the dictionary, set the `resultsLimit` key to the number of records you want to fetch for each operation. If the `moreComing` property of the response object is `true`, the results exceeded the limit and you should perform the fetch operation again until `moreComing` is false. The next time you perform the operation, pass the response object to the [`performQuery`](cloudkit.database/performquery.md) method. The response object contains the fetch options you passed the first time you called the method.

For example, perform a query limiting the results to 10 records until all records matching the query are fetched.

```javascript
database.performQuery(query, { resultsLimit: 10 }).then(function(response) {
    if (response.hasErrors) {
        // Insert error handling
        throw response.errors[0];
    } else {
        // Insert successfully fetched record code
        if(response.moreComing) {
            return database.performQuery(response);
        }
    }
});
```

For the maximum number of records in a response and other data limits, see [`Data Size Limits`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/PropertyMetrics.html#//apple_ref/doc/uid/TP40015240-CH23) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## Parameters

- `query`: Either a   dictionary or a   object describing the matching criteria.
- `options`: A dictionary containing options to use when fetching records. Possible dictionary keys are:

## See Also

- [saveRecords](cloudkit.database/saverecords.md)
  Saves records to the database.
- [fetchRecords](cloudkit.database/fetchrecords.md)
  Fetches one or more records.
- [deleteRecords](cloudkit.database/deleterecords.md)
  Deletes one or more records.
- [newRecordsBatch](cloudkit.database/newrecordsbatch.md)
  Creates records batch builder object for modifying multiple records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/performquery)*