# startDownloadingUbiquitousItem(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Starts downloading (if necessary) the specified item to the local system.

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
func startDownloadingUbiquitousItem(at url: URL) throws
```

```objc
- (BOOL) startDownloadingUbiquitousItemAtURL:(NSURL *) url error:(NSError **) error;
```

#### Discussion

If a cloud-based file or directory has not been downloaded yet, calling this method starts the download process. If the item exists locally, calling this method synchronizes the local copy with the version in the cloud.

For a given URL, you can determine if a file is downloaded by getting the value of the [`NSMetadataUbiquitousItemDownloadingStatusKey`](../nsmetadataubiquitousitemdownloadingstatuskey.md) key. You can also use related keys to determine the current progress in downloading the file.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The URL for the file or directory in the cloud that you want to download.

## See Also

### Managing iCloud-based items
- [var ubiquityIdentityToken: (any NSCoding & NSCopying & NSObjectProtocol)?](./ubiquityidentitytoken.md)
  An opaque token that represents the current user’s iCloud Drive Documents identity.
- [func url(forUbiquityContainerIdentifier: String?) -> URL?](./url%28forubiquitycontaineridentifier%29.md)
  Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [func isUbiquitousItem(at: URL) -> Bool](./isubiquitousitem%28at%29.md)
  Returns a Boolean indicating whether the item is targeted for storage in iCloud.
- [func setUbiquitous(Bool, itemAt: URL, destinationURL: URL) throws](./setubiquitous%28_,itemat,destinationurl%29.md)
  Indicates whether the item at the specified URL should be stored in iCloud.
- [func evictUbiquitousItem(at: URL) throws](./evictubiquitousitem%28at%29.md)
  Removes the local copy of the specified item that’s stored in iCloud.
- [func url(forPublishingUbiquitousItemAt: URL, expiration: AutoreleasingUnsafeMutablePointer<NSDate?>?) throws -> URL](./url%28forpublishingubiquitousitemat,expiration%29.md)
  Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/startdownloadingubiquitousitem(at:))*