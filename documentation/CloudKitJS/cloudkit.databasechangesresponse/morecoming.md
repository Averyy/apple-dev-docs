# moreComing

**Framework**: CloudKit JS  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates there are more database changes to fetch.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
readonly attribute Boolean moreComing;
```

#### Discussion

`true` if there are more database changes to fetch; otherwise, `false`.

## See Also

### Response Properties
- [syncToken](./synctoken.md)
  A point in the database’s change history.
- [zones](./zones.md)
  The zones in the database where the changes occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.databasechangesresponse/morecoming)*