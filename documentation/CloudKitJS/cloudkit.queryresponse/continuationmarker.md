# continuationMarker

**Framework**: CloudKit JS  
**Kind**: property

Marks the location of the last batch of results.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute String continuationMarker;
```

#### Discussion

Pass this key to another [`performQuery`](cloudkit.database/performquery.md) method call when the results of a previous fetch exceed the maximum.

## See Also

- [moreComing](cloudkit.queryresponse/morecoming.md)
  A Boolean value that indicates whether there are more records to fetch.
- [zoneID](cloudkit.queryresponse/zoneid.md)
  A [`CloudKit.ZoneID`](cloudkit.zoneid.md) dictionary that identifies a record zone in the database.
- [resultsLimit](cloudkit.queryresponse/resultslimit.md)
  The maximum number of records to fetch.
- [desiredKeys](cloudkit.queryresponse/desiredkeys.md)
  An array of strings containing record field names that limits the amount of data returned in this operation.
- [zoneWide](cloudkit.queryresponse/zonewide.md)
  A Boolean value that determines whether all zones should be searched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.queryresponse/continuationmarker)*