# containsPass(_:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the user’s pass library contains the specified pass.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func containsPass(_ pass: PKPass) -> Bool
```

```objc
- (BOOL) containsPass:(PKPass *) pass;
```

#### Return Value

[`true`](../../Swift/true.md) if the user’s pass library contains the pass; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method lets you determine that the pass library contains a pass even though your app can’t read or modify the pass. For example, an email client doesn’t have entitlements to read or write any passes from the library.

Your app can use this method to provide a UI that indicates whether a pass is already in the library.

## Parameters

- `pass`: The pass to query.

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
- [func serviceProviderData(for: PKSecureElementPass, completion: (Data?, (any Error)?) -> Void)](./serviceproviderdata%28for,completion%29.md)
  Calls a completion handler that returns the custom data for a Secure Element pass.
- [var remoteSecureElementPasses: [PKSecureElementPass]](./remotesecureelementpasses.md)
  The Secure Element passes that PassKit stores on paired devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/containspass(_:))*