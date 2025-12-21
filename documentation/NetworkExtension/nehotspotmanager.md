# NEHotspotManager

**Framework**: Network Extension  
**Kind**: class

A class that you use to enable or disable the hotspot evaluation and authentication provider extensions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
final class NEHotspotManager
```

#### Overview

Use an `NEHotspotManager` to perform custom authentication of Wi-Fi hotspots in app extensions rather than in an app. Using sandboxed extensions is more performant and secure than performing hotspot authentication in an app.

The manager is responsible for two extensions:

- An [`NEHotspotEvaluationProvider`](nehotspotevaluationprovider.md) to evaluate detected Wi-Fi hotspots.
- An [`NEHotspotAuthenticationProvider`](nehotspotauthenticationprovider.md) to authenticate with evaluated hotspots.

##### Implementing an Evaluation Provider

The [`NEHotspotEvaluationProvider`](nehotspotevaluationprovider.md) managed by this class can receive a [`NEHotspotHelperCommandType.filterScanList`](nehotspothelpercommandtype/filterscanlist.md) command at any time. Respond to this by indicating which of the listed networks your provider can confidently handle.

When the device initially joins a network, the hotspot helper enters the  state. In this state, each [`NEHotspotEvaluationProvider`](nehotspotevaluationprovider.md) instance receives a command of type [`NEHotspotHelperCommandType.evaluate`](nehotspothelpercommandtype/evaluate.md). If one or more evaluation providers indicates it can handle the network, the hotspot helper chooses the one with the highest confidence level before entering the  state. If no evaluation provider instance claims the network, the state machine enters the  state.

##### Using the State Machine During Authentication

In the authenticating state, your [`NEHotspotAuthenticationProvider`](nehotspotauthenticationprovider.md) receives the [`NEHotspotHelperCommandType.authenticate`](nehotspothelpercommandtype/authenticate.md) command. At this point, the provider performs any network processing needed to make the network available for general network traffic. If authentication is successful, your provider calls [`createResponse(_:)`](nehotspothelpercommand/createresponse(_:).md) on the command to create a [`NEHotspotHelperResult.success`](nehotspothelperresult/success.md) response and returns it.

While in the authenticating state, if your authentication provider determines that it needs interaction from the person using the device, create an alert with [`UNUserNotificationCenter`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenter), and respond to the command with an [`NEHotspotHelperResult.uiRequired`](nehotspothelperresult/uirequired.md) response. This transitions the state machine to a  state, and the provider receives a command of type [`NEHotspotHelperCommandType.presentUI`](nehotspothelpercommandtype/presentui.md). The extension runs in the background in this state until the app collects the needed information from the person. After the app uses the information to complete the authentication, return a success response to enter the authenticated state.

After a successful authentication, the network enters a  state when the network is joined again. In this state, the provider periodically receives the [`NEHotspotHelperCommandType.maintain`](nehotspothelpercommandtype/maintain.md) command. To process this command, determine if the network remains able to carry general network traffic, and return success if this is the case. If not, and the network again requires authentication, return an [`NEHotspotHelperResult.authenticationRequired`](nehotspothelperresult/authenticationrequired.md) result.

## Topics

### Accessing the shared instance
- [static var shared: NEHotspotManager](nehotspotmanager/shared.md)
  The shared instance of the hotspot manager class.
### Accessing provider properties
- [var isEnabled: Bool](nehotspotmanager/isenabled.md)
  A Boolean value that indicates whether the configuration is enabled.
- [var evaluationProviderBundleIdentifier: String?](nehotspotmanager/evaluationproviderbundleidentifier.md)
  The bundle identifier of the hotspot evaluation provider.
- [var authenticationProviderBundleIdentifier: String?](nehotspotmanager/authenticationproviderbundleidentifier.md)
  The bundle identifier of the hotspot authentication provider.
### Authenticating with Safari domains
- [var safariDomains: [String]](nehotspotmanager/safaridomains.md)
  An array of domain strings for use with Safari-based hotspot authentication.
### Identifying pre-evaluated Wi-Fi networks
- [var evaluatedSSIDs: [String]](nehotspotmanager/evaluatedssids.md)
  An array of pre-evaluated Wi-Fi SSID strings.
### Managing the saved configuration
- [func loadFromPreferences() async throws](nehotspotmanager/loadfrompreferences.md)
  Loads the hotspot manager configuration from the Network Extension preferences.
- [func saveToPreferences() async throws](nehotspotmanager/savetopreferences.md)
  Saves the HotspotManager configuration in the Network Extension preferences.
- [func removeFromPreferences() async throws](nehotspotmanager/removefrompreferences.md)
  Removes the hotspot manager configuration from the Network Extension preferences.
### Identifying manager errors
- [NEHotspotManager.Error](nehotspotmanager/error.md)
  An enumeration of errors thrown by hotspot manager methods.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NEHotspotEvaluationProvider](nehotspotevaluationprovider.md)
  A protocol that defines methods and properties your extension implements to handle evaluate and filter scan list commands.
- [protocol NEHotspotAuthenticationProvider](nehotspotauthenticationprovider.md)
  A protocol that defines methods that your extension adopts to start and stop the extension, and to handle commands to authenticate with the hotspot network.
- [class NEHotspotEvaluationProviderConfiguration](nehotspotevaluationproviderconfiguration.md)
  A class that defines configuration options for use in NetworkExtension evaluation providers.
- [class NEHotspotAuthenticationProviderConfiguration](nehotspotauthenticationproviderconfiguration.md)
  A class that defines configuration options for use in NetworkExtension authentication providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotmanager)*