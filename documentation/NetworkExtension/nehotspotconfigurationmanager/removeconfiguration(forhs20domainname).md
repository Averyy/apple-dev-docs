# removeConfiguration(forHS20DomainName:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Removes a Wi-Fi hotspot configuration, identified by a Hotspot 2.0 domain name, that your app previously added.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func removeConfiguration(forHS20DomainName domainName: String)
```

```objc
- (void) removeConfigurationForHS20DomainName:(NSString *) domainName;
```

## Discussion

Your app can use this method to delete a configuration that it has added, but not a configuration added by another app or by the user.  The user can also delete configured networks through Settings > Wi-Fi.

## Parameters

- `domainName`: The domain name of the HS 2.0 Wi-Fi network.

## See Also

### Removing configuration
- [func removeConfiguration(forSSID: String)](./removeconfiguration%28forssid%29.md)
  Removes a Wi-Fi configuration, identified by an SSID, that your app previously added.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfigurationmanager/removeconfiguration(forhs20domainname:))*