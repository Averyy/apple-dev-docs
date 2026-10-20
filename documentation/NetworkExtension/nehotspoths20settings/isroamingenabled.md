# isRoamingEnabled

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether or not roaming is enabled on a Hotspot 2.0 Wi-Fi network.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isRoamingEnabled: Bool { get set }
```

```objc
@property (getter=isRoamingEnabled) BOOL roamingEnabled;
```

#### Discussion

If `true`, the HS 2.0 Wi-Fi- network can connect to networks of roaming service providers. The default value is `false`.

## See Also

### Accessing Hotspot 2.0 properties
- [var domainName: String](./domainname.md)
  The domain name of a Hotspot 2.0 Wi-Fi Network.
- [var mccAndMNCs: [String]](./mccandmncs.md)
  An array of Mobile Country Code (MCC) and Mobile Network Code  (MNC) pairs used for Wi-Fi Hotspot 2.0 negotiation.
- [var naiRealmNames: [String]](./nairealmnames.md)
  An array of Network Access Identifier (NAI) realm name strings used for Wi-Fi Hotspot 2.0 negotiation.
- [var roamingConsortiumOIs: [String]](./roamingconsortiumois.md)
  An array of Roaming Consortium Organization (RCO) identifiers used for Wi-Fi Hotspot 2.0 negotiation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspoths20settings/isroamingenabled)*