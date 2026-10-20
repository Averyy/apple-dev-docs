# init(domainName:roamingEnabled:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

Creates a new hotspot configuration of a legacy Hotspot or HS 2.0 Wi-Fi network. with optional roaming enabled.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(domainName: String, roamingEnabled: Bool)
```

```objc
- (instancetype) initWithDomainName:(NSString *) domainName roamingEnabled:(BOOL) roamingEnabled;
```

## Parameters

- `domainName`: The domain name of a Hotspot 2.0 Wi-Fi network. See [`domainName`](./domainname.md).
- `roamingEnabled`: A Boolean value indicating whether roaming is enabled on the network (`true`) or not (`false`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspoths20settings/init(domainname:roamingenabled:))*