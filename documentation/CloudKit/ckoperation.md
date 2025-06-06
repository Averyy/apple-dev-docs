# CKOperation

**Framework**: CloudKit  
**Kind**: class

The abstract base class for all operations that execute in a database.

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
class CKOperation
```

## Mentions

- [Encrypting User Data](encrypting-user-data.md)
- [Deciding whether CloudKit is right for your app](deciding-whether-cloudkit-is-right-for-your-app.md)

#### Overview

All CloudKit operations descend from `CKOperation`, which provides the infrastructure for executing tasks in one of your app’s containers. Don’t subclass or create instances of this class directly. Instead, create instances of one of its concrete subclasses.

Use the properties of this class to configure the behavior of the operation before submitting it to a queue or executing it directly. CloudKit operations involve communicating with the iCloud servers to send and receive data. You can use the properties of this class to configure the behavior of those network requests to ensure the best performance for your app.

> ❗ **Important**:  `CKOperation` objects have a default quality of service level of [`QualityOfService.default`](https://developer.apple.com/documentation/Foundation/QualityOfService/default) (see [`qualityOfService`](https://developer.apple.com/documentation/foundation/operation/1413553-qualityofservice)). Operations with this service level are discretionary, and the system schedules them for an optimal time according to battery level and other factors. On iPhone, discretionary activities pause when the device is in Low Power Mode. For information about quality of service levels, see [`Prioritize Work with Quality of Service Classes`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html#//apple_ref/doc/uid/TP40015243-CH39) in [`Energy Efficiency Guide for iOS Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html#//apple_ref/doc/uid/TP40015243) and [`Prioritize Work at the Task Level`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/PrioritizeWorkAtTheTaskLevel.html#//apple_ref/doc/uid/TP40013929-CH35) in [`Energy Efficiency Guide for Mac Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929).

 `CKOperation` objects have a default quality of service level of [`QualityOfService.default`](https://developer.apple.com/documentation/Foundation/QualityOfService/default) (see [`qualityOfService`](https://developer.apple.com/documentation/foundation/operation/1413553-qualityofservice)). Operations with this service level are discretionary, and the system schedules them for an optimal time according to battery level and other factors. On iPhone, discretionary activities pause when the device is in Low Power Mode. For information about quality of service levels, see [`Prioritize Work with Quality of Service Classes`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html#//apple_ref/doc/uid/TP40015243-CH39) in [`Energy Efficiency Guide for iOS Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html#//apple_ref/doc/uid/TP40015243) and [`Prioritize Work at the Task Level`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/PrioritizeWorkAtTheTaskLevel.html#//apple_ref/doc/uid/TP40013929-CH35) in [`Energy Efficiency Guide for Mac Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929).

##### Long Lived Operations

A  is an operation that continues to run after the user closes the app. To specify a long-lived operation, set [`isLongLived`](ckoperation/islonglived.md) to [`true`](https://developer.apple.com/documentation/swift/true), provide a completion handler, and execute the operation. To get the identifiers of all running long-lived operations, use the [`fetchAllLongLivedOperationIDsWithCompletionHandler:`](ckcontainer/fetchalllonglivedoperationidswithcompletionhandler:.md) method that [`CKContainer`](ckcontainer.md) provides. To get a specific long-lived operation, use the [`fetchLongLivedOperationWithID:completionHandler:`](ckcontainer/fetchlonglivedoperationwithid:completionhandler:.md) method. Make sure you set the completion handler of a long-lived operation before you execute it so that the system can notify you when it completes and you can process the results. Do not execute an operation, change it to long-lived, and execute it again as a long-lived operation.

The following is the typical life cycle of a long-lived operation:

1. The app creates a long-lived operation and executes it.

The daemon starts saving and sending the callbacks to the running app. 2. The app exits.

The daemon continues running the long-lived operation and saves the callbacks. 3. The app launches and fetches the long-lived operation.

If the operation is running or if it completed within the previous 24 hours, the daemon returns a proxy for the long-lived operation. If the operation completed more than 24 hours previously, the daemon may stop returning it in fetch requests. 4. The app runs the long-lived operation again.

The daemon sends the app all the saved callbacks (it doesn’t actually rerun the operation), and continues saving the callbacks and sending them to the running app. 5. The app receives the completion callback or the app cancels the operation.

The daemon stops including the operation in future fetch results.

## Topics

### Creating an Operation
- [init()](ckoperation/init.md)
  Creates an operation.
### Identifying the Operation
- [var operationID: CKOperation.ID](ckoperation/operationid-8auuc.md)
  A unique identifier for a long-lived operation.
- [CKOperation.ID](ckoperation/id.md)
  A type that represents the ID of an operation.
### Managing the Operation’s Configuration
- [var configuration: CKOperation.Configuration!](ckoperation/configuration-swift.property.md)
  The operation’s configuration.
- [CKOperation.Configuration](ckoperation/configuration-swift.class.md)
  An object that describes how a CloudKit operation behaves.
- [var group: CKOperationGroup?](ckoperation/group.md)
  The operation’s group.
- [var longLivedOperationWasPersistedBlock: (() -> Void)?](ckoperation/longlivedoperationwaspersistedblock.md)
  The closure to execute when the server begins to store callbacks for the long-lived operation.
### Deprecated
- [Deprecated Symbols](ckoperation-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [Operation](../Foundation/Operation.md)
### Inherited By
- [CKAcceptSharesOperation](ckacceptsharesoperation.md)
- [CKDatabaseOperation](ckdatabaseoperation.md)
- [CKDiscoverAllUserIdentitiesOperation](ckdiscoveralluseridentitiesoperation.md)
- [CKDiscoverUserIdentitiesOperation](ckdiscoveruseridentitiesoperation.md)
- [CKFetchShareMetadataOperation](ckfetchsharemetadataoperation.md)
- [CKFetchShareParticipantsOperation](ckfetchshareparticipantsoperation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation)*