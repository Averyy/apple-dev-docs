# zoneWide

**Framework**: CloudKit JS  
**Kind**: property

A Boolean value that determines whether all zones should be searched.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute Boolean zoneWide;
```

#### Discussion

If `true`, all zones are searched. If `false`, only the default zone is searched.

## See Also

- [zoneID](cloudkit.queryresponse/zoneid.md)
  A [`CloudKit.ZoneID`](cloudkit.zoneid.md) dictionary that identifies a record zone in the database.
- [resultsLimit](cloudkit.queryresponse/resultslimit.md)
  The maximum number of records to fetch.
- [continuationMarker](cloudkit.queryresponse/continuationmarker.md)
  Marks the location of the last batch of results.
- [desiredKeys](cloudkit.queryresponse/desiredkeys.md)
  An array of strings containing record field names that limits the amount of data returned in this operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.queryresponse/zonewide)*