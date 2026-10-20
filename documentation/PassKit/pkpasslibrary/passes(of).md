# passes(of:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Returns the passes of the specified pass type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func passes(of passType: PKPassType) -> [PKPass]
```

```objc
- (NSArray<PKPass *> *) passesOfType:(PKPassType) passType;
```

#### Return Value

An array of passes of the specified type.

## Parameters

- `passType`: One of the pass types in [`PKPassType`](../pkpasstype.md).

## See Also

### Accessing passes
- [class func isPassLibraryAvailable() -> Bool](./ispasslibraryavailable%28%29.md)
  Returns a Boolean value that indicates whether the pass library is available.
- [func passes() -> [PKPass]](./passes%28%29.md)
  Returns the passes in the user’s pass library that the app can access.
- [func pass(withPassTypeIdentifier: String, serialNumber: String) -> PKPass?](./pass%28withpasstypeidentifier,serialnumber%29.md)
  Returns the pass with the specified pass type identifier and serial number.
- [func containsPass(PKPass) -> Bool](./containspass%28_%29.md)
  Returns a Boolean value that indicates whether the user’s pass library contains the specified pass.
- [func serviceProviderData(for: PKSecureElementPass, completion: (Data?, (any Error)?) -> Void)](./serviceproviderdata%28for,completion%29.md)
  Calls a completion handler that returns the custom data for a Secure Element pass.
- [var remoteSecureElementPasses: [PKSecureElementPass]](./remotesecureelementpasses.md)
  The Secure Element passes that PassKit stores on paired devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/passes(of:))*