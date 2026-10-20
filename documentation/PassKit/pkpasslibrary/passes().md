# passes()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Returns the passes in the user’s pass library that the app can access.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func passes() -> [PKPass]
```

```objc
- (NSArray<PKPass *> *) passes;
```

#### Return Value

The passes in the user’s pass library.

#### Discussion

Your app only has access to certain passes according to its entitlements. PassKit doesn’t return passes that your app can’t access.

Passes don’t have a fixed order. Calling this method multiple times may return the same passes, but in a different order.

## See Also

### Accessing passes
- [class func isPassLibraryAvailable() -> Bool](./ispasslibraryavailable%28%29.md)
  Returns a Boolean value that indicates whether the pass library is available.
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

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/passes())*