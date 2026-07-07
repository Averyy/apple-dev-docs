# inserted

**Framework**: FinanceKit  
**Kind**: property

An array of model objects the framework inserted into the finance store.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
let inserted: [Model]
```

## See Also

- [let deleted: [Model.ID]](financestore/changes/deleted.md)
  An array of model objects identifiers that the framework deleted from the finance store.
- [let newToken: FinanceStore.HistoryToken](financestore/changes/newtoken.md)
  An updated history token that you can use to query more historical data.
- [let updated: [Model]](financestore/changes/updated.md)
  An array of model objects that the framework updated in the finance store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/changes/inserted)*