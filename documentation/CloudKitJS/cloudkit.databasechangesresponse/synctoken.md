# syncToken

**Framework**: CloudKit JS  
**Kind**: property

A point in the database’s change history.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute String syncToken;
```

#### Discussion

If [`moreComing`](cloudkit.databasechangesresponse/morecoming.md) is `true` in the response, use the this property in the next request until [`moreComing`](cloudkit.databasechangesresponse/morecoming.md) is `false`.

## See Also

- [moreComing](cloudkit.databasechangesresponse/morecoming.md)
  A Boolean value that indicates there are more database changes to fetch.
- [zones](cloudkit.databasechangesresponse/zones.md)
  The zones in the database where the changes occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.databasechangesresponse/synctoken)*