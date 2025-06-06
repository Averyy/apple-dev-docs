# PKPassLibrary

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

Provides an interface to the user’s library of passes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class PKPassLibrary
```

#### Overview

The `PKPassLibrary` isn’t thread-safe. Use instances of this class only on a single thread.

## Topics

### Accessing passes
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
- [func serviceProviderData(for: PKSecureElementPass, completion: (Data?, (any Error)?) -> Void)](pkpasslibrary/serviceproviderdata(for:completion:).md)
  Calls a completion handler that returns the custom data for a Secure Element pass.
- [var remoteSecureElementPasses: [PKSecureElementPass]](pkpasslibrary/remotesecureelementpasses.md)
  The Secure Element passes that PassKit stores on paired devices.
### Adding passes
- [func canAddSecureElementPass(primaryAccountIdentifier: String) -> Bool](pkpasslibrary/canaddsecureelementpass(primaryaccountidentifier:).md)
  Returns a Boolean value that indicates whether PassKit can add a Secure Element pass for the specified account.
- [func canAddFelicaPass() -> Bool](pkpasslibrary/canaddfelicapass.md)
  Returns a Boolean value that indicates whether the library can add FeliCa™ passes.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](pkpasslibrary/addpasses(_:withcompletionhandler:).md)
  Presents a user interface for adding multiple passes at once.
- [enum PKPassLibraryAddPassesStatus](pkpasslibraryaddpassesstatus.md)
  Statuses that PassKit uses when it adds passes to the pass library.
### Managing passes
- [var isSecureElementPassActivationAvailable: Bool](pkpasslibrary/issecureelementpassactivationavailable.md)
  A Boolean value that indicates whether the device supports creating Secure Element passes.
- [func activate(PKSecureElementPass, activationData: Data, completion: ((Bool, (any Error)?) -> Void)?)](pkpasslibrary/activate(_:activationdata:completion:).md)
  Activates a Secure Element pass using the specified data.
- [func replacePass(with: PKPass) -> Bool](pkpasslibrary/replacepass(with:).md)
  Replaces a pass in the user’s pass library with the specified pass.
- [func removePass(PKPass)](pkpasslibrary/removepass(_:).md)
  Removes the pass from the user’s pass library.
### Presenting and suppressing passes
- [func present(PKSecureElementPass)](pkpasslibrary/present(_:)-9467u.md)
  Presents a Secure Element pass.
- [class func isSuppressingAutomaticPassPresentation() -> Bool](pkpasslibrary/issuppressingautomaticpasspresentation.md)
  Returns a Boolean value that indicates whether the system suppresses the automatic presentation of Apple Pay passes.
- [class func requestAutomaticPassPresentationSuppression(responseHandler: (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken](pkpasslibrary/requestautomaticpasspresentationsuppression(responsehandler:).md)
  Prevents the device from automatically displaying the Apple Pay interface.
- [enum PKAutomaticPassPresentationSuppressionResult](pkautomaticpasspresentationsuppressionresult.md)
  The result of an attempt to suppress automatic pass presentation.
- [class func endAutomaticPassPresentationSuppression(withRequestToken: PKSuppressionRequestToken)](pkpasslibrary/endautomaticpasspresentationsuppression(withrequesttoken:).md)
  Reenables the automatic display of the Apple Pay interface.
- [typealias PKSuppressionRequestToken](pksuppressionrequesttoken.md)
  A token that represents a request to suppress the automatic presentation of payment passes.
### Setting up payments
- [func openPaymentSetup()](pkpasslibrary/openpaymentsetup.md)
  Opens the user interface to set up credit cards for Apple Pay.
### Signing data
- [func sign(Data, using: PKSecureElementPass, completion: (Data?, Data?, (any Error)?) -> Void)](pkpasslibrary/sign(_:using:completion:).md)
  Signs an opaque value using a cryptographic signature.
### Receiving notifications
- [struct PKPassLibraryNotificationKey](pkpasslibrarynotificationkey.md)
  The user info keys that a pass library notification uses.
- [struct PKPassLibraryNotificationName](pkpasslibrarynotificationname.md)
  The types of notifications that the pass library posts.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Methods
- [func encryptedServiceProviderData(for: PKSecureElementPass, completion: ([AnyHashable : Any]?, (any Error)?) -> Void)](pkpasslibrary/encryptedserviceproviderdata(for:completion:).md)
- [func passes(withReaderIdentifier: String) -> Set<PKSecureElementPass>](pkpasslibrary/passes(withreaderidentifier:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary)*