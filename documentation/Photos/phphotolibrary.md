# PHPhotoLibrary

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An object that manages access and changes to a person’s photo library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHPhotoLibrary
```

```objc
@interface PHPhotoLibrary : NSObject
```

## Mentions

- [Editing Asset Content](../PhotoKit/editing-asset-content.md)
- [Delivering an Enhanced Privacy Experience in Your Photos App](../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)
- [Fetching Assets](../PhotoKit/fetching-assets.md)
- [Fetching Objects and Requesting Changes](../PhotoKit/fetching-objects-and-requesting-changes.md)
- [Observing Changes in the Photo Library](../PhotoKit/observing-changes-in-the-photo-library.md)

## Overview

The object represents the entire set of assets and collections that the Photos app manages, including assets stored on the local device and those stored in iCloud Photos. Use this object for the following tasks:

- Retrieving or verifying the user’s permission for your app to access Photos content
- Making changes to assets and collections; for example, editing asset metadata or content, inserting new assets, or rearranging the members of a collection
- Determining which records change since a previous state of the Photos library
- Registering for update messages the system sends when the library changes

## Topics

### Verifying Authorization
- [class func authorizationStatus(for: PHAccessLevel) -> PHAuthorizationStatus](./phphotolibrary/authorizationstatus%28for%29.md)
  Returns the app’s authorization to access the user’s photo library for the specified access level.
- [class func requestAuthorization(for: PHAccessLevel, handler: (PHAuthorizationStatus) -> Void)](./phphotolibrary/requestauthorization%28for,handler%29.md)
  Prompts the user to grant the app permission to access the photo library.
- [enum PHAccessLevel](./phaccesslevel.md)
  The app’s level of access to the user’s photo library.
- [enum PHAuthorizationStatus](./phauthorizationstatus.md)
  Information about your app’s authorization to access the user’s photo library.
- [class func authorizationStatus() -> PHAuthorizationStatus](./phphotolibrary/authorizationstatus%28%29.md)
  Returns information about your app’s authorization to access the user’s photo library.
- [class func requestAuthorization((PHAuthorizationStatus) -> Void)](./phphotolibrary/requestauthorization%28_%29.md)
  Requests the user’s permission, if needed, to access the photo library.
### Accessing the Shared Library
- [class func shared() -> PHPhotoLibrary](./phphotolibrary/shared%28%29.md)
  Retrieves the shared photo library object.
### Presenting the Limited Library Picker
- [func presentLimitedLibraryPicker(from: UIViewController)](./phphotolibrary/presentlimitedlibrarypicker%28from%29.md)
  Prompts the user to update their limited library selection.
- [func presentLimitedLibraryPicker(from: UIViewController, completionHandler: ([String]) -> Void)](./phphotolibrary/presentlimitedlibrarypicker%28from,completionhandler%29.md)
  Prompts the user to update their limited library selection with a callback providing newly selected identifiers.
### Updating the Library
- [Requesting Changes to the Photo Library](../PhotoKit/requesting-changes-to-the-photo-library.md)
  Create, delete, or modify assets and collections in a photo library by making change requests.
- [func performChanges(() -> Void, completionHandler: ((Bool, (any Error)?) -> Void)?)](./phphotolibrary/performchanges%28_,completionhandler%29.md)
  Asynchronously runs a block that requests changes to the photo library.
- [func performChangesAndWait(() -> Void) throws](./phphotolibrary/performchangesandwait%28_%29.md)
  Synchronously runs a block that requests changes to be performed in the photo library.
- [class PHChangeRequest](./phchangerequest.md)
  The abstract base class of the framework’s photo library change requests.
- [class PHAssetChangeRequest](./phassetchangerequest.md)
  A request to create, delete, change metadata for, or edit the content of a Photos asset, for use in a photo library change block.
- [class PHAssetCollectionChangeRequest](./phassetcollectionchangerequest.md)
  A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.
- [class PHCollectionListChangeRequest](./phcollectionlistchangerequest.md)
  A request to create, delete, or modify a Photos collection list, for use in a photo library change block.
- [class PHObjectPlaceholder](./phobjectplaceholder.md)
  A read-only proxy object that represents a Photos asset or collection to create.
### Fetching Change History
- [func fetchPersistentChanges(since: PHPersistentChangeToken) throws -> PHPersistentChangeFetchResult](./phphotolibrary/fetchpersistentchanges%28since%29.md)
  Retrieves the Photos library changes since the token you specify.
- [class PHPersistentChangeFetchResult](./phpersistentchangefetchresult.md)
  An object that represents a fetch result and allows you to enumerate a very large set of change records.
- [var currentChangeToken: PHPersistentChangeToken](./phphotolibrary/currentchangetoken.md)
  The opaque token that represents the current state of the Photos library.
- [class PHPersistentChangeToken](./phpersistentchangetoken.md)
  An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.
### Observing Library Changes
- [Observing Changes in the Photo Library](../PhotoKit/observing-changes-in-the-photo-library.md)
  Register an observer to be notified of changes to the photo library.
- [func register(any PHPhotoLibraryChangeObserver)](./phphotolibrary/register%28_%29-6y3b9.md)
  Registers an object to receive messages when objects in the photo library change.
- [func unregisterChangeObserver(any PHPhotoLibraryChangeObserver)](./phphotolibrary/unregisterchangeobserver%28_%29.md)
  Unregisters an object so that it no longer receives change messages.
- [protocol PHPhotoLibraryChangeObserver](./phphotolibrarychangeobserver.md)
  A protocol to adopt to have the system notify your app of changes to the photo library.
- [class PHChange](./phchange.md)
  A description of a change that occurred in the photo library.
- [class PHObjectChangeDetails](./phobjectchangedetails.md)
  A description of changes that occurred in an asset or collection object.
- [class PHFetchResultChangeDetails](./phfetchresultchangedetails.md)
  A description of changes that occurred in the set of asset or collection objects listed in a fetch result.
### Observing Library Availability
- [func register(any PHPhotoLibraryAvailabilityObserver)](./phphotolibrary/register%28_%29-gm0a.md)
  Registers an object to observe changes to the photo library’s availability.
- [func unregisterAvailabilityObserver(any PHPhotoLibraryAvailabilityObserver)](./phphotolibrary/unregisteravailabilityobserver%28_%29.md)
  Unregisters an object from observing changes to the photo library’s availability.
- [protocol PHPhotoLibraryAvailabilityObserver](./phphotolibraryavailabilityobserver.md)
  A protocol to adopt to have the system notify your app when the availability of a photo library changes.
- [var unavailabilityReason: (any Error)?](./phphotolibrary/unavailabilityreason.md)
  An error that describes the reason the photo library isn’t available.
### Converting Between Local and iCloud Identifiers
- [func cloudIdentifierMappings(forLocalIdentifiers: [String]) -> [String : Result<PHCloudIdentifier, any Error>]](./phphotolibrary/cloudidentifiermappings%28forlocalidentifiers%29.md)
  Retrieves the cloud identifier mappings for the list of local identifiers.
- [func localIdentifierMappings(for: [PHCloudIdentifier]) -> [PHCloudIdentifier : Result<String, any Error>]](./phphotolibrary/localidentifiermappings%28for%29.md)
  Retrieves the local identifier mappings for the list of cloud identifiers.
- [class PHCloudIdentifier](./phcloudidentifier.md)
  An object that identifies an asset or collection that syncs through iCloud Photos.
- [func cloudIdentifiers(forLocalIdentifiers: [String]) -> [PHCloudIdentifier]](./phphotolibrary/cloudidentifiers%28forlocalidentifiers%29.md)
  Retrieves the equivalent iCloud identifiers for the list of local identifiers.
- [func localIdentifiers(for: [PHCloudIdentifier]) -> [String]](./phphotolibrary/localidentifiers%28for%29.md)
  Retrieves the equivalent local identifiers for the list of iCloud identifiers.
- [let PHLocalIdentifierNotFound: String](./phlocalidentifiernotfound.md)
  A constant value that indicates that the system can’t resolve a local object from a global identifier.
- [- cloudIdentifierMappingsForLocalIdentifiers:](./phphotolibrary/cloudidentifiermappingsforlocalidentifiers_.md)
  Retrieves the cloud identifier mappings for the list of local identifiers.
- [- localIdentifierMappingsForCloudIdentifiers:](./phphotolibrary/localidentifiermappingsforcloudidentifiers_.md)
  Retrieves the local identifier mappings for the list of cloud identifiers.
- [PHCloudIdentifierMapping](./phcloudidentifiermapping.md)
  An object that contains the cloud identifier result from looking up a local identifier, or an error indicating why the lookup failed.
- [PHLocalIdentifierMapping](./phlocalidentifiermapping.md)
  An object that contains the local identifier result from looking up a cloud identifier, or an error indicating why the lookup failed.
### Enabling an Upload Job Extension
- [var uploadJobExtensionEnabled: Bool](./phphotolibrary/uploadjobextensionenabled.md)
  A Boolean value that indicates whether background asset resource uploading is enabled.
- [func setUploadJobExtensionEnabled(Bool) throws](./phphotolibrary/setuploadjobextensionenabled%28_%29.md)
  Enables or disables the background asset resource upload job feature.
### Instance Properties
- [var uploadJobExtensionOptions: PHAssetResourceUploadJobOptions?](./phphotolibrary/uploadjobextensionoptions.md)
  The options for the calling app’s background asset resource upload job configuration.
### Instance Methods
- [func disableUploadJobExtension() throws](./phphotolibrary/disableuploadjobextension%28%29.md)
  Disables the background asset resource upload job feature.
- [func enableUploadJobExtension(with: PHAssetResourceUploadJobOptions?) throws](./phphotolibrary/enableuploadjobextension%28with%29.md)
  Enables the background asset resource upload job feature with the given options, atomically.
- [func localIdentifierMappings(forSynced: [PHCloudIdentifier]) -> [PHCloudIdentifier : Result<String, any Error>]](./phphotolibrary/localidentifiermappings%28forsynced%29.md)
- [func register(any PHPhotoLibraryPersistentChangesObserver)](./phphotolibrary/register%28_%29-7lhue.md)
  Registers an observer to be notified when persistent changes occur in the photo library.
- [func setUploadJobExtensionOptions(PHAssetResourceUploadJobOptions) throws](./phphotolibrary/setuploadjobextensionoptions%28_%29.md)
  Sets the options for the calling app’s background asset resource upload job configuration.
- [func unregisterPersistentChangesObserver(any PHPhotoLibraryPersistentChangesObserver)](./phphotolibrary/unregisterpersistentchangesobserver%28_%29.md)
  Unregisters a previously registered persistent changes observer.
- [- localIdentifierMappingsForSyncedCloudIdentifiers:](./phphotolibrary/localidentifiermappingsforsyncedcloudidentifiers_.md)
  Returns a dictionary that maps each cloud identifier from the provided array to a `PHLocalIdentifierMapping` result containing the local identifier found for that cloud identifier if that cloud identifier is a known synced identifier.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary)*