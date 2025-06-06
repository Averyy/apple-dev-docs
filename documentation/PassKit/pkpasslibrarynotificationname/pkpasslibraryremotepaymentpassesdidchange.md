# PKPassLibraryRemotePaymentPassesDidChange

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A notification that PassKit posts when it adds or removes a pass on a paired remote device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let PKPassLibraryRemotePaymentPassesDidChange: PKPassLibraryNotificationName
```

#### Discussion

PassKit posts this notification on an arbitary queue, and only does so if an instance of `PKPassLibrary` exists. The notification’s user info dictionary describes the changes. See [`PKPassLibrary`](pkpasslibrary.md) for the keys it uses.

## See Also

- [static let PKPassLibraryDidChange: PKPassLibraryNotificationName](pkpasslibrarynotificationname/pkpasslibrarydidchange.md)
  A notification that PassKit posts when the pass library changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationname/pkpasslibraryremotepaymentpassesdidchange)*