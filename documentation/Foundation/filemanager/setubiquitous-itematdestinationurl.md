# setUbiquitous(_:itemAt:destinationURL:)

**Framework**: Foundation  
**Kind**: method

Indicates whether the item at the specified URL should be stored in iCloud.

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
func setUbiquitous(_ flag: Bool, itemAt url: URL, destinationURL: URL) throws
```

#### Discussion

Use this method to move a file from its current location to iCloud. For files located in an app’s sandbox, this involves physically removing the file from the sandbox container. (The system extends your app’s sandbox privileges to give it access to files it moves to iCloud.) You can also use this method to move files out of iCloud and back into a local directory.

If your app is presenting the file’s contents to the user, it must have an active file presenter object configured to monitor the specified file or directory before calling this method. When you specify [`true`](https://developer.apple.com/documentation/swift/true) for the `flag` parameter, this method attempts to move the file or directory to the cloud and returns [`true`](https://developer.apple.com/documentation/swift/true) if it is successful. Calling this method also notifies your file presenter of the new location of the file so that your app can continue to operate on it.

> ❗ **Important**:  Avoid calling this method from your app’s main thread. This method performs a coordinated write operation on the specified file, which can block for a long time. Additionally, if the file presenter that is monitoring the file is incorrectly configured so that it receives messages on the main operation queue, calling this method on the main thread can cause a deadlock. Instead, use a dispatch queue to call this method from background thread. After the method returns, message your main thread to update the rest of your app’s data structures. After calling this method, you must wait for a file to be fully uploaded to iCloud before attempting to share the file using the [`url(forPublishingUbiquitousItemAt:expiration:)`](filemanager/url(forpublishingubiquitousitemat:expiration:).md) method.

 Avoid calling this method from your app’s main thread. This method performs a coordinated write operation on the specified file, which can block for a long time. Additionally, if the file presenter that is monitoring the file is incorrectly configured so that it receives messages on the main operation queue, calling this method on the main thread can cause a deadlock. Instead, use a dispatch queue to call this method from background thread. After the method returns, message your main thread to update the rest of your app’s data structures.

After calling this method, you must wait for a file to be fully uploaded to iCloud before attempting to share the file using the [`url(forPublishingUbiquitousItemAt:expiration:)`](filemanager/url(forpublishingubiquitousitemat:expiration:).md) method.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `flag`:   to move the item to iCloud or   to remove it from iCloud (if it is there currently).
- `url`: The URL of the item (file or directory) that you want to store in iCloud.
- `destinationURL`: When moving a file into iCloud, this is the location in iCloud at which to store the file or directory. This URL must be constructed from a URL returned by the   method, which you use to retrieve the desired iCloud container directory. The URL you specify may contain additional subdirectories so that you can organize your files hierarchically in iCloud. However, you are responsible for creating those intermediate subdirectories (using the   class) in your iCloud container directory. When moving a file  , this is the location on the local device.

## See Also

- [var ubiquityIdentityToken: (any NSCoding & NSCopying & NSObjectProtocol)?](filemanager/ubiquityidentitytoken.md)
  An opaque token that represents the current user’s iCloud Drive Documents identity.
- [func url(forUbiquityContainerIdentifier: String?) -> URL?](filemanager/url(forubiquitycontaineridentifier:).md)
  Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [func isUbiquitousItem(at: URL) -> Bool](filemanager/isubiquitousitem(at:).md)
  Returns a Boolean indicating whether the item is targeted for storage in iCloud.
- [func startDownloadingUbiquitousItem(at: URL) throws](filemanager/startdownloadingubiquitousitem(at:).md)
  Starts downloading (if necessary) the specified item to the local system.
- [func evictUbiquitousItem(at: URL) throws](filemanager/evictubiquitousitem(at:).md)
  Removes the local copy of the specified item that’s stored in iCloud.
- [func url(forPublishingUbiquitousItemAt: URL, expiration: AutoreleasingUnsafeMutablePointer<NSDate?>?) throws -> URL](filemanager/url(forpublishingubiquitousitemat:expiration:).md)
  Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/setubiquitous(_:itemat:destinationurl:))*