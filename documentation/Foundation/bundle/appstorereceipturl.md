# appStoreReceiptURL

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The file URL for the bundle’s App Store receipt.

**Availability**:
- iOS 7.0+ - Deprecated in 18.0
- iPadOS 7.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 2.0+ - Deprecated in 11.0

> **Deprecated**: Use AppTransaction.shared and Transaction.all from StoreKit.framework instead

## Declaration

```swift
var appStoreReceiptURL: URL? { get }
```

```objc
@property (copy, readonly, nullable) NSURL * appStoreReceiptURL;
```

## Discussion

> **Note**:  The receipt isn’t necessary if you use [`AppTransaction`](../../StoreKit/apptransaction.md) to validate the app download, or [`Transaction`](../../StoreKit/transaction.md) to validate in-app purchases. Only use the receipt if your app uses the [Original API for Apple In-App Purchase](../../StoreKit/original-api-for-in-app-purchase.md), or needs the receipt to validate the app download because it can’t use [`AppTransaction`](../../StoreKit/apptransaction.md).

Use this app bundle property to locate the app receipt if it’s present; this property is `nil` if the receipt isn’t present. In the rare case a receipt is invalid or missing in an app that a user downloads from the App Store, use [`SKReceiptRefreshRequest`](../../StoreKit/skreceiptrefreshrequest.md) to request a new receipt. For information about validating receipts, see [Choosing a receipt validation technique](../../StoreKit/choosing-a-receipt-validation-technique.md).

You can’t use the general best practice of weak linking using the [`responds(to:)`](../../ObjectiveC/nsobjectprotocol/responds%28to%29.md) method here; the method’s implementation uses the [`doesNotRecognizeSelector(_:)`](../../ObjectiveC/nsobject-swift.class/doesnotrecognizeselector%28_%29.md) method.

### Get the receipt in testing environments

Receipts aren’t initially present in iOS and iPadOS apps in the sandbox environment and in Xcode. Apps get a receipt after the tester completes the first in-app purchase. When your app checks [`appStoreReceiptURL`](./appstorereceipturl.md) and finds that it’s `nil`, assume the tester is a new customer and has no access to premium content. For Mac apps running in TestFlight, the receipt is always present.

## See Also

### Getting the standard bundle directories
- [var resourceURL: URL?](./resourceurl.md)
  The file URL of the bundle’s subdirectory containing resource files.
- [var executableURL: URL?](./executableurl.md)
  The file URL of the receiver’s executable file.
- [var privateFrameworksURL: URL?](./privateframeworksurl.md)
  The file URL of the bundle’s subdirectory containing private frameworks.
- [var sharedFrameworksURL: URL?](./sharedframeworksurl.md)
  The file URL of the receiver’s subdirectory containing shared frameworks.
- [var builtInPlugInsURL: URL?](./builtinpluginsurl.md)
  The file URL of the receiver’s subdirectory containing plug-ins.
- [func url(forAuxiliaryExecutable: String) -> URL?](./url%28forauxiliaryexecutable%29.md)
  Returns the file URL of the executable with the specified name in the receiver’s bundle.
- [var sharedSupportURL: URL?](./sharedsupporturl.md)
  The file URL of the bundle’s subdirectory containing shared support files.
- [var resourcePath: String?](./resourcepath.md)
  The full pathname of the bundle’s subdirectory containing resources.
- [var executablePath: String?](./executablepath.md)
  The full pathname of the receiver’s executable file.
- [var privateFrameworksPath: String?](./privateframeworkspath.md)
  The full pathname of the bundle’s subdirectory containing private frameworks.
- [var sharedFrameworksPath: String?](./sharedframeworkspath.md)
  The full pathname of the bundle’s subdirectory containing shared frameworks.
- [var builtInPlugInsPath: String?](./builtinpluginspath.md)
  The full pathname of the receiver’s subdirectory containing plug-ins.
- [func path(forAuxiliaryExecutable: String) -> String?](./path%28forauxiliaryexecutable%29.md)
  Returns the full pathname of the executable with the specified name in the receiver’s bundle.
- [var sharedSupportPath: String?](./sharedsupportpath.md)
  The full pathname of the bundle’s subdirectory containing shared support files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/appstorereceipturl)*