# AccessoryMessage.Result

**Framework**: Accessory Transport Extension  
**Kind**: enum

An enumeration of results for message transmission.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)

## Declaration

```swift
enum Result
```

#### Overview

Pass values of this type to completion handlers in [`AccessoryTransportSession.EventHandler`](accessorytransportsession/eventhandler.md) and [`AccessorySecuritySession.EventHandler`](accessorysecuritysession/eventhandler.md) methods to indicate transmission outcomes.

## Topics

### Identifying result types
- [AccessoryMessage.Result.success](accessorymessage/result/success.md)
  A result indicating successful message transmission to the accessory.
- [case failure(AccessoryMessage.Error)](accessorymessage/result/failure(_:).md)
  A result indicating message transmission failed.

## See Also

- [AccessoryMessage.Error](accessorymessage/error.md)
  An enumeration of errors that can occur during message transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/result)*