# mccAndMNCs

**Framework**: Network Extension  
**Kind**: property

An array of Mobile Country Code (MCC) and Mobile Network Code  (MNC) pairs used for Wi-Fi Hotspot 2.0 negotiation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var mccAndMNCs: [String] { get set }
```

#### Discussion

Each `MCCAndMNCs` string must contain exactly six integers.

## See Also

- [var domainName: String](nehotspoths20settings/domainname.md)
  The domain name of a Hotspot 2.0 Wi-Fi Network.
- [var isRoamingEnabled: Bool](nehotspoths20settings/isroamingenabled.md)
  A Boolean value indicating whether or not roaming is enabled on a Hotspot 2.0 Wi-Fi network.
- [var naiRealmNames: [String]](nehotspoths20settings/nairealmnames.md)
  An array of Network Access Identifier (NAI) realm name strings used for Wi-Fi Hotspot 2.0 negotiation.
- [var roamingConsortiumOIs: [String]](nehotspoths20settings/roamingconsortiumois.md)
  An array of Roaming Consortium Organization (RCO) identifiers used for Wi-Fi Hotspot 2.0 negotiation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspoths20settings/mccandmncs)*