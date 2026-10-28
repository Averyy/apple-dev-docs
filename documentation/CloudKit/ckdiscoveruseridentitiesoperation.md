# CKDiscoverUserIdentitiesOperation

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An operation that uses the provided criteria to search for discoverable iCloud users.

**Availability**:
- iOS 10.0+ - Deprecated in 17.0
- iPadOS 10.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.12+ - Deprecated in 14.0
- tvOS 10.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 10.0

> **Deprecated**: No longer supported. Please see Sharing CloudKit Data with Other iCloud Users.

## Declaration

```swift
class CKDiscoverUserIdentitiesOperation
```

```objc
@interface CKDiscoverUserIdentitiesOperation : CKOperation
```

## Overview

Use this operation to discover one or more iCloud users that match identity information you provide, such as email addresses and phone numbers.

Before CloudKit can return a user’s identity, you must ask for their permission by calling [`requestApplicationPermission(_:completionHandler:)`](./ckcontainer/requestapplicationpermission%28_,completionhandler%29.md). Do this as part of any onboarding where you can highlight the benefits of being discoverable within the context of your app.

The operation executes the handlers you provide on an internal queue it manages. You must provide handlers capable of executing on a background queue. Tasks that need access to the main queue must redirect as appropriate.

The operation calls [`discoverUserIdentitiesCompletionBlock`](./ckdiscoveruseridentitiesoperation/discoveruseridentitiescompletionblock.md) after it executes and returns results. Use the completion handler to perform housekeeping tasks for the operation. It should also manage any failures, whether due to an error or an explicit cancellation.

> **Note**: Because this class inherits from [`Operation`](../Foundation/operation.md), you can also set the [`completionBlock`](../Foundation/operation/completionblock.md) property. The operation calls both completion handlers if they’re both set.

CloudKit operations have a default QoS of [`QualityOfService.default`](../Foundation/qualityofservice/default.md). Operations with this service level are discretionary. The system schedules their execution at an optimal time according to battery level and network conditions, among other factors. Use the [`qualityOfService`](../Foundation/operation/qualityofservice.md) property to set a more appropriate QoS for the operation.

The following example shows how to create the operation, configure its callbacks, and execute it using the default container’s queue:

```swift
func fetchUserIdentities(withEmails emails: [String],
    completion: @escaping (Result<[CKUserIdentity], any Error>) -> Void) {

    var identities = [CKUserIdentity]()

    // Convert the email addresses into instances of
    // CKUserIdentity.LookupInfo, which CloudKit uses
    // to discover identities.
    let lookupInfos =
        CKUserIdentity.LookupInfo.lookupInfos(withEmails: emails)

    // Create the operation using the array of lookup objects.
    let operation = CKDiscoverUserIdentitiesOperation(
        userIdentityLookupInfos: lookupInfos)

    // Cache the user identities as CloudKit discovers them.
    operation.userIdentityDiscoveredBlock = { userIdentity, _ in
        identities.append(userIdentity)
    }

    // If the operation fails, return the error to the caller.
    // Otherwise, return the array of discovered user identities.
    operation.discoverUserIdentitiesCompletionBlock = { error in
        if let error = error {
            completion(.failure(error))
        } else {
            completion(.success(identities))
        }
    }

    // Set an appropriate QoS and add the operation to the
    // default container's queue to execute it.
    operation.qualityOfService = .userInitiated
    CKContainer.default().add(operation)
}
```

## Topics

### Creating an Operation
- [init()](./ckdiscoveruseridentitiesoperation/init%28%29.md)
  Creates an operation for discovering user identities.
- [convenience init(userIdentityLookupInfos: [CKUserIdentity.LookupInfo])](./ckdiscoveruseridentitiesoperation/init%28useridentitylookupinfos%29.md)
  Creates an operation for discovering the user identities of the specified lookup infos.
### Configuring the Operation
- [var userIdentityLookupInfos: [CKUserIdentity.LookupInfo]](./ckdiscoveruseridentitiesoperation/useridentitylookupinfos.md)
  The lookup info for discovering user identities.
### Processing the Results
- [var userIdentityDiscoveredBlock: ((CKUserIdentity, CKUserIdentity.LookupInfo) -> Void)?](./ckdiscoveruseridentitiesoperation/useridentitydiscoveredblock.md)
  The closure to execute for each user identity.
- [var discoverUserIdentitiesCompletionBlock: (((any Error)?) -> Void)?](./ckdiscoveruseridentitiesoperation/discoveruseridentitiescompletionblock.md)
  The closure to execute when the operation finishes.
### Instance Properties
- [var discoverUserIdentitiesResultBlock: ((Result<Void, any Error>) -> Void)?](./ckdiscoveruseridentitiesoperation/discoveruseridentitiesresultblock.md)
  The closure to execute when the operation finishes.

## Relationships

### Inherits From
- [CKOperation](./ckoperation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated classes
- [class CKDiscoverAllUserIdentitiesOperation](./ckdiscoveralluseridentitiesoperation.md)
  An operation that uses the device’s contacts to search for discoverable iCloud users.
- [class CKFetchRecordChangesOperation](./ckfetchrecordchangesoperation.md)
  An operation that reports on the changed and deleted records in the specified record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation)*