# add(_:)

**Framework**: CloudKit  
**Kind**: method

Executes the specified operation in the current database.

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
func add(_ operation: CKDatabaseOperation)
```

#### Discussion

Configure the operation fully before you call this method. Prior to the operation executing, CloudKit sets its [`database`](ckdatabaseoperation/database.md) property to the current database. The operation executes at the priority and quality of service (QoS) that you specify using the [`queuePriority`](https://developer.apple.com/documentation/Foundation/Operation/queuePriority-swift.property) and [`qualityOfService`](https://developer.apple.com/documentation/Foundation/Operation/qualityOfService) properties.

## Parameters

- `operation`: The operation to execute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/add(_:))*