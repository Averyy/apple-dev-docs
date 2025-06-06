# pass(withPassTypeIdentifier:serialNumber:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns the pass with the specified pass type identifier and serial number.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func pass(withPassTypeIdentifier identifier: String, serialNumber: String) -> PKPass?
```

#### Return Value

The pass with the specified pass type identifier and serial number, or `nil` if there isn’t such a pass or if the app doesn’t have the appropriate entitlement.

## Parameters

- `identifier`: The pass’s pass type identifier.
- `serialNumber`: The pass’s serial number.

## See Also

- [class func isPassLibraryAvailable() -> Bool](pkpasslibrary/ispasslibraryavailable.md)
  Returns a Boolean value that indicates whether the pass library is available.
- [func passes() -> [PKPass]](pkpasslibrary/passes.md)
  Returns the passes in the user’s pass library that the app can access.
- [func passes(of: PKPassType) -> [PKPass]](pkpasslibrary/passes(of:).md)
  Returns the passes of the specified pass type.
- [func containsPass(PKPass) -> Bool](pkpasslibrary/containspass(_:).md)
  Returns a Boolean value that indicates whether the user’s pass library contains the specified pass.
- [func serviceProviderData(for: PKSecureElementPass, completion: (Data?, (any Error)?) -> Void)](pkpasslibrary/serviceproviderdata(for:completion:).md)
  Calls a completion handler that returns the custom data for a Secure Element pass.
- [var remoteSecureElementPasses: [PKSecureElementPass]](pkpasslibrary/remotesecureelementpasses.md)
  The Secure Element passes that PassKit stores on paired devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/pass(withpasstypeidentifier:serialnumber:))*