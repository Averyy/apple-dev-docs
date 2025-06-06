# desiredKeys

**Framework**: CloudKit JS  
**Kind**: property

An array of strings containing record field names that limits the amount of data returned in this operation.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute String[] desiredKeys;
```

#### Discussion

The default is `null`, which fetches all record fields.

## See Also

- [zoneID](cloudkit.queryresponse/zoneid.md)
  A [`CloudKit.ZoneID`](cloudkit.zoneid.md) dictionary that identifies a record zone in the database.
- [resultsLimit](cloudkit.queryresponse/resultslimit.md)
  The maximum number of records to fetch.
- [continuationMarker](cloudkit.queryresponse/continuationmarker.md)
  Marks the location of the last batch of results.
- [zoneWide](cloudkit.queryresponse/zonewide.md)
  A Boolean value that determines whether all zones should be searched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.queryresponse/desiredkeys)*