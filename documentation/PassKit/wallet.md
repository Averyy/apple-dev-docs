# Wallet

**Framework**: PassKit (Apple Pay and Wallet)

Manage tickets, boarding passes, payment cards and other passes in the Wallet app.

#### Overview

To access your pass using PassKit, add the Wallet capability to your app. Use the API in Wallet to access and manage different types of passes, including identity passes, payment passes, and digital car keys. You can choose to access all of the passes signed with your developer team identifier, or access a subset of pass types. For information on adding capabilities to your app, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app). For information on signing a pass, see [`Wallet Passes`](https://developer.apple.com/documentation/WalletPasses).

## Topics

### Essentials
- [Pass Type IDs Entitlement](../BundleResources/Entitlements/com.apple.developer.pass-type-identifiers.md)
  A list of identifiers that specify pass types that your app can access in Wallet.
- [Merchant IDs Entitlement](../BundleResources/Entitlements/com.apple.developer.in-app-payments.md)
  A list of merchant IDs your app uses for Apple Pay support.
- [com.apple.developer.in-app-identity-presentment](../BundleResources/Entitlements/com.apple.developer.in-app-identity-presentment.md)
  An entitlement that verifies age or identity.
- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)
  Initiate a request for identity information by prompting a user for permission and decrypting a response payload.
- [Verifying Wallet identity requests](verifying-wallet-identity-requests.md)
  Decrypt and verify an in-app presentment request on your server.
### Wallet Passes
- [Wallet Passes](../WalletPasses/WalletPasses.md)
  Create, distribute, and update passes for the Wallet app.
### Common data types
- [class PKObject](pkobject.md)
  An opaque type that acts as the superclass for the pass object.
- [class PKAddPassButton](pkaddpassbutton.md)
  Provides a button that enables users to add passes to Wallet.
- [class PKLabeledValue](pklabeledvalue.md)
  An object that can represent a detail about a payment card or other item.
- [struct AddPassToWalletButton](addpasstowalletbutton.md)
  A type that provides a button that enables people to add a new or existing pass to Apple Wallet.
- [struct AddPassToWalletButtonFilter](addpasstowalletbuttonfilter.md)
- [struct AddPassToWalletButtonResponse](addpasstowalletbuttonresponse.md)
- [struct AddPassToWalletButtonStyle](addpasstowalletbuttonstyle.md)
### Pass library
- [class PKPassLibrary](pkpasslibrary.md)
  Provides an interface to the user’s library of passes.
### General purpose passes
- [class PKSecureElementPass](pksecureelementpass.md)
  A pass with a credential that the device stores in a certified payment information chip.
- [class PKAddSecureElementPassConfiguration](pkaddsecureelementpassconfiguration.md)
  An object that describes the configuration of a secure element payment pass.
- [class PKAddSecureElementPassViewController](pkaddsecureelementpassviewcontroller.md)
  A view controller that manages the addition of secure element payment passes.
- [class PKPass](pkpass.md)
  An object that represents a single pass.
- [class PKAddPassesViewController](pkaddpassesviewcontroller.md)
  Lets your app show a pass and prompt the user to add that pass to the pass library.
- [struct AsyncShareablePassConfiguration](asyncshareablepassconfiguration.md)
- [class PKShareSecureElementPassViewController](pksharesecureelementpassviewcontroller.md)
- [protocol PKShareSecureElementPassViewControllerDelegate](pksharesecureelementpassviewcontrollerdelegate.md)
- [PKShareablePassMetadata.Preview](pkshareablepassmetadata/preview-swift.class.md)
- [enum PKShareSecureElementPassResult](pksharesecureelementpassresult.md)
### Identity passes and authorization
- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)
  Initiate a request for identity information by prompting a user for permission and decrypting a response payload.
- [Configuring your environment for the Verify with Wallet API](configuring-your-environment-for-the-verify-with-wallet-api.md)
  Set up your environment to use Verify with Wallet.
- [Verifying Wallet identity requests](verifying-wallet-identity-requests.md)
  Decrypt and verify an in-app presentment request on your server.
- [class PKIdentityPhotoIDDescriptor](pkidentityphotoiddescriptor.md)
  An object you use to request information from a user’s photo ID or equivalent document.
- [class PKIdentityAnyOfDescriptor](pkidentityanyofdescriptor.md)
  An object you use to request information from multiple identity documents.
- [class PKIdentityDriversLicenseDescriptor](pkidentitydriverslicensedescriptor.md)
  An object for requesting information from a user’s driver’s license or equivalent document.
- [class PKAddIdentityDocumentMetadata](pkaddidentitydocumentmetadata.md)
  The object for specifying the metadata necessary to provision identity documents.
