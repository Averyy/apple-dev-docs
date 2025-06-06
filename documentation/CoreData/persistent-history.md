# Persistent history

**Framework**: Core Data

Use persistent history tracking to determine what changes have occurred in the store since the enabling of persistent history tracking.

## Topics

### Tracking History
- [class NSPersistentHistoryToken](nspersistenthistorytoken.md)
  A bookmark for keeping track the most recent history that you’ve processed.
### Requesting History
- [class NSPersistentHistoryChangeRequest](nspersistenthistorychangerequest.md)
  A request to fetch or purge persistent history.
- [class NSPersistentHistoryResult](nspersistenthistoryresult.md)
  The result of a request to fetch persistent history.
### Reading History
- [class NSPersistentHistoryTransaction](nspersistenthistorytransaction.md)
  A set of changes in the persistent history based on a context save or batch operation.
- [class NSPersistentHistoryChange](nspersistenthistorychange.md)
  A change representing the insertion, update, or deletion of a managed object in the persistent store.

## See Also

- [Accessing data when the store changes](accessing-data-when-the-store-changes.md)
  Guarantee that a context won’t see store changes until you tell it to look.
- [Consuming relevant store changes](consuming-relevant-store-changes.md)
  Filter store transactions for changes relevant to the current view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/persistent-history)*