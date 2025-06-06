# fetchAllLongLivedOperationIDs(completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches the IDs of any long-lived operations that are running.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.2+
- visionOS ?+
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
@preconcurrency
func fetchAllLongLivedOperationIDs(completionHandler: @escaping ([CKOperation.ID]?, (any Error)?) -> Void)
```

#### Discussion

The closure doesn’t return a value and takes the following parameters:

- The IDs of all of the long-lived operations that are running.
- An error if a problem occurs, or `nil` if CloudKit successfully retrieves the IDs.

A long-lived operation is one that continues to run after the user closes your app. When a long-lived operation completes, or your app or the system cancels it, it’s no longer active and CloudKit doesn’t include its ID in `outstandingOperationsByIDs`. An operation is complete when the system calls its completion handler.

Use the [`fetchLongLivedOperationWithID:completionHandler:`](ckcontainer/fetchlonglivedoperationwithid:completionhandler:.md) method to fetch the operation for a specific ID.

## Parameters

- `completionHandler`: The closure to execute with the fetch results.

## See Also

- [func fetchLongLivedOperation(withID: CKOperation.ID, completionHandler: (CKOperation?, (any Error)?) -> Void)](ckcontainer/fetchlonglivedoperation(withid:completionhandler:).md)
  Fetches the long-lived operation for the specified operation ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/fetchalllonglivedoperationids(completionhandler:))*