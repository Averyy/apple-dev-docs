# InstallApplicationCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to install a third-party app on a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- macOS 10.9+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object InstallApplicationCommand.Command
```

## Topics

### Objects
- [object InstallApplicationCommand.Command.Attributes](installapplicationcommand/command-data.dictionary/attributes-data.dictionary.md)
  A dictionary that contains the initial attributes of the app.
- [object InstallApplicationCommand.Command.Configuration](installapplicationcommand/command-data.dictionary/configuration-data.dictionary.md)
  A dictionary that contains the configuration to install an enterprise app.
- [object InstallApplicationCommand.Command.Options](installapplicationcommand/command-data.dictionary/options-data.dictionary.md)
  A dictionary that contains the app installation options.

## Properties

- `Attributes` (InstallApplicationCommand.Command.Attributes): A dictionary that contains the initial attributes of the app, if you choose to provide it. Available: iOS 7+ | iPadOS 7+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `ChangeManagementState` (string): The change management state. This value doesn’t work with the user enrollment feature introduced in iOS 13, or any type of account driven enrollment. The only possible value is: - `Managed`: Take management of the app if the user installed it already and `InstallAsManaged` is `true`. Available: iOS 9+ | iPadOS 9+ | macOS 11+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `Configuration` (InstallApplicationCommand.Command.Configuration): A dictionary that contains the initial configuration of the app, if you choose to provide it. Available: iOS 7+ | iPadOS 7+ | macOS 11+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `Identifier` (string): The app’s bundle identifier. > ❗ **Important**:  For a watchOS app, the identifier needs to be the watch’s bundle identifier, which differs from the main bundle identifier for the iPhone the watch pairs with. Obtain the watch’s bundle identifier for an app with a watch bundle, in the `watchBundleId` key that’s part of the Content Metadata query. For more information on this query, see [`Getting app and book information (Legacy)`](getting-app-and-book-information-legacy.md). Available: iOS 7+ | iPadOS 7+ | macOS 10.9+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `InstallAsManaged` (boolean): If `true`, install the app as a managed app. Otherwise, the system installs the app as unmanaged. If you reinstall a manged app and omit this value or set it to `false`, the app becomes unmanaged. For manifest-based installs, if `true`, the system only considers apps installed in `/Applications` as managed. In macOS 11 through 13, the system requires that the `pkg` only contains a single signed app. Available: macOS 11+
- `iOSApp` (boolean): If `true`, the app is an iOS app that can run on a Mac with Apple silicon in macOS 11 and later. Available: macOS 11+
- `iTunesStoreID` (integer): The app’s iTunes Store identifier.
- `ManagementFlags` (integer): A bitwise OR of the management flags. The possible values are: - `1`: If `InstallAsManaged` is `true`, remove the app upon removal of the MDM profile.
- `4`: Prevent backup of app data.
- `5`: Both `1` and `4`. Available: iOS 5+ | iPadOS 5+ | macOS 11+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `ManifestURL` (string): The URL of the app manifest, which needs to begin with `https:`. The server returns the manifest as a property list that uses the [`ManifestURL`](manifesturl.md) format. Available: iOS 7+ | iPadOS 7+ | macOS 10.9+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `Options` (InstallApplicationCommand.Command.Options): A dictionary that contains the app installation options. Available: iOS 7+ | iPadOS 7+ | macOS 10.9+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installapplicationcommand/command-data.dictionary)*