# AccessoryMessage.Result

**Framework**: Accessory Transport Extension  
**Kind**: enum  
**Role**: Enumeration

An enumeration of results for message transmission.

**Availability**:
- iOS 26.5+

## Declaration

```swift
enum Result
```

## Overview

Pass values of this type to completion handlers in [`AccessoryTransportSession.EventHandler`](../accessorytransportsession/eventhandler.md) and [`AccessorySecuritySession.EventHandler`](../accessorysecuritysession/eventhandler.md) methods to indicate transmission outcomes.

## Topics

### Identifying result types
- [AccessoryMessage.Result.success](./result/success.md)
  A result indicating successful message transmission to the accessory.
- [case failure(AccessoryMessage.Error)](./result/failure%28_%29.md)
  A result indicating message transmission failed.

## See Also

### Assessing outcomes
- [AccessoryMessage.Error](./error.md)
  An enumeration of errors that can occur during message transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/result)*