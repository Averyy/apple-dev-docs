# roamingConsortiumOIs

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An array of Roaming Consortium Organization (RCO) identifiers used for Wi-Fi Hotspot 2.0 negotiation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var roamingConsortiumOIs: [String] { get set }
```

```objc
@property (copy) NSArray<NSString *> * roamingConsortiumOIs;
```

## See Also

### Accessing Hotspot 2.0 properties
- [var domainName: String](./domainname.md)
  The domain name of a Hotspot 2.0 Wi-Fi Network.
- [var isRoamingEnabled: Bool](./isroamingenabled.md)
  A Boolean value indicating whether or not roaming is enabled on a Hotspot 2.0 Wi-Fi network.
- [var mccAndMNCs: [String]](./mccandmncs.md)
  An array of Mobile Country Code (MCC) and Mobile Network Code  (MNC) pairs used for Wi-Fi Hotspot 2.0 negotiation.
- [var naiRealmNames: [String]](./nairealmnames.md)
  An array of Network Access Identifier (NAI) realm name strings used for Wi-Fi Hotspot 2.0 negotiation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspoths20settings/roamingconsortiumois)*