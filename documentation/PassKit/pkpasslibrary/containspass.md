# containsPass(_:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user’s pass library contains the pass; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method lets you determine that the pass library contains a pass even though your app can’t read or modify the pass. For example, an email client doesn’t have entitlements to read or write any passes from the library.

Your app can use this method to provide a UI that indicates whether a pass is already in the library.

## Parameters

- `pass`: The pass to query.

## See Also

- [class func isPassLibraryAvailable() -> Bool](pkpasslibrary/ispasslibraryavailable.md)
  Returns a Boolean value that indicates whether the pass library is available.
- [func passes() -> [PKPass]](pkpasslibrary/passes.md)
  Returns the passes in the user’s pass library that the app can access.
- [func passes(of: PKPassType) -> [PKPass]](pkpasslibrary/passes(of:).md)
  Returns the passes of the specified pass type.
- [func pass(withPassTypeIdentifier: String, serialNumber: String) -> PKPass?](pkpasslibrary/pass(withpasstypeidentifier:serialnumber:).md)
  Returns the pass with the specified pass type identifier and serial number.
- [func serviceProviderData(for: PKSecureElementPass, completion: (Data?, (any Error)?) -> Void)](pkpasslibrary/serviceproviderdata(for:completion:).md)
  Calls a completion handler that returns the custom data for a Secure Element pass.
- [var remoteSecureElementPasses: [PKSecureElementPass]](pkpasslibrary/remotesecureelementpasses.md)
  The Secure Element passes that PassKit stores on paired devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/containspass(_:))*