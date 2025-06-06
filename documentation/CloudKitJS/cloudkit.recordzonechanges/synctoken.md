# syncToken

**Framework**: CloudKit JS  
**Kind**: property

Identifies a point in the zone’s change history. The first time you get record changes, omit this key and if `moreComing` is `true` in the response, use the `syncToken` in the response in the next request until `moreComing` is `false`. Otherwise, get the current sync token by fetching a zone.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
attribute String syncToken;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordzonechanges/synctoken)*