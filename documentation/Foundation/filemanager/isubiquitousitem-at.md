# isUbiquitousItem(at:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the item is targeted for iCloud storage or [`false`](https://developer.apple.com/documentation/swift/false) if it is not. This method also returns [`false`](https://developer.apple.com/documentation/swift/false) if no item exists at `url`.

#### Discussion

This method reflects only whether the item should be stored in iCloud because a call was made to the  [`setUbiquitous(_:itemAt:destinationURL:)`](filemanager/setubiquitous(_:itemat:destinationurl:).md) method with a value of [`true`](https://developer.apple.com/documentation/swift/true) for its `flag` parameter. This method does not reflect whether the file has actually been uploaded to any iCloud servers. To determine a file’s upload status, check the `NSURLUbiquitousItemIsUploadedKey` attribute of the corresponding [`NSURL`](nsurl.md) object.

## Parameters

- `url`: Specify the URL for the file or directory whose status you want to check.

## See Also

- [var ubiquityIdentityToken: (any NSCoding & NSCopying & NSObjectProtocol)?](filemanager/ubiquityidentitytoken.md)
  An opaque token that represents the current user’s iCloud Drive Documents identity.
- [func url(forUbiquityContainerIdentifier: String?) -> URL?](filemanager/url(forubiquitycontaineridentifier:).md)
  Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [func setUbiquitous(Bool, itemAt: URL, destinationURL: URL) throws](filemanager/setubiquitous(_:itemat:destinationurl:).md)
  Indicates whether the item at the specified URL should be stored in iCloud.
- [func startDownloadingUbiquitousItem(at: URL) throws](filemanager/startdownloadingubiquitousitem(at:).md)
  Starts downloading (if necessary) the specified item to the local system.
- [func evictUbiquitousItem(at: URL) throws](filemanager/evictubiquitousitem(at:).md)
  Removes the local copy of the specified item that’s stored in iCloud.
- [func url(forPublishingUbiquitousItemAt: URL, expiration: AutoreleasingUnsafeMutablePointer<NSDate?>?) throws -> URL](filemanager/url(forpublishingubiquitousitemat:expiration:).md)
  Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/isubiquitousitem(at:))*