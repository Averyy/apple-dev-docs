# PKPass

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that represents a single pass.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class PKPass
```

#### Overview

The properties of this class correspond to fields of the pass. For details about what individual fields mean, see [`Pass`](https://developer.apple.com/documentation/WalletPasses/Pass).

## Topics

### Creating a pass
- [init(data: Data) throws](pkpass/init(data:).md)
  Creates a pass using the data you provide.
### Identifying a pass
- [var passType: PKPassType](pkpass/passtype.md)
  The pass’s type.
- [enum PKPassType](pkpasstype.md)
  Types of passes.
- [var secureElementPass: PKSecureElementPass?](pkpass/secureelementpass.md)
  The pass that contains an accompanying credential that the device stores in the Secure Element.
- [var serialNumber: String](pkpass/serialnumber.md)
  A value that uniquely identifies the pass.
- [var passTypeIdentifier: String](pkpass/passtypeidentifier.md)
  The pass’s pass type identifier.
- [var deviceName: String](pkpass/devicename.md)
  The name of the device that hosts the pass.
- [var localizedName: String](pkpass/localizedname.md)
  The localized name for the pass’s template.
- [var localizedDescription: String](pkpass/localizeddescription.md)
  The pass’s localized description.
- [var isRemotePass: Bool](pkpass/isremotepass.md)
  A Boolean value that indicates whether the pass is on a paired device, such as an Apple Watch.
- [var paymentPass: PKPaymentPass?](pkpass/paymentpass.md)
  The underlying payment pass.
### Getting the web service information
- [var webServiceURL: URL?](pkpass/webserviceurl.md)
  The URL for the web service.
- [var authenticationToken: String?](pkpass/authenticationtoken.md)
  The token for authenticating update requests.
### Getting the display attributes
- [var icon: UIImage](pkpass/icon.md)
  The pass icon.
- [func localizedValue(forFieldKey: String) -> Any?](pkpass/localizedvalue(forfieldkey:).md)
  Returns the localized value for a specified field of the pass.
- [var organizationName: String](pkpass/organizationname.md)
  The name of the organization that creates the pass.
- [var relevantDate: Date?](pkpass/relevantdate.md)
  The date when the pass is most likely to be useful or necessary.
- [class PKPassRelevantDate](pkpassrelevantdate.md)
### Getting the Wallet URL
- [var passURL: URL?](pkpass/passurl.md)
  The URL that opens the pass in the Wallet app.
### Providing contextual information
- [var userInfo: [AnyHashable : Any]?](pkpass/userinfo.md)
  Developer-specific custom data.
### Instance Properties
- [var relevantDates: [PKPassRelevantDate]](pkpass/relevantdates.md)

## Relationships

### Inherits From
- [PKObject](pkobject.md)
### Inherited By
- [PKSecureElementPass](pksecureelementpass.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKSecureElementPass](pksecureelementpass.md)
  A pass with a credential that the device stores in a certified payment information chip.
- [class PKAddSecureElementPassConfiguration](pkaddsecureelementpassconfiguration.md)
  An object that describes the configuration of a secure element payment pass.
- [class PKAddSecureElementPassViewController](pkaddsecureelementpassviewcontroller.md)
  A view controller that manages the addition of secure element payment passes.
- [class PKAddPassesViewController](pkaddpassesviewcontroller.md)
  Lets your app show a pass and prompt the user to add that pass to the pass library.
- [struct AsyncShareablePassConfiguration](asyncshareablepassconfiguration.md)
- [class PKShareSecureElementPassViewController](pksharesecureelementpassviewcontroller.md)
- [protocol PKShareSecureElementPassViewControllerDelegate](pksharesecureelementpassviewcontrollerdelegate.md)
- [PKShareablePassMetadata.Preview](pkshareablepassmetadata/preview-swift.class.md)
- [enum PKShareSecureElementPassResult](pksharesecureelementpassresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass)*