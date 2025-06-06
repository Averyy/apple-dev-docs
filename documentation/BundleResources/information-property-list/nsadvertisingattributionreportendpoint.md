# NSAdvertisingAttributionReportEndpoint

**Framework**: Bundleresources  
**Kind**: typealias

The URL where Private Click Measurement and SKAdNetwork send attribution information.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- visionOS 1.0+

#### Discussion

This key is a string that contains a valid URL containing your domain name. Provide a string in the format `“https://example.com”`, where you replace `example` with your domain name. Include this key in your app for the following two uses:

- To specify where the system sends event attribution data it receives from launched websites that support Private Click Measurement (PCM). PCM won’t work if your app doesn’t include this key.
- To specify where the system sends a copy of the winning install-validation postback to the advertised app’s developer, for apps that are advertised using the [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) API. Including this key is optional.

The system sends postbacks to a well-known URL it generates using the domain name you provide in the key. To receive the postbacks, configure your server to receive HTTPS POST messages at the following endpoints:

- To receive PCM event attribution data: `https://example.com/.well-known/private-click-measurement/report-attribution/`
- To receive SKAdNetwork install-validation postbacks: `https://example.com/.well-known/skadnetwork/report-attribution/`

Replace `example.com` with your domain name. The system uses only the registrable part of the domain name, and ignores any subdomains.

For more information about PCM and setting up a server to receive event attribution data, see [`Introducing Private Click Measurement`](https://developer.apple.comhttps://webkit.org/blog/11529/introducing-private-click-measurement-pcm/). For more information about configuring an advertised app to enable its developer to receive postbacks, see [`Configuring an advertised app`](https://developer.apple.com/documentation/StoreKit/configuring-an-advertised-app) and [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork).

> **Note**:  Mac apps built with Mac Catalyst don’t support PCM.

## See Also

- [NSAppTransportSecurity](information-property-list/nsapptransportsecurity.md)
  A description of changes made to the default security for HTTP connections.
- [NSBonjourServices](information-property-list/nsbonjourservices.md)
  Bonjour service types browsed by the app.
- [CKSharingSupported](information-property-list/cksharingsupported.md)
  A Boolean value that indicates your app supports CloudKit Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsadvertisingattributionreportendpoint)*