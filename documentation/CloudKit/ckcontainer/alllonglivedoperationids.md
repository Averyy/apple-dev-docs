# allLongLivedOperationIDs()

**Framework**: CloudKit  
**Kind**: method

Fetches the IDs of any long-lived operations that are running and returns them to an awaiting caller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func allLongLivedOperationIDs() async throws -> [CKOperation.ID]
```

#### Return Value

The IDs of all of the long-lived operations that are running.

#### Discussion

A long-lived operation is one that continues to run after the user closes your app. When a long-lived operation completes, or your app or the system cancels it, it’s no longer active and CloudKit doesn’t include its ID in the returned array. An operation is complete when the system calls its completion handler.

Use the [`longLivedOperation(for:)`](ckcontainer/longlivedoperation(for:).md) method to fetch the operation for a specific ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/alllonglivedoperationids())*