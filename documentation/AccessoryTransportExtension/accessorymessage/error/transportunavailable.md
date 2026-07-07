# AccessoryMessage.Error.transportUnavailable

**Framework**: Accessory Transport Extension  
**Kind**: case

An error indicating the transport is unavailable.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
case transportUnavailable
```

#### Discussion

The system attempts delivery on a different transport if available when you return this error.

## See Also

- [AccessoryMessage.Error.transportFailed](accessorymessage/error/transportfailed.md)
  An error indicating the transport failed but may recover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/error/transportunavailable)*