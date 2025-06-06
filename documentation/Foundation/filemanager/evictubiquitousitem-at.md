# evictUbiquitousItem(at:)

**Framework**: Foundation  
**Kind**: method

Removes the local copy of the specified item that’s stored in iCloud.

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
func evictUbiquitousItem(at url: URL) throws
```

#### Discussion

Don’t use a coordinated write to perform this operation. In macOS 10.7 or earlier, the framework takes a coordinated write in its implementation of this method, so taking one in your app causes a deadlock. In macOS 10.8 and later, the framework detects coordination done by your app on the same thread as the call to this method, to avoid deadlocking.

This method doesn’t remove the item from iCloud. It removes only the local version. You can then use [`startDownloadingUbiquitousItem(at:)`](filemanager/startdownloadingubiquitousitem(at:).md) to force iCloud to download a new version of the file or directory from the server.

To delete a file permanently from the user’s iCloud storage, use the regular [`FileManager`](filemanager.md) routines for deleting files and directories. Remember that deleting items from iCloud can’t be undone. Once deleted, the item is gone forever.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The URL to a file or directory in iCloud storage.

## See Also

- [func removeItem(at: URL) throws](filemanager/removeitem(at:).md)
  Removes the file or directory at the specified URL.
- [var ubiquityIdentityToken: (any NSCoding & NSCopying & NSObjectProtocol)?](filemanager/ubiquityidentitytoken.md)
  An opaque token that represents the current user’s iCloud Drive Documents identity.
- [func url(forUbiquityContainerIdentifier: String?) -> URL?](filemanager/url(forubiquitycontaineridentifier:).md)
  Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [func isUbiquitousItem(at: URL) -> Bool](filemanager/isubiquitousitem(at:).md)
  Returns a Boolean indicating whether the item is targeted for storage in iCloud.
- [func setUbiquitous(Bool, itemAt: URL, destinationURL: URL) throws](filemanager/setubiquitous(_:itemat:destinationurl:).md)
  Indicates whether the item at the specified URL should be stored in iCloud.
- [func startDownloadingUbiquitousItem(at: URL) throws](filemanager/startdownloadingubiquitousitem(at:).md)
  Starts downloading (if necessary) the specified item to the local system.
- [func url(forPublishingUbiquitousItemAt: URL, expiration: AutoreleasingUnsafeMutablePointer<NSDate?>?) throws -> URL](filemanager/url(forpublishingubiquitousitemat:expiration:).md)
  Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/evictubiquitousitem(at:))*