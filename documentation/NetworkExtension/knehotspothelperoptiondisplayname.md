# kNEHotspotHelperOptionDisplayName

**Framework**: Network Extension  
**Kind**: var  
**Role**: Global Variable

The string displayed in Wi-Fi Settings for a network handled by the application.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
let kNEHotspotHelperOptionDisplayName: String
```

```c
extern const NSString * kNEHotspotHelperOptionDisplayName;
```

#### Discussion

This key specifies the display name for the application, if an alternate name is desired. If this property is not specified, the application’s name is used.

This name appears in Settings -> Wi-Fi underneath the Wi-Fi network name if the helper indicated that it was able to handle the network.

## See Also

### Registering a hotspot helper
- [class func register(options: [String : NSObject]?, queue: dispatch_queue_t, handler: NEHotspotHelperHandler) -> Bool](./nehotspothelper/register%28options,queue,handler%29.md)
  Register the application as a Hotspot Helper.
- [typealias NEHotspotHelperHandler](./nehotspothelperhandler.md)
  The type definition for the Hotspot Helper’s command handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/knehotspothelperoptiondisplayname)*