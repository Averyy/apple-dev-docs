# ubiquityIdentityToken

**Framework**: Foundation  
**Kind**: property

An opaque token that represents the current user’s iCloud Drive Documents identity.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var ubiquityIdentityToken: (any NSCoding & NSCopying & NSObjectProtocol)? { get }
```

#### Discussion

In iCloud Drive Documents, when iCloud is available, this property contains an opaque object representing the identity of the current user. If iCloud is unavailable or there is no logged-in user, the value of this property is `nil`. Accessing the value of this property is relatively fast, so you can check the value at launch time from your app’s main thread.

You can use the token in this property, together with the [`NSUbiquityIdentityDidChange`](nsnotification/name-swift.struct/nsubiquityidentitydidchange.md) notification, to detect when the user logs in or out of iCloud and to detect changes to the active iCloud account. When the user logs in with a different iCloud account, the identity token changes, and the system posts the notification. If you stored or archived the previous token, compare that token to the newly obtained one using the [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) method to determine if the users are the same or different.

Accessing the token in this property doesn’t connect your app to its ubiquity containers. To establish access to a ubiquity container, call the [`url(forUbiquityContainerIdentifier:)`](filemanager/url(forubiquitycontaineridentifier:).md) method. In macOS, you can instead use an [`NSDocument`](https://developer.apple.com/documentation/AppKit/NSDocument) object, which establishes access automatically.

CloudKit clients should not use this token as a way to identify whether the iCloud account is logged in. Instead, use [`accountStatus(completionHandler:)`](https://developer.apple.com/documentation/CloudKit/CKContainer/accountStatus(completionHandler:)) or [`fetchUserRecordID(completionHandler:)`](https://developer.apple.com/documentation/CloudKit/CKContainer/fetchUserRecordID(completionHandler:)).

## See Also

- [func url(forUbiquityContainerIdentifier: String?) -> URL?](filemanager/url(forubiquitycontaineridentifier:).md)
  Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/ubiquityidentitytoken)*