# longLivedOperation(for:)

**Framework**: CloudKit  
**Kind**: method

Fetches the long-lived operation for the specified operation ID and returns it to an awaiting caller.

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
func longLivedOperation(for operationID: CKOperation.ID) async throws -> CKOperation?
```

#### Return Value

The long-lived operation, or `nil` if the operation completes, or your app or the system cancels it

#### Discussion

A long-lived operation is one that continues to run after the user closes your app. When a long-lived operation completes, the system calls its completion block to notify you.

After setting callback blocks on the returned long-lived operation, and starting the returned long-lived operation on an operation queue, the operation invokes all callbacks made while your app was closed.

## Parameters

- `operationID`: The operation’s ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/longlivedoperation(for:))*