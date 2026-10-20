# Configuring a source app

**Framework**: StoreKit  
**Role**: Article

Set up a source app to participate in ad campaigns.

#### Overview

A *source app* is an app that participates in ad campaigns by displaying ads that an ad network signs. To participate in install validation, the source app needs to include ad network IDs in its `Info.plist` file. Ad networks are responsible for publishing or providing their ad network IDs to developers.

Only ads from ad networks that have an entry in the app’s `Info.plist` file are eligible for install validation. To work with multiple ad networks, include each of the ad network IDs in the source app’s `Info.plist` file, as follows:

1. Select `Info.plist` in the Project navigator in Xcode.
2. Click the Add button (+) beside a key in the property list editor and press Return.
3. Type the key name [`SKAdNetworkItems`](../BundleResources/information-property-list/skadnetworkitems.md).
4. Choose Array from the pop-up menu in the Type column.

Create an array that contains one dictionary for each allowed ad network, using the single key [`SKAdNetworkIdentifier`](../BundleResources/information-property-list/skadnetworkitems/skadnetworkidentifier.md). The string value for the key is the ad network ID.

> ❗ **Important**:  Lowercase the ad network ID string; otherwise, the system doesn’t recognize it as valid.

The following example shows an array with two dictionaries that represent the example ad network IDs `example100.skadnetwork` and `example200.skadnetwork`:

```xml
<array>
    <dict>
        <key>SKAdNetworkIdentifier</key>
        <string>example100.skadnetwork</string>
    </dict>
    <dict>   
         <key>SKAdNetworkIdentifier</key>
         <string>example200.skadnetwork</string>
    </dict>
</array>
```

For more information about property lists, see [Edit property lists](https://help.apple.com/xcode/mac/current/#/dev3f399a2a6).

## See Also

### Registering ad networks and configuring apps
- [Registering an ad network](./registering-an-ad-network.md)
  Use the install-validation APIs for your ad campaigns after registering your ad network with Apple.
- [Configuring an advertised app](./configuring-an-advertised-app.md)
  Prepare an advertised app to participate in ad campaigns.
- [SKAdNetworkItems](../BundleResources/information-property-list/skadnetworkitems.md)
  An array of dictionaries containing a list of ad network IDs.
- [NSAdvertisingAttributionReportEndpoint](../BundleResources/information-property-list/nsadvertisingattributionreportendpoint.md)
  The URL where Private Click Measurement and SKAdNetwork send attribution information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/configuring-a-source-app)*