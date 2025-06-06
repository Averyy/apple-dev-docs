# desiredKeys

**Framework**: CloudKit  
**Kind**: property

The fields to fetch for the requested records.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var desiredKeys: [String]? { get set }
```

#### Discussion

Use this property to limit the amount of data that CloudKit retrieves for each record during the fetch operation. This property contains an array of strings, each of which is the name of a field from the target records. When you retrieve a record, CloudKit only includes fields with names that match one of the keys in this property. The default value is `nil`, which causes CloudKit to fetch all of the record’s keys.

Because the records you fetch can be of different types, configure the array to include the merged set of all field names for the requested records and at least one field name from each record type.

If you intend to specify the desired set of keys, set the value of this property before executing the operation or submitting it to a queue.

## See Also

- [var previousServerChangeToken: CKServerChangeToken?](ckfetchrecordzonechangesoperation/zoneoptions/previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var resultsLimit: Int](ckfetchrecordzonechangesoperation/zoneoptions/resultslimit.md)
  The maximum number of records to fetch from the record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneoptions/desiredkeys)*