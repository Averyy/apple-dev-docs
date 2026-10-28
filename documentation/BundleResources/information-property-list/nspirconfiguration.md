# NSPIRConfiguration

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

The URLs used for a PIR server to support a URL filter or Live Caller ID lookup app.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- macOS 27.2+

## Details

- **Name**: `NSPIRConfiguration`
- **Type**: dictionary

## Discussion

Use this key to declare how your extension uses a Private Information Retrieval (PIR) server. You use a different information property list depending on the app type:

- For Live Caller ID Lookup, add this key to the app extension’s information property list.
- For a URL Filter, add this key to app’s information property list, rather than the URL Filter app extension.

See the [PIRService documentation](https://swiftpackageindex.com/apple/pir-service-example/main/documentation/pirservice) for more information on configuring your PIR server to work with URL filters and Live Caller ID lookup.

An `NSPIRConfiguration` dictionary may look like this example:

```xml
<key>NSPIRConfiguration</key>
<dict>
    <key>PIRServerURL</key>
    <string>https://pir.example.com</string>
    <key>PrivacyPassIssuerURL</key>
    <string>https://issuer.example.com</string>
</dict>
```

## Topics

### Configuring URLs
- [PIRServerURL](./nspirconfiguration/pirserverurl.md)
  The URL of the PIR server.
- [PrivacyPassIssuerURL](./nspirconfiguration/privacypassissuerurl.md)
  The URL of the Privacy Pass issuer.

## See Also

### Network
- [NSApplicationServices](./nsapplicationservices.md)
  A list of service providers and the devices that they support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nspirconfiguration)*