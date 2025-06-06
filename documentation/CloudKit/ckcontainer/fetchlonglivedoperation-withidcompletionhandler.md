# fetchLongLivedOperation(withID:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches the long-lived operation for the specified operation ID.

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
func fetchLongLivedOperation(withID operationID: CKOperation.ID, completionHandler: @escaping (CKOperation?, (any Error)?) -> Void)
```

#### Discussion

The closure doesn’t return a value and takes the following parameters:

- The long-lived operation. If the operation completes, or your app or the system cancels it, this parameter is `nil`.
- An error if a problem occurs, or `nil` if CloudKit successfully retrieves the operation.

A long-lived operation is one that continues to run after the user closes your app. When a long-lived operation completes, the system calls its completion block to notify you.

## Parameters

- `operationID`: The operation’s ID.
- `completionHandler`: The closure to execute with the fetch results.

## See Also

- [func fetchAllLongLivedOperationIDs(completionHandler: ([CKOperation.ID]?, (any Error)?) -> Void)](ckcontainer/fetchalllonglivedoperationids(completionhandler:).md)
  Fetches the IDs of any long-lived operations that are running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/fetchlonglivedoperation(withid:completionhandler:))*