# Conflict resolution

**Framework**: Core Data

Detect and resolve conflicts that occur when data is changed on multiple threads.

## Topics

### Conflict Management
- [class NSConstraintConflict](nsconstraintconflict.md)
  An encapsulation of conflicts that occur during an attempt to save a managed object.
- [class NSMergeConflict](nsmergeconflict.md)
  An encapsulation of conflicts that occur during an attempt to save changes in a managed object context.
- [class NSMergePolicy](nsmergepolicy.md)
  A policy object that you use to resolve conflicts between the persistent store and in-memory versions of managed objects.
- [class NSQueryGenerationToken](nsquerygenerationtoken.md)
  A token that indicates which generation of the persistent store is being accessed.

## See Also

- [Using Core Data in the background](using-core-data-in-the-background.md)
  Use Core Data in both a single-threaded and multithreaded app.
- [Loading and displaying a large data feed](../SwiftUI/loading-and-displaying-a-large-data-feed.md)
  Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [Batch processing](batch-processing.md)
  Use batch processes to manage large data changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/conflict-resolution)*