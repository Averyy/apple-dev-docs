# execute()

**Framework**: Core Data  
**Kind**: method

Executes the fetch request against the managed object context that is associated with the current queue.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func execute() throws -> [ResultType]
```

#### Discussion

Calling `execute` on an [`NSFetchRequest`](nsfetchrequest.md) will cause the [`NSFetchRequest`](nsfetchrequest.md) to run against the managed object context ([`NSManagedObjectContext`](nsmanagedobjectcontext.md)) that is associated with the queue on which the `execute` is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/execute())*