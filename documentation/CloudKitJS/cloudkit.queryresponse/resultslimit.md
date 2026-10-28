# resultsLimit

**Framework**: CloudKit JS  
**Kind**: property  
**Role**: Instance Property

The maximum number of records to fetch.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
readonly attribute Number resultsLimit;
```

## Discussion

The default is the maximum number of records in a response that is allowed, described in [Data Size Limits](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/PropertyMetrics.html#//apple_ref/doc/uid/TP40015240-CH23) in [CloudKit Web Services Reference](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## See Also

### Related Documentation
- [moreComing](./morecoming.md)
  A Boolean value that indicates whether there are more records to fetch.
### Accessing Request Properties
- [zoneID](./zoneid.md)
  A [`CloudKit.ZoneID`](../cloudkit.zoneid.md) dictionary that identifies a record zone in the database.
- [continuationMarker](./continuationmarker.md)
  Marks the location of the last batch of results.
- [desiredKeys](./desiredkeys.md)
  An array of strings containing record field names that limits the amount of data returned in this operation.
- [zoneWide](./zonewide.md)
  A Boolean value that determines whether all zones should be searched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.queryresponse/resultslimit)*