# syncToken

**Framework**: CloudKit JS  
**Kind**: property  
**Role**: Instance Property

A point in the database’s change history.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
readonly attribute String syncToken;
```

## Discussion

If [`moreComing`](./morecoming.md) is `true` in the response, use the this property in the next request until [`moreComing`](./morecoming.md) is `false`.

## See Also

### Response Properties
- [moreComing](./morecoming.md)
  A Boolean value that indicates there are more database changes to fetch.
- [zones](./zones.md)
  The zones in the database where the changes occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.databasechangesresponse/synctoken)*