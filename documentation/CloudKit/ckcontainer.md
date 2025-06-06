# CKContainer

**Framework**: CloudKit  
**Kind**: class

A conduit to your app’s databases.

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
class CKContainer
```

## Mentions

- [Identifying an App’s Containers](identifying-an-app-s-containers.md)
- [Designing and Creating a CloudKit Database](designing-and-creating-a-cloudkit-database.md)

#### Overview

A container manages all explicit and implicit attempts to access its contents.

Every app has a default container that manages its own content. If you develop a suite of apps, you can access any containers that you have the appropriate entitlements for. Each new container distinguishes between public and private data. CloudKit always stores private data in the appropriate container directory in the user’s iCloud account.

> **Note**:  `CKContainer` instances operate with a [`QualityOfService.userInitiated`](https://developer.apple.com/documentation/Foundation/QualityOfService/userInitiated) quality of service level by default. For information about quality of service, see [`Prioritize Work with Quality of Service Classes`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html#//apple_ref/doc/uid/TP40015243-CH39) in [`Energy Efficiency Guide for iOS Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html#//apple_ref/doc/uid/TP40015243) and [`Prioritize Work at the Task Level`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/PrioritizeWorkAtTheTaskLevel.html#//apple_ref/doc/uid/TP40013929-CH35) in [`Energy Efficiency Guide for Mac Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929).

 `CKContainer` instances operate with a [`QualityOfService.userInitiated`](https://developer.apple.com/documentation/Foundation/QualityOfService/userInitiated) quality of service level by default. For information about quality of service, see [`Prioritize Work with Quality of Service Classes`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html#//apple_ref/doc/uid/TP40015243-CH39) in [`Energy Efficiency Guide for iOS Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html#//apple_ref/doc/uid/TP40015243) and [`Prioritize Work at the Task Level`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/PrioritizeWorkAtTheTaskLevel.html#//apple_ref/doc/uid/TP40013929-CH35) in [`Energy Efficiency Guide for Mac Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929).

##### Interacting with a Container

A container coordinates all interactions between your app and the server. Most of these interactions involve the following tasks:

- Determining whether the user has an iCloud account, which lets you know if you can write data to the user’s personal storage.
- With the user’s permission, discovering other users who the current user knows, and making the current user’s information discoverable.
- Getting the container or one of its databases to use with an operation.

##### Public and Private Databases

Each container provides a public and a private database for storing data. The contents of the public database are accessible to all users of the app, whereas the contents of the private database are, by default, visible only to the current user. Content that is specific to a single user usually belongs in that user’s private database, whereas app-related content that you provide (or that users want to share) belongs in the public database.

The public database is always available, regardless of whether the device has an active iCloud account. When there isn’t an iCloud account, your app can fetch records from and query the public database, but it can’t save changes. Saving records to the public database requires an active iCloud account to identify the owner of those records. Access to the private database always requires an active iCloud account on the device.

> **Note**:  The data in a public database counts toward the iCloud storage quota of the app that owns the container. That data doesn’t count toward the storage quota of any single user. Data in the private database counts toward the user’s iCloud storage quota.

 The data in a public database counts toward the iCloud storage quota of the app that owns the container. That data doesn’t count toward the storage quota of any single user. Data in the private database counts toward the user’s iCloud storage quota.

##### Using Icloud

Whenever possible, design your app to run gracefully with or without an active iCloud account. Even without an active iCloud account, apps can fetch records from the public database and display that information to the user. If your app requires the ability to write to the public database or requires access to the private database, notify the user of the reason and encourage them to enable iCloud. You can even provide a button that takes the user directly to Settings so that they can enable iCloud. To implement such a button, have the button’s action open the URL that the [`openSettingsURLString`](https://developer.apple.com/documentation/UIKit/UIApplication/openSettingsURLString) constant provides.

##### User Records and Permissions

When a user accesses a container for the first time, CloudKit assigns them a unique identifier and uses it to create two user records — one in the app’s public database and another in that user’s private database. By default, these records don’t contain any identifying personal information, but you can use the record in the user’s private database to store additional, nonsensitive information about that user. Because the public database’s user record is accessible to all users of your app, don’t use it to store information about the user.

While a user record isn’t the same as the user’s [`CKUserIdentity`](ckuseridentity.md), the identity does provide the identifier of their user record that you can use to fetch that record from either the public database or the user’s private database. For more information, see [`userRecordID`](ckuseridentity/userrecordid.md).

##### Testing Your Code Using the Development Container

At runtime, CloudKit uses your app’s `com.apple.developer.icloud-container-environment` entitlement to discover whether you’re using a `Development` or `Production` version of your provisioning profile. When you configure the entitlement for development, CloudKit configures the app’s containers to use the development server. The development environment is a safe place to make changes during the development process without disrupting users of your app. You can add new fields to records programmatically, and you can delete or modify fields using iCloud Dashboard.

Before shipping your app, always test your app’s behavior in the production environment. The production server generates errors when your app tries to add record types or add new fields to existing record types. Testing in the production environment helps you find and fix the places in your code where you’re making those types of changes. You can use CloudKit Dashboard to modify record types in the development environment, and then migrate those changes to the production environment.

> **Note**:  Simulator works only with the development environment. When you’re ready to test your app in a production environment, do so from a device.

 Simulator works only with the development environment. When you’re ready to test your app in a production environment, do so from a device.

## Topics

### Creating Containers
- [class func `default`() -> CKContainer](ckcontainer/default.md)
  Returns the app’s default container.
- [init(identifier: String)](ckcontainer/init(identifier:).md)
  Creates a container for the specified identifier.
### Getting the Public and Private Databases
- [var privateCloudDatabase: CKDatabase](ckcontainer/privateclouddatabase.md)
  The user’s private database.
- [var publicCloudDatabase: CKDatabase](ckcontainer/publicclouddatabase.md)
  The app’s public database.
- [var sharedCloudDatabase: CKDatabase](ckcontainer/sharedclouddatabase.md)
  The database that contains shared data.
- [func database(with: CKDatabase.Scope) -> CKDatabase](ckcontainer/database(with:).md)
  Returns the database with the specified scope.
### Getting the Container’s Identifier
- [var containerIdentifier: String?](ckcontainer/containeridentifier.md)
  The container’s unique identifier.
### Determining the User’s iCloud Access Status
- [func accountStatus(completionHandler: (CKAccountStatus, (any Error)?) -> Void)](ckcontainer/accountstatus(completionhandler:).md)
  Determines whether the system can access the user’s iCloud account.
- [enum CKAccountStatus](ckaccountstatus.md)
  Constants that indicate the availability of the user’s iCloud account.
### Requesting and Determining App Permissions
- [func requestApplicationPermission(CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](ckcontainer/requestapplicationpermission(_:completionhandler:).md)
  Prompts the user to authorize the specified permission.
- [func status(forApplicationPermission: CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](ckcontainer/status(forapplicationpermission:completionhandler:).md)
  Determines the authorization status of the specified permission.
- [CKContainer.Application](ckcontainer/application.md)
  A collection of types for app permissions.
- [CKContainer.ApplicationPermissions](ckcontainer/applicationpermissions.md)
  Constants that represent the permissions that a user grants.
- [CKContainer.ApplicationPermissionBlock](ckcontainer/applicationpermissionblock.md)
  A closure that processes the outcome of a permissions request.
- [CKContainer.ApplicationPermissionStatus](ckcontainer/applicationpermissionstatus.md)
  Constants that represent the status of a permission.
### Performing Operations on the Container
- [func add(CKOperation)](ckcontainer/add(_:).md)
  Adds an operation to the container’s queue.
### Discovering User Records
- [func discoverAllIdentities(completionHandler: ([CKUserIdentity]?, (any Error)?) -> Void)](ckcontainer/discoverallidentities(completionhandler:).md)
  Fetches all user identities that match entries in the user’s Contacts.
- [func discoverUserIdentity(withEmailAddress: String, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](ckcontainer/discoveruseridentity(withemailaddress:completionhandler:).md)
  Fetches the user identity for the specified email address.
- [func discoverUserIdentity(withPhoneNumber: String, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](ckcontainer/discoveruseridentity(withphonenumber:completionhandler:).md)
  Fetches the user identity for the specified phone number.
- [func discoverUserIdentity(withUserRecordID: CKRecord.ID, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](ckcontainer/discoveruseridentity(withuserrecordid:completionhandler:).md)
  Fetches the user identity for the specified user record ID.
- [func fetchShareParticipant(withEmailAddress: String, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](ckcontainer/fetchshareparticipant(withemailaddress:completionhandler:).md)
  Fetches the share participant with the specified email address.
- [func fetchShareParticipant(withPhoneNumber: String, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](ckcontainer/fetchshareparticipant(withphonenumber:completionhandler:).md)
  Fetches the share participant with the specified phone number.
- [func fetchShareParticipant(withUserRecordID: CKRecord.ID, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](ckcontainer/fetchshareparticipant(withuserrecordid:completionhandler:).md)
  Fetches the share participant with the specified user record ID.
- [func fetchUserRecordID(completionHandler: (CKRecord.ID?, (any Error)?) -> Void)](ckcontainer/fetchuserrecordid(completionhandler:).md)
  Fetches the user record ID of the current user.
- [let CKCurrentUserDefaultName: String](ckcurrentuserdefaultname.md)
  A constant that provides the current user’s default name.
- [let CKOwnerDefaultName: String](ckownerdefaultname.md)
  A constant that provides the default owner’s name.
### Fetching Long-Lived Operations
- [func fetchAllLongLivedOperationIDs(completionHandler: ([CKOperation.ID]?, (any Error)?) -> Void)](ckcontainer/fetchalllonglivedoperationids(completionhandler:).md)
  Fetches the IDs of any long-lived operations that are running.
- [func fetchLongLivedOperation(withID: CKOperation.ID, completionHandler: (CKOperation?, (any Error)?) -> Void)](ckcontainer/fetchlonglivedoperation(withid:completionhandler:).md)
  Fetches the long-lived operation for the specified operation ID.
### Accessing Container Metadata
- [func fetchShareMetadata(with: URL, completionHandler: (CKShare.Metadata?, (any Error)?) -> Void)](ckcontainer/fetchsharemetadata(with:completionhandler:).md)
  Fetches the share metadata for the specified share URL.
- [func accept(CKShare.Metadata, completionHandler: (CKShare?, (any Error)?) -> Void)](ckcontainer/accept(_:completionhandler:)-949ea.md)
  Accepts the specified share metadata.
- [static let CKAccountChanged: NSNotification.Name](../foundation/nsnotification/name/1399172-ckaccountchanged.md)
  A notification that a container posts when the status of an iCloud account changes.
### Instance Methods
- [func accept([CKShare.Metadata]) async throws -> [CKShare.Metadata : Result<CKShare, any Error>]](ckcontainer/accept(_:).md)
- [func accept([CKShare.Metadata], completionHandler: (Result<[CKShare.Metadata : Result<CKShare, any Error>], any Error>) -> Void)](ckcontainer/accept(_:completionhandler:)-7s3t7.md)
- [func allLongLivedOperationIDs() async throws -> [CKOperation.ID]](ckcontainer/alllonglivedoperationids.md)
- [func configuredWith<R>(configuration: CKOperation.Configuration?, group: CKOperationGroup?, body: (CKContainer) throws -> R) rethrows -> R](ckcontainer/configuredwith(configuration:group:body:)-40x6k.md)
- [func configuredWith<R>(configuration: CKOperation.Configuration?, group: CKOperationGroup?, body: (CKContainer) async throws -> R) async rethrows -> R](ckcontainer/configuredwith(configuration:group:body:)-4kc2l.md)
- [func discoverUserIdentities(forEmailAddresses: [String], completionHandler: (Result<[String : CKUserIdentity], any Error>) -> Void)](ckcontainer/discoveruseridentities(foremailaddresses:completionhandler:).md)
- [func discoverUserIdentities(forPhoneNumbers: [String], completionHandler: (Result<[String : CKUserIdentity], any Error>) -> Void)](ckcontainer/discoveruseridentities(forphonenumbers:completionhandler:).md)
- [func discoverUserIdentities(forUserRecordIDs: [CKRecord.ID], completionHandler: (Result<[CKRecord.ID : CKUserIdentity], any Error>) -> Void)](ckcontainer/discoveruseridentities(foruserrecordids:completionhandler:).md)
- [func fetchShareMetadatas(for: [URL], completionHandler: (Result<[URL : Result<CKShare.Metadata, any Error>], any Error>) -> Void)](ckcontainer/fetchsharemetadatas(for:completionhandler:).md)
- [func fetchShareParticipants(forEmailAddresses: [String], completionHandler: (Result<[String : Result<CKShare.Participant, any Error>], any Error>) -> Void)](ckcontainer/fetchshareparticipants(foremailaddresses:completionhandler:).md)
- [func fetchShareParticipants(forPhoneNumbers: [String], completionHandler: (Result<[String : Result<CKShare.Participant, any Error>], any Error>) -> Void)](ckcontainer/fetchshareparticipants(forphonenumbers:completionhandler:).md)
- [func fetchShareParticipants(forUserRecordIDs: [CKRecord.ID], completionHandler: (Result<[CKRecord.ID : Result<CKShare.Participant, any Error>], any Error>) -> Void)](ckcontainer/fetchshareparticipants(foruserrecordids:completionhandler:).md)
- [func longLivedOperation(for: CKOperation.ID) async throws -> CKOperation?](ckcontainer/longlivedoperation(for:).md)
- [func shareMetadatas(for: [URL]) async throws -> [URL : Result<CKShare.Metadata, any Error>]](ckcontainer/sharemetadatas(for:).md)
- [func shareParticipants(forEmailAddresses: [String]) async throws -> [String : Result<CKShare.Participant, any Error>]](ckcontainer/shareparticipants(foremailaddresses:).md)
- [func shareParticipants(forPhoneNumbers: [String]) async throws -> [String : Result<CKShare.Participant, any Error>]](ckcontainer/shareparticipants(forphonenumbers:).md)
- [func shareParticipants(forUserRecordIDs: [CKRecord.ID]) async throws -> [CKRecord.ID : Result<CKShare.Participant, any Error>]](ckcontainer/shareparticipants(foruserrecordids:).md)
- [func userIdentities(forEmailAddresses: [String]) async throws -> [String : CKUserIdentity]](ckcontainer/useridentities(foremailaddresses:).md)
- [func userIdentities(forPhoneNumbers: [String]) async throws -> [String : CKUserIdentity]](ckcontainer/useridentities(forphonenumbers:).md)
- [func userIdentities(forUserRecordIDs: [CKRecord.ID]) async throws -> [CKRecord.ID : CKUserIdentity]](ckcontainer/useridentities(foruserrecordids:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CKDatabase](ckdatabase.md)
  An object that represents a collection of record zones and subscriptions.
- [class CKOperationGroup](ckoperationgroup.md)
  An explicit association between two or more operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer)*