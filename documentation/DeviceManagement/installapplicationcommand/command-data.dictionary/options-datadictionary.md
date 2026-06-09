# InstallApplicationCommand.Command.Options

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains the app installation options.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.9+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object InstallApplicationCommand.Command.Options
```

## Properties

- `PurchaseMethod` (integer): The app’s purchase type, which must be one of the following values: - `0`: Free apps and Legacy Volume Purchase Program (VPP) with a redemption code. This option is only available in iOS.
- `1`: Volume Purchase Program (VPP) app assignment. Set this value to `1` to install first-party apps without user login to the iTunes Store, such as Mail or Safari, or to install an iOS app with user enrollment.

## See Also

- [object InstallApplicationCommand.Command.Attributes](installapplicationcommand/command-data.dictionary/attributes-data.dictionary.md)
  A dictionary that contains the initial attributes of the app.
- [object InstallApplicationCommand.Command.Configuration](installapplicationcommand/command-data.dictionary/configuration-data.dictionary.md)
  A dictionary that contains the configuration to install an enterprise app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installapplicationcommand/command-data.dictionary/options-data.dictionary)*