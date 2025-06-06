# url(forUbiquityContainerIdentifier:)

**Framework**: Foundation  
**Kind**: method

Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func url(forUbiquityContainerIdentifier containerIdentifier: String?) -> URL?
```

#### Return Value

A URL pointing to the specified ubiquity container, or `nil` if the container could not be located or if iCloud storage is unavailable for the current user or device.

#### Discussion

You use this method to determine the location of your app’s ubiquity container directories and to configure your app’s initial iCloud access. The first time you call this method for a given ubiquity container, the system extends your app’s sandbox to include that container. In iOS, you must call this method at least once before trying to search for cloud-based files in the ubiquity container. If your app accesses multiple ubiquity containers, call this method once for each container. In macOS, you do not need to call this method if you use [`NSDocument`](https://developer.apple.com/documentation/AppKit/NSDocument)-based objects, because the system then calls this method automatically.

You can use the URL returned by this method to build paths to files and directories within your app’s ubiquity container. Each app that syncs documents to the cloud must have at least one associated ubiquity container in which to put those files. This container can be unique to the app or shared by multiple apps.

> ❗ **Important**:  Do not call this method from your app’s main thread. Because this method might take a nontrivial amount of time to set up iCloud and return the requested URL, you should always call it from a secondary thread. To determine if iCloud is available, especially at launch time, check the value of the [`ubiquityIdentityToken`](filemanager/ubiquityidentitytoken.md) property instead.

In addition to writing to its own ubiquity container, an app can write to any container directory for which it has the appropriate permission. Each additional ubiquity container should be listed as an additional value in the `com.apple.developer.ubiquity-container-identifiers` entitlement array.

To learn how to view your development team’s unique  value, read To view the team ID in Tools Workflow Guide for Mac.

> **Note**:  The development team ID that precedes each container ID string is the unique identifier associated with your development team. To learn how to view your development team’s unique  value, read To view the team ID in Tools Workflow Guide for Mac.

## Parameters

- `containerIdentifier`: If you specify   for this parameter, this method returns the first container listed in the   entitlement array.

## See Also

- [var ubiquityIdentityToken: (any NSCoding & NSCopying & NSObjectProtocol)?](filemanager/ubiquityidentitytoken.md)
  An opaque token that represents the current user’s iCloud Drive Documents identity.
- [func isUbiquitousItem(at: URL) -> Bool](filemanager/isubiquitousitem(at:).md)
  Returns a Boolean indicating whether the item is targeted for storage in iCloud.
- [func setUbiquitous(Bool, itemAt: URL, destinationURL: URL) throws](filemanager/setubiquitous(_:itemat:destinationurl:).md)
  Indicates whether the item at the specified URL should be stored in iCloud.
- [func startDownloadingUbiquitousItem(at: URL) throws](filemanager/startdownloadingubiquitousitem(at:).md)
  Starts downloading (if necessary) the specified item to the local system.
- [func evictUbiquitousItem(at: URL) throws](filemanager/evictubiquitousitem(at:).md)
  Removes the local copy of the specified item that’s stored in iCloud.
- [func url(forPublishingUbiquitousItemAt: URL, expiration: AutoreleasingUnsafeMutablePointer<NSDate?>?) throws -> URL](filemanager/url(forpublishingubiquitousitemat:expiration:).md)
  Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/url(forubiquitycontaineridentifier:))*