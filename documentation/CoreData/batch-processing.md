# Batch processing

**Framework**: Core Data

Use batch processes to manage large data changes.

## Topics

### Data Inserts
- [class NSBatchInsertRequest](nsbatchinsertrequest.md)
  A request to insert a batch of data in a persistent store.
- [class NSBatchInsertResult](nsbatchinsertresult.md)
  The result that Core Data returns when executing a batch-insertion request.
### Data Updates
- [class NSBatchUpdateRequest](nsbatchupdaterequest.md)
  A request to Core Data to do a batch update of data in a persistent store without loading any data into memory.
- [class NSBatchUpdateResult](nsbatchupdateresult.md)
  The result returned when executing a batch update request.
### Data Deletion
- [class NSBatchDeleteRequest](nsbatchdeleterequest.md)
  A request that deletes objects in the SQLite persistent store without loading them into memory.
- [class NSBatchDeleteResult](nsbatchdeleteresult.md)
  An object that describes the result of a batch delete request.

## See Also

- [Using Core Data in the background](using-core-data-in-the-background.md)
  Use Core Data in both a single-threaded and multithreaded app.
- [Loading and displaying a large data feed](../SwiftUI/loading-and-displaying-a-large-data-feed.md)
  Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [Conflict resolution](conflict-resolution.md)
  Detect and resolve conflicts that occur when data is changed on multiple threads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/batch-processing)*