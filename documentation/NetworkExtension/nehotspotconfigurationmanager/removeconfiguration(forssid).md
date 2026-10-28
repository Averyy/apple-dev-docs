# removeConfiguration(forSSID:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Removes a Wi-Fi configuration, identified by an SSID, that your app previously added.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func removeConfiguration(forSSID SSID: String)
```

```objc
- (void) removeConfigurationForSSID:(NSString *) SSID;
```

## Discussion

Your app can use this method to delete a configuration that it has added, but not a configuration added by another app or by the user.  The user can also delete configured networks through Settings > Wi-Fi.

## Parameters

- `SSID`: A string of 1-32 characters.

## See Also

### Removing configuration
- [func removeConfiguration(forHS20DomainName: String)](./removeconfiguration%28forhs20domainname%29.md)
  Removes a Wi-Fi hotspot configuration, identified by a Hotspot 2.0 domain name, that your app previously added.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfigurationmanager/removeconfiguration(forssid:))*