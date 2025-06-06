# NEHotspotHelperHandler

**Framework**: Network Extension  
**Kind**: typealias

The type definition for the Hotspot Helper’s command handler block.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
typealias NEHotspotHelperHandler = (NEHotspotHelperCommand) -> Void
```

#### Discussion

The Hotspot Helper app provides a block of this type when it invokes the `registerWithOptions:queue:handler:` method.

The block is invoked every time there is a command to be processed.

## See Also

- [class func register(options: [String : NSObject]?, queue: dispatch_queue_t, handler: NEHotspotHelperHandler) -> Bool](nehotspothelper/register(options:queue:handler:).md)
  Register the application as a Hotspot Helper.
- [let kNEHotspotHelperOptionDisplayName: String](knehotspothelperoptiondisplayname.md)
  The string displayed in Wi-Fi Settings for a network handled by the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelperhandler)*