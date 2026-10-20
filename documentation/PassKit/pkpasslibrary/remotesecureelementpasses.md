# remoteSecureElementPasses

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The Secure Element passes that PassKit stores on paired devices.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.12+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var remoteSecureElementPasses: [PKSecureElementPass] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<PKSecureElementPass *> * remoteSecureElementPasses;
```

#### Discussion

This is an array that contains the Secure Element passes from all of the device’s remote paired devices, such as an Apple Watch.

## See Also

### Accessing passes
- [class func isPassLibraryAvailable() -> Bool](./ispasslibraryavailable%28%29.md)
  Returns a Boolean value that indicates whether the pass library is available.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/remotesecureelementpasses)*