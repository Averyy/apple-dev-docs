# usesUbiquitousStorage

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns whether the document object stores its contents in the user’s iCloud document storage.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class var usesUbiquitousStorage: Bool { get }
```

```objc
@property (class, readonly) BOOL usesUbiquitousStorage;
```

#### Discussion

This method’s default implementation returns [`true`](../../Swift/true.md) if your app has a valid iCloud document storage entitlement (`com.apple.developer.ubiquity-container-identifiers` or `com.apple.developer.icloud-container-identifiers`, as described in [Entitlement Key Reference](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/AboutEntitlements.html#//apple_ref/doc/uid/TP40011195)). When this method returns [`true`](../../Swift/true.md), the system adds new menu items and other UI for iCloud documents, as appropriate, and allows documents to be saved or moved into the primary iCloud container. (The primary iCloud container is the one identified by the first container identifier string in the iCloud Containers list in the Xcode target editor.)

To indicate that your [`NSDocument`](../nsdocument.md) subclass does not use iCloud storage, override this method to return [`false`](../../Swift/false.md).

## See Also

### Storing Documents in iCloud
- [func moveToUbiquityContainer(Any?)](./movetoubiquitycontainer%28_%29.md)
  Moves the document to the user’s iCloud storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/usesubiquitousstorage)*