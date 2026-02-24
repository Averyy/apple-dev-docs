# InstalledApplicationListCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get a list of the installed apps on a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object InstalledApplicationListCommand.Command
```

## Properties

- `Identifiers` ([string]): An array of app identifiers. Provide this value to limit the response to only include these apps. This value is available in iOS 7 and later, macOS 10.15 and later, tvOS 10.2 and later, visionOS 1.1 and later, and watchOS 10 and later. > ❗ **Important**:  For a watchOS app, the identifier needs to be the watch’s bundle identifier, which differs from the main bundle identifier for the iPhone to which the watch is paired. Obtain the watch’s bundle identifier for an app with a watch bundle, in the `watchBundleId` key that’s part of the Content Metadata query. For more information on this query, see [`Getting App and Book Information (Legacy)`](getting-app-and-book-information-legacy.md).
- `Items` ([string]): An array of strings that represent keys in [`InstalledApplicationListResponse.InstalledApplicationListItem`](installedapplicationlistresponse/installedapplicationlistitem.md). If present, the response only contains the keys listed here, except `Identifier` is always included. If not present, the response contains all keys. Starting in iOS 26, macOS 26, tvOS 26, watchOS 26, and visionOS 26, if this key isn’t present, the response omits values that are expensive to calculate. > 💡 **Tip**:  Only request the keys that you need, because some key values can take significant time and power to calculate on the device.
- `ManagedAppsOnly` (boolean): If `true`, only get a list of managed apps, excluding ones that Declarative Device Management is managing. This value is available in iOS 7 and later, macOS 10.15 and later, and tvOS 10.2 and later. > **Note**:  If the enrollment type is a user enrollment, the system always considers this key as set to `true` and only returns managed apps, excluding ones that Declarative Device Management is managing.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installedapplicationlistcommand/command-data.dictionary)*