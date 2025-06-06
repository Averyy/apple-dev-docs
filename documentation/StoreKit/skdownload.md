# SKDownload

**Framework**: StoreKit  
**Kind**: class

Downloadable content associated with a product.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
class SKDownload
```

## Mentions

- [Unlocking purchased content](unlocking-purchased-content.md)

#### Overview

When you create a product in App Store Connect, you can associate one or more pieces of downloadable content with it. At runtime, when a product is purchased by a user, your app uses [`SKDownload`](skdownload.md) objects to download the content from the App Store.

Your app never directly creates a [`SKDownload`](skdownload.md) object. Instead, after a payment is processed, your app reads the transaction object’s [`downloads`](skpaymenttransaction/downloads.md) property to retrieve an array of [`SKDownload`](skdownload.md) objects associated with the transaction.

To download the content, you queue a download object on the payment queue and wait for the content to be downloaded. After a download completes, read the download object’s [`contentURL`](skdownload/contenturl.md) property to get a URL to the downloaded content. Your app must process the downloaded file before completing the transaction. For example, it might copy the file into a directory whose contents are persistent. When all downloads are complete, you finish the transaction. After the transaction is finished, the download objects cannot be queued to the payment queue and any URLs to the downloaded content are invalid.

## Topics

### Getting Content Information
- [var expectedContentLength: Int64](skdownload/expectedcontentlength.md)
  The length of the downloadable content, in bytes.
- [var contentIdentifier: String](skdownload/contentidentifier.md)
  A string that uniquely identifies the downloadable content.
- [var contentVersion: String](skdownload/contentversion.md)
  A string that identifies which version of the content is available for download.
- [var transaction: SKPaymentTransaction](skdownload/transaction.md)
  The transaction associated with the downloadable file.
- [var contentLength: Int64](skdownload/contentlength.md)
  The length of the downloadable content, in bytes.
### Getting State Information
- [var state: SKDownloadState](skdownload/state.md)
  The current state of the download object.
- [var progress: Float](skdownload/progress.md)
  A value that indicates how much of the file has been downloaded.
- [var timeRemaining: TimeInterval](skdownload/timeremaining.md)
  An estimated time, in seconds, to finish downloading the content.
- [var SKDownloadTimeRemainingUnknown: TimeInterval](skdownloadtimeremainingunknown.md)
  Indicates that the system cannot determine how much time is needed to finish downloading the content.
- [enum SKDownloadState](skdownloadstate.md)
  The states that a download operation can be in.
- [var downloadState: SKDownloadState](skdownload/downloadstate.md)
  The current state of the download object.
### Accessing a Completed Download
- [var error: (any Error)?](skdownload/error.md)
  The error that prevented the content from being downloaded.
- [var contentURL: URL?](skdownload/contenturl.md)
  The local location of the downloaded file.
### Managing Downloaded Content
- [class func contentURL(forProductID: String) -> URL?](skdownload/contenturl(forproductid:).md)
  Returns the local location for the previously downloaded flie.
- [class func deleteContent(forProductID: String)](skdownload/deletecontent(forproductid:).md)
  Deletes the previously downloaded file.

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

## See Also

- [Unlocking purchased content](unlocking-purchased-content.md)
  Deliver content to the customer after validating the purchase.
- [Persisting a purchase](persisting-a-purchase.md)
  Keep a persistent record of a purchase to continue making the product available as needed.
- [Finishing a transaction](finishing-a-transaction.md)
  Finish the transaction to complete the purchase process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload)*