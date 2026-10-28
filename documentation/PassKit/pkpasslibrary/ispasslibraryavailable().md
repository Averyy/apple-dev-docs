# isPassLibraryAvailable()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the pass library is available.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func isPassLibraryAvailable() -> Bool
```

```objc
+ (BOOL) isPassLibraryAvailable;
```

## Return Value

[`true`](../../Swift/true.md) if the pass library is available; otherwise, [`false`](../../Swift/false.md).

## Discussion

This method exists because the pass library may be unavailable even if the [`PKPassLibrary`](../pkpasslibrary.md) class exists.

> **Note**:  Don’t use this method to determine whether the user can add passes on the device. A device may have a pass library, but still not be able to add passes. Use the [`PKAddPassesViewController`](../pkaddpassesviewcontroller.md) class’s [`canAddPasses()`](../pkaddpassesviewcontroller/canaddpasses%28%29.md) method instead.

## See Also

### Accessing passes
- [func passes() -> [PKPass]](./passes%28%29.md)
  Returns the passes in the user’s pass library that the app can access.
- [func passes(of: PKPassType) -> [PKPass]](./passes%28of%29.md)
  Returns the passes of the specified pass type.
- [func pass(withPassTypeIdentifier: String, serialNumber: String) -> PKPass?](./pass%28withpasstypeidentifier,serialnumber%29.md)
  Returns the pass with the specified pass type identifier and serial number.
- [func containsPass(PKPass) -> Bool](./containspass%28_%29.md)
  Returns a Boolean value that indicates whether the user’s pass library contains the specified pass.
- [func serviceProviderData(for: PKSecureElementPass, completion: (Data?, (any Error)?) -> Void)](./serviceproviderdata%28for,completion%29.md)
  Calls a completion handler that returns the custom data for a Secure Element pass.
- [var remoteSecureElementPasses: [PKSecureElementPass]](./remotesecureelementpasses.md)
  The Secure Element passes that PassKit stores on paired devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/ispasslibraryavailable())*