- [class PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
  Configuration to define the identity document.
- [struct JPKIPassContents](jpkipasscontents.md)
  A set of actions for viewing and updating PINs, passwords, and signing abilities associated with digital identities on the JPKI applet.
- [class PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
  Configuration to define the identity document.
- [class PKAddPassMetadataPreview](pkaddpassmetadatapreview.md)
  A preview object that contains information representing the pass you add to Wallet.
- [class PKIdentityDocumentMetadata](pkidentitydocumentmetadata.md)
  A set of configured metadata that defines the required information to add the corresponding pass to Wallet.
- [class PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md)
  An object for requesting information from a user’s national ID card.
- [class PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md)
  A class that contains metadata indicating the specific product instance to provision.
### Identity sheet interactions and authorization
- [class PKIdentityAuthorizationController](pkidentityauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to allow a request for identity information.
- [class PKIdentityRequest](pkidentityrequest.md)
  An object that represents a request for identity information from a Wallet pass.
- [class PKIdentityDocument](pkidentitydocument.md)
  An object that represents the response to a request.
- [class PKIdentityElement](pkidentityelement.md)
  An object that represents the elements an app requests from identity documents.
- [class PKIdentityButton](pkidentitybutton.md)
  An object that displays a button to trigger the identity verification flow.
- [struct VerifyIdentityWithWalletButton](verifyidentitywithwalletbutton.md)
  A type that displays a button to present the identity verification flow.
- [struct VerifyIdentityWithWalletButtonLabel](verifyidentitywithwalletbuttonlabel.md)
  A type that represents the label you use with a verify identity button.
- [struct VerifyIdentityWithWalletButtonStyle](verifyidentitywithwalletbuttonstyle.md)
  A type that represents the style you use with a verify identity button.
### Payment passes
- [class PKPaymentPass](pkpaymentpass.md)
  An object that represents a provisioned payment card for in-app payments.
- [class PKAddPaymentPassViewController](pkaddpaymentpassviewcontroller.md)
  Displays an interface that lets users add cards to Apple Pay from within your app.
### Stored-value passes
- [class PKTransitPassProperties](pktransitpassproperties.md)
  The properties of a transit pass.
- [class PKSuicaPassProperties](pksuicapassproperties.md)
  The properties of a pass used as a ticket for the Suica transportation system.
- [class PKStoredValuePassProperties](pkstoredvaluepassproperties.md)
  An object that represents the properties of a pass that contains a balance used for specific transactions, such as a transit pass or loyalty card.
- [class PKStoredValuePassBalance](pkstoredvaluepassbalance.md)
  An object that represents a balance that’s available for transactions, such as points or money.
### Shareable passes
- [class PKAddShareablePassConfiguration](pkaddshareablepassconfiguration.md)
  An object that represents the data and action for a shared copy of pass.
- [class PKShareablePassMetadata](pkshareablepassmetadata.md)
  Information that you use to configure the sharing sheet for a pass.
- [enum PKAddShareablePassConfigurationPrimaryAction](pkaddshareablepassconfigurationprimaryaction.md)
  The kind of add action that the system performs with a pass.
### Digital car keys
- [class PKAddCarKeyPassConfiguration](pkaddcarkeypassconfiguration.md)
  A specialized configuration object that PassKit uses when it creates a digital car key.
- [class PKVehicleConnectionSession](pkvehicleconnectionsession.md)
- [protocol PKVehicleConnectionDelegate](pkvehicleconnectiondelegate.md)
- [enum PKVehicleConnectionSessionConnectionState](pkvehicleconnectionsessionconnectionstate.md)
### Issuer cards
- [Implementing Wallet Extensions](implementing-wallet-extensions.md)
  Support adding an issued card to Apple Pay from directly within Apple Wallet using Wallet Extensions.
- [class PKIssuerProvisioningExtensionHandler](pkissuerprovisioningextensionhandler.md)
  An abstract superclass for an app extension to add a payment card to Wallet.
- [protocol PKIssuerProvisioningExtensionAuthorizationProviding](pkissuerprovisioningextensionauthorizationproviding.md)
  A protocol for a UI app extension to authorize a user to add a payment card to Wallet.
### Errors
- [struct PKPassKitError](pkpasskiterror.md)
  Errors that the PassKit framework uses.
- [struct PKAddSecureElementPassError](pkaddsecureelementpasserror.md)
  An error object that PassKit uses when it adds Secure Element passes.
- [PKPassKitError.Code](pkpasskiterror/code.md)
  Errors that the PassKit framework uses.
- [PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/code.md)
  Error codes for problems that occur when you add a secure element passes.
- [enum PKAddPaymentPassError](pkaddpaymentpasserror.md)
  Error codes for adding payment passes.
- [struct PKIdentityError](pkidentityerror-swift.struct.md)
  A structure that represents an identity error.
- [PKIdentityError.Code](pkidentityerror-swift.struct/code.md)
  Error codes for identity operations.
- [struct PKShareSecureElementPassError](pksharesecureelementpasserror.md)
- [PKShareSecureElementPassError.Code](pksharesecureelementpasserror/code.md)
- [enum PKVehicleConnectionErrorCode](pkvehicleconnectionerrorcode.md)
- [enum PayWithApplePayButtonPaymentAuthorizationPhase](paywithapplepaybuttonpaymentauthorizationphase.md)
- [let PKPassKitErrorDomain: String](pkpasskiterrordomain.md)
  The error domain for PassKit errors.
- [let PKIdentityErrorDomain: String](pkidentityerrordomain.md)
  The error domain for identity errors.
- [let PKAddSecureElementPassErrorDomain: String](pkaddsecureelementpasserrordomain.md)
  The error domain for errors that occur when adding a secure pass.
- [let PKShareSecureElementPassErrorDomain: String](pksharesecureelementpasserrordomain.md)
### Deprecated
- [struct PayLaterView](paylaterview.md)
  A view that displays the Apple Pay Later visual merchandising widget.
- [class PKPayLaterView](pkpaylaterview.md)
  A view that displays the Apple Pay Later visual merchandising widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/wallet)*