# serviceProviderData(for:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Calls a completion handler that returns the custom data for a Secure Element pass.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.12+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func serviceProviderData(for secureElementPass: PKSecureElementPass) async throws -> Data
```

## Parameters

- `secureElementPass`: The Secure Element pass to check for secure data.
- `completion`: This block takes the following parameters:

## See Also

- [class func isPassLibraryAvailable() -> Bool](pkpasslibrary/ispasslibraryavailable.md)
  Returns a Boolean value that indicates whether the pass library is available.
- [func passes() -> [PKPass]](pkpasslibrary/passes.md)
  Returns the passes in the user’s pass library that the app can access.
- [func passes(of: PKPassType) -> [PKPass]](pkpasslibrary/passes(of:).md)
  Returns the passes of the specified pass type.
- [func pass(withPassTypeIdentifier: String, serialNumber: String) -> PKPass?](pkpasslibrary/pass(withpasstypeidentifier:serialnumber:).md)
  Returns the pass with the specified pass type identifier and serial number.
- [func containsPass(PKPass) -> Bool](pkpasslibrary/containspass(_:).md)
  Returns a Boolean value that indicates whether the user’s pass library contains the specified pass.
- [var remoteSecureElementPasses: [PKSecureElementPass]](pkpasslibrary/remotesecureelementpasses.md)
  The Secure Element passes that PassKit stores on paired devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/serviceproviderdata(for:completion:))*