# appStoreReceiptURL

**Framework**: Foundation  
**Kind**: property

The file URL for the bundle’s App Store receipt.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var appStoreReceiptURL: URL? { get }
```

#### Discussion

> **Note**:  The receipt isn’t necessary if you use [`AppTransaction`](https://developer.apple.com/documentation/StoreKit/AppTransaction) to validate the app download, or [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction) to validate in-app purchases. Only use the receipt if your app uses the [`Original API for In-App Purchase`](https://developer.apple.com/documentation/StoreKit/original-api-for-in-app-purchase), or needs the receipt to validate the app download because it can’t use [`AppTransaction`](https://developer.apple.com/documentation/StoreKit/AppTransaction).

Use this app bundle property to locate the app receipt if it’s present; this property is `nil` if the receipt isn’t present. In the rare case a receipt is invalid or missing in an app that a user downloads from the App Store, use [`SKReceiptRefreshRequest`](https://developer.apple.com/documentation/StoreKit/SKReceiptRefreshRequest) to request a new receipt. For information about validating receipts, see [`Choosing a receipt validation technique`](https://developer.apple.com/documentation/StoreKit/choosing-a-receipt-validation-technique).

You can’t use the general best practice of weak linking using the [`responds(to:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/responds(to:)) method here; the method’s implementation uses the [`doesNotRecognizeSelector(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/doesNotRecognizeSelector(_:)) method.

##### Get the Receipt in Testing Environments

Receipts aren’t initially present in iOS and iPadOS apps in the sandbox environment and in Xcode. Apps get a receipt after the tester completes the first in-app purchase. When your app checks [`appStoreReceiptURL`](bundle/appstorereceipturl.md) and finds that it’s `nil`, assume the tester is a new customer and has no access to premium content. For Mac apps running in TestFlight, the receipt is always present.

## See Also

- [var resourceURL: URL?](bundle/resourceurl.md)
  The file URL of the bundle’s subdirectory containing resource files.
- [var executableURL: URL?](bundle/executableurl.md)
  The file URL of the receiver’s executable file.
- [var privateFrameworksURL: URL?](bundle/privateframeworksurl.md)
  The file URL of the bundle’s subdirectory containing private frameworks.
- [var sharedFrameworksURL: URL?](bundle/sharedframeworksurl.md)
  The file URL of the receiver’s subdirectory containing shared frameworks.
- [var builtInPlugInsURL: URL?](bundle/builtinpluginsurl.md)
  The file URL of the receiver’s subdirectory containing plug-ins.
- [func url(forAuxiliaryExecutable: String) -> URL?](bundle/url(forauxiliaryexecutable:).md)
  Returns the file URL of the executable with the specified name in the receiver’s bundle.
- [var sharedSupportURL: URL?](bundle/sharedsupporturl.md)
  The file URL of the bundle’s subdirectory containing shared support files.
- [var resourcePath: String?](bundle/resourcepath.md)
  The full pathname of the bundle’s subdirectory containing resources.
- [var executablePath: String?](bundle/executablepath.md)
  The full pathname of the receiver’s executable file.
- [var privateFrameworksPath: String?](bundle/privateframeworkspath.md)
  The full pathname of the bundle’s subdirectory containing private frameworks.
- [var sharedFrameworksPath: String?](bundle/sharedframeworkspath.md)
  The full pathname of the bundle’s subdirectory containing shared frameworks.
- [var builtInPlugInsPath: String?](bundle/builtinpluginspath.md)
  The full pathname of the receiver’s subdirectory containing plug-ins.
- [func path(forAuxiliaryExecutable: String) -> String?](bundle/path(forauxiliaryexecutable:).md)
  Returns the full pathname of the executable with the specified name in the receiver’s bundle.
- [var sharedSupportPath: String?](bundle/sharedsupportpath.md)
  The full pathname of the bundle’s subdirectory containing shared support files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/appstorereceipturl)*