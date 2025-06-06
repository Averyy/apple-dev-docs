# add(_:)

**Framework**: CloudKit  
**Kind**: method

Adds an operation to the container’s queue.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func add(_ operation: CKOperation)
```

#### Discussion

This method adds the operation to a queue that the container manages. The queue’s operations execute on background threads concurrently, and with default priorities. When you add an operation to the queue, its container becomes the current container.

## Parameters

- `operation`: The operation to add to the queue. Make sure you fully configure the operation and have it ready to execute. Don’t change the operation’s configuration after you queue it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/add(_:))*