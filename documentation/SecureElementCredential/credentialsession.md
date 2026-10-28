# CredentialSession

**Framework**: SecureElementCredential  
**Kind**: class  
**Role**: Class

A class for performing actions on a credential stored in the Secure Element.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
actor CredentialSession
```

## Mentions

- [Accessing and using secure element credentials](./accessing-and-using-secure-element-credentials.md)

## Overview

Create a credential session with the [`startSession()`](./credentialsession/startsession%28%29.md) method. After you start a session, the session has three states:

- **Management**: In this default state, you can list, add, and delete credentials in the Secure Element.
- **Wired**: The wired state allows you to exchange data with a credential-corresponding entity (an *applet*) in the Secure Element.
- **Card Emulation**: In the card emulation state, your credential can communicate with a contactless card reader.

The framework provides SwiftUI and UIKit user interfaces for your app to display while using the wired and card emulation states.

You can read the current state at any time from the [`state`](./credentialsession/state-swift.property.md) property. The [`eventStream`](./credentialsession/eventstream.md) property provides an [`AsyncStream`](../Swift/asyncstream.md) of events from both your own actions on credentials and outside sources like detecting an NFC reader’s RF field.

An app can have only one active session at a time. When your app no longer needs the credential session, call [`invalidate()`](./credentialsession/invalidate%28%29.md). If your app goes into the background, the system automatically invalidates your session after a short delay. In wired mode, the system invalidates the session if it goes 15 seconds without performing a [`transceive(_:)`](./credentialsession/transceive%28_%29.md) call.

### Use a session in an app extension

Certain methods in [`CredentialSession`](./credentialsession.md) are only appropriate for use in apps. If you’re writing an app extension, such as for an identity service provider, use only the following methods:

- [`startSession()`](./credentialsession/startsession%28%29.md)
- [`listCredentials()`](./credentialsession/listcredentials%28%29.md)
- [`performWiredTransaction(using:over:instanceAID:)`](./credentialsession/performwiredtransaction%28using,over,instanceaid%29.md)
- [`transceive(_:)`](./credentialsession/transceive%28_%29.md)
- [`endWiredMode()`](./credentialsession/endwiredmode%28%29.md)
- [`invalidate()`](./credentialsession/invalidate%28%29.md)

## Topics

### Verifying eligibility
- [static var isEligible: Bool](./credentialsession/iseligible.md)
  A Boolean value that indicates whether the app or app extension is eligible to start a credential session.
### Accessing hardware information
- [var secureElementInfo: CredentialSession.SecureElementInfo](./credentialsession/secureelementinfo-swift.property.md)
  A property that provides information about the Secure Element hardware.
- [CredentialSession.SecureElementInfo](./credentialsession/secureelementinfo-swift.struct.md)
  A type that provides information about the Secure Element hardware.
### Managing the credential session life cycle
- [static func startSession() async throws -> CredentialSession](./credentialsession/startsession%28%29.md)
  Requests a session to view, manage, or use credentials in the Secure Element.
- [func invalidate() async throws](./credentialsession/invalidate%28%29.md)
  Inmediately invalidates a session.
### Accessing the session state
- [var state: CredentialSession.State](./credentialsession/state-swift.property.md)
  The current state of the session.
- [CredentialSession.State](./credentialsession/state-swift.enum.md)
  An enumeration of the possible states of a card session.
### Accessing credentials
- [func listCredentials() async throws -> [CredentialSession.Credential]](./credentialsession/listcredentials%28%29.md)
  Retrieves a list of of credentials to which the app has access rights.
- [CredentialSession.Credential](./credentialsession/credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.
### Acquiring exclusive foreground privileges
- [func acquirePresentmentAssertion() async throws -> CredentialSession.PresentmentIntentAssertion](./credentialsession/acquirepresentmentassertion%28%29.md)
  Indicates that the app intends to present a credential to a contactless interface.
- [CredentialSession.PresentmentIntentAssertion](./credentialsession/presentmentintentassertion.md)
  An object that signals your app’s intention to make exclusive use of the device’s contactless features.
### Handling session events
- [var eventStream: AsyncStream<CredentialSession.Event>](./credentialsession/eventstream.md)
  An asynchronous stream of session events.
- [CredentialSession.Event](./credentialsession/event.md)
  Events produced by a credential session, such as connectivity events and errors.
### Managing a credential
- [func provisionCredential(configurationUUID: UUID, name: String) async throws -> CredentialSession.Credential](./credentialsession/provisioncredential%28configurationuuid,name%29.md)
  Creates a credential in the Secure Element.
- [func deleteCredential(CredentialSession.Credential) async throws](./credentialsession/deletecredential%28_%29.md)
  Deletes a credential on the Secure Element.
### Performing wired mode actions
- [func performWiredTransaction(using: CredentialSession.Credential, over: UIScene, instanceAID: Data) async throws](./credentialsession/performwiredtransaction%28using,over,instanceaid%29.md)
  Enters wired mode with user authentication.
- [func enterWiredMode(using: CredentialSession.Credential) async throws](./credentialsession/enterwiredmode%28using%29.md)
  Enters wired mode to perform maintenance operations with the given credential.
- [func transceive(Data) async throws -> Data](./credentialsession/transceive%28_%29.md)
  Send a wired command Application Protocol Data Unit (APDU) to the credential to complete a transaction or a card content management task.
- [func endWiredMode() async throws](./credentialsession/endwiredmode%28%29.md)
  Ends wired mode and returns to management state.
### Performing card emulation
- [func performCardEmulationTransactionWithCurrentCredential(over: UIScene, options: CredentialSession.CardEmulationOptions) async throws](./credentialsession/performcardemulationtransactionwithcurrentcredential%28over,options%29.md)
  Activate the current credential in Wired mode to enter Card Emulation mode.
- [func performTransaction(using: CredentialSession.Credential, over: UIScene, options: CredentialSession.CardEmulationOptions) async throws](./credentialsession/performtransaction%28using,over,options%29.md)
  Prompts the user for authorization and then activate a credential for card emulation.
- [CredentialSession.CardEmulationOptions](./credentialsession/cardemulationoptions.md)
  Options for customizing card emulation behavior.
- [func endCardEmulation() async throws](./credentialsession/endcardemulation%28%29.md)
  Ends card emulation and transitions the session to management state.
### Using SwiftUI
- [func configuration() async throws -> CredentialTransaction.Configuration](./credentialsession/configuration%28%29.md)
  Retrieves a transaction configuration related to this session.
- [CredentialTransaction.Configuration](./credentialtransaction/configuration.md)
  An object that provides configuration information for a transaction that the client intends to perform.
### Handling errors
- [CredentialSession.ErrorCode](./credentialsession/errorcode.md)
  An error encountered by a credential session.
### Infrequently-used functionality
- [init()](./credentialsession/init%28%29.md)
  Creates an empty credential session.
### Structures
- [CredentialSession.ConnectivityEvent](./credentialsession/connectivityevent.md)
  An event that a credential receives during card emulation.
### Enumerations
- [CredentialSession.NFCFieldInformation](./credentialsession/nfcfieldinformation.md)
  The state of an NFC RF field.

## Relationships

### Conforms To
- [Actor](../Swift/actor.md)
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession)*