# PKPassLibrary

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

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

```objc
@interface PKPassLibrary : NSObject
```

#### Overview

The `PKPassLibrary` isn’t thread-safe. Use instances of this class only on a single thread.

## Topics

### Accessing passes
- [class func isPassLibraryAvailable() -> Bool](./pkpasslibrary/ispasslibraryavailable%28%29.md)
  Returns a Boolean value that indicates whether the pass library is available.
- [func passes() -> [PKPass]](./pkpasslibrary/passes%28%29.md)
  Returns the passes in the user’s pass library that the app can access.
- [func passes(of: PKPassType) -> [PKPass]](./pkpasslibrary/passes%28of%29.md)
  Returns the passes of the specified pass type.
- [func pass(withPassTypeIdentifier: String, serialNumber: String) -> PKPass?](./pkpasslibrary/pass%28withpasstypeidentifier,serialnumber%29.md)
  Returns the pass with the specified pass type identifier and serial number.
- [func containsPass(PKPass) -> Bool](./pkpasslibrary/containspass%28_%29.md)
  Returns a Boolean value that indicates whether the user’s pass library contains the specified pass.
- [func serviceProviderData(for: PKSecureElementPass, completion: (Data?, (any Error)?) -> Void)](./pkpasslibrary/serviceproviderdata%28for,completion%29.md)
  Calls a completion handler that returns the custom data for a Secure Element pass.
- [var remoteSecureElementPasses: [PKSecureElementPass]](./pkpasslibrary/remotesecureelementpasses.md)
  The Secure Element passes that PassKit stores on paired devices.
### Automatically adding passes
- [func requestAuthorization(for: PKPassLibrary.Capability, completion: (PKPassLibrary.AuthorizationStatus) -> Void)](./pkpasslibrary/requestauthorization%28for,completion%29.md)
  Requests a person’s authorization to use a pass library capability.
- [PKPassLibrary.AuthorizationStatus](./pkpasslibrary/authorizationstatus.md)
  Statuses that indicate whether a person authorized your app to add a pass to their Wallet.
- [PKPassLibrary.Capability](./pkpasslibrary/capability.md)
  Features for which your app can request authorization from a person.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](./pkpasslibrary/addpasses%28_,withcompletionhandler%29.md)
  Presents a user interface for adding multiple passes at once.
### Adding passes
- [func canAddSecureElementPass(primaryAccountIdentifier: String) -> Bool](./pkpasslibrary/canaddsecureelementpass%28primaryaccountidentifier%29.md)
  Returns a Boolean value that indicates whether PassKit can add a Secure Element pass for the specified account.
- [func canAddFelicaPass() -> Bool](./pkpasslibrary/canaddfelicapass%28%29.md)
  Returns a Boolean value that indicates whether the library can add FeliCa™ passes.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](./pkpasslibrary/addpasses%28_,withcompletionhandler%29.md)
  Presents a user interface for adding multiple passes at once.
- [enum PKPassLibraryAddPassesStatus](./pkpasslibraryaddpassesstatus.md)
  Statuses that PassKit uses when it adds passes to the pass library.
### Managing passes
- [var isSecureElementPassActivationAvailable: Bool](./pkpasslibrary/issecureelementpassactivationavailable.md)
  A Boolean value that indicates whether the device supports creating Secure Element passes.
- [func activate(PKSecureElementPass, activationData: Data, completion: ((Bool, (any Error)?) -> Void)?)](./pkpasslibrary/activate%28_,activationdata,completion%29.md)
  Activates a Secure Element pass using the specified data.
- [func replacePass(with: PKPass) -> Bool](./pkpasslibrary/replacepass%28with%29.md)
  Replaces a pass in the user’s pass library with the specified pass.
- [func removePass(PKPass)](./pkpasslibrary/removepass%28_%29.md)
  Removes the pass from the user’s pass library.
### Presenting and suppressing passes
- [func present(PKSecureElementPass)](./pkpasslibrary/present%28_%29-9467u.md)
  Presents a Secure Element pass.
- [class func isSuppressingAutomaticPassPresentation() -> Bool](./pkpasslibrary/issuppressingautomaticpasspresentation%28%29.md)
  Returns a Boolean value that indicates whether the system suppresses the automatic presentation of Apple Pay passes.
- [class func requestAutomaticPassPresentationSuppression(responseHandler: (PKAutomaticPassPresentationSuppressionResult) -> Void) -> PKSuppressionRequestToken](./pkpasslibrary/requestautomaticpasspresentationsuppression%28responsehandler%29.md)
  Prevents the device from automatically displaying the Apple Pay interface.
- [enum PKAutomaticPassPresentationSuppressionResult](./pkautomaticpasspresentationsuppressionresult.md)
  The result of an attempt to suppress automatic pass presentation.
- [class func endAutomaticPassPresentationSuppression(withRequestToken: PKSuppressionRequestToken)](./pkpasslibrary/endautomaticpasspresentationsuppression%28withrequesttoken%29.md)
  Reenables the automatic display of the Apple Pay interface.
- [typealias PKSuppressionRequestToken](./pksuppressionrequesttoken.md)
  A token that represents a request to suppress the automatic presentation of payment passes.
### Setting up payments
- [func openPaymentSetup()](./pkpasslibrary/openpaymentsetup%28%29.md)
  Opens the user interface to set up credit cards for Apple Pay.
### Signing data
- [func sign(Data, using: PKSecureElementPass, completion: (Data?, Data?, (any Error)?) -> Void)](./pkpasslibrary/sign%28_,using,completion%29.md)
  Signs an opaque value using a cryptographic signature.
### Receiving notifications
- [struct PKPassLibraryNotificationKey](./pkpasslibrarynotificationkey.md)
  The user info keys that a pass library notification uses.
- [struct PKPassLibraryNotificationName](./pkpasslibrarynotificationname.md)
  The types of notifications that the pass library posts.
### Deprecated
- [Deprecated Symbols](./deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Methods
- [func addPasses(data: [Data], completion: (PKPassLibraryAddPassesStatus) -> Void)](./pkpasslibrary/addpasses%28data,completion%29.md)
- [func addPasses(fromArchiveAt: URL, completion: (PKPassLibraryAddPassesStatus) -> Void)](./pkpasslibrary/addpasses%28fromarchiveat,completion%29.md)
- [func addPasses(fromArchiveData: Data, completion: (PKPassLibraryAddPassesStatus) -> Void)](./pkpasslibrary/addpasses%28fromarchivedata,completion%29.md)
- [func authorizationStatus(for: PKPassLibrary.Capability) -> PKPassLibrary.AuthorizationStatus](./pkpasslibrary/authorizationstatus%28for%29.md)
- [func encryptedServiceProviderData(for: PKSecureElementPass, completion: ([AnyHashable : Any]?, (any Error)?) -> Void)](./pkpasslibrary/encryptedserviceproviderdata%28for,completion%29.md)
- [func openPaymentSetup(merchantIdentifier: String)](./pkpasslibrary/openpaymentsetup%28merchantidentifier%29.md)
- [func passes(withReaderIdentifier: String) -> Set<PKSecureElementPass>](./pkpasslibrary/passes%28withreaderidentifier%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary)*