# resultsLimit

**Framework**: CloudKit JS  
**Kind**: property

The maximum number of records to fetch.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute Number resultsLimit;
```

#### Discussion

The default is the maximum number of records in a response that is allowed, described in [`Data Size Limits`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/PropertyMetrics.html#//apple_ref/doc/uid/TP40015240-CH23) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## See Also

- [moreComing](cloudkit.queryresponse/morecoming.md)
  A Boolean value that indicates whether there are more records to fetch.
- [zoneID](cloudkit.queryresponse/zoneid.md)
  A [`CloudKit.ZoneID`](cloudkit.zoneid.md) dictionary that identifies a record zone in the database.
- [continuationMarker](cloudkit.queryresponse/continuationmarker.md)
  Marks the location of the last batch of results.
- [desiredKeys](cloudkit.queryresponse/desiredkeys.md)
  An array of strings containing record field names that limits the amount of data returned in this operation.
- [zoneWide](cloudkit.queryresponse/zonewide.md)
  A Boolean value that determines whether all zones should be searched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.queryresponse/resultslimit)*