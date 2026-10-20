# isUbiquitousItem(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean indicating whether the item is targeted for storage in iCloud.

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
func isUbiquitousItem(at url: URL) -> Bool
```

```objc
- (BOOL) isUbiquitousItemAtURL:(NSURL *) url;
```

#### Return Value

[`true`](../../Swift/true.md) if the item is targeted for iCloud storage or [`false`](../../Swift/false.md) if it is not. This method also returns [`false`](../../Swift/false.md) if no item exists at `url`.

#### Discussion

This method reflects only whether the item should be stored in iCloud because a call was made to the  [`setUbiquitous(_:itemAt:destinationURL:)`](./setubiquitous%28_,itemat,destinationurl%29.md) method with a value of [`true`](../../Swift/true.md) for its `flag` parameter. This method does not reflect whether the file has actually been uploaded to any iCloud servers. To determine a file’s upload status, check the `NSURLUbiquitousItemIsUploadedKey` attribute of the corresponding [`NSURL`](../nsurl.md) object.

## Parameters

- `url`: Specify the URL for the file or directory whose status you want to check.

## See Also

### Managing iCloud-based items
- [var ubiquityIdentityToken: (any NSCoding & NSCopying & NSObjectProtocol)?](./ubiquityidentitytoken.md)
  An opaque token that represents the current user’s iCloud Drive Documents identity.
- [func url(forUbiquityContainerIdentifier: String?) -> URL?](./url%28forubiquitycontaineridentifier%29.md)
  Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [func setUbiquitous(Bool, itemAt: URL, destinationURL: URL) throws](./setubiquitous%28_,itemat,destinationurl%29.md)
  Indicates whether the item at the specified URL should be stored in iCloud.
- [func startDownloadingUbiquitousItem(at: URL) throws](./startdownloadingubiquitousitem%28at%29.md)
  Starts downloading (if necessary) the specified item to the local system.
- [func evictUbiquitousItem(at: URL) throws](./evictubiquitousitem%28at%29.md)
  Removes the local copy of the specified item that’s stored in iCloud.
- [func url(forPublishingUbiquitousItemAt: URL, expiration: AutoreleasingUnsafeMutablePointer<NSDate?>?) throws -> URL](./url%28forpublishingubiquitousitemat,expiration%29.md)
  Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/isubiquitousitem(at:))*