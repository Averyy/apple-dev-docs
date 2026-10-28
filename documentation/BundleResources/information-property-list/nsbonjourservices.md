# NSBonjourServices

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

Bonjour service types browsed by the app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Details

- **Name**: `NSBonjourServices` (Bonjour services)
- **Type**: array of string 

## Discussion

The value associated with this key is an array of strings that represent Bonjour service types. Include all service types that your app expects to use. Bonjour service type strings look like `_ipp._tcp`, and `_myservice._udp`, where the first substring identifies the application protocol and the second identifies the transport protocol.

## See Also

### Network
- [NSAdvertisingAttributionReportEndpoint](./nsadvertisingattributionreportendpoint.md)
  The URL where Private Click Measurement and SKAdNetwork send attribution information.
- [NSAppTransportSecurity](./nsapptransportsecurity.md)
  A description of changes made to the default security for HTTP connections.
- [CKSharingSupported](./cksharingsupported.md)
  A Boolean value that indicates your app supports CloudKit Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsbonjourservices)*