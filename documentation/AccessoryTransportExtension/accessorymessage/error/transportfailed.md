# AccessoryMessage.Error.transportFailed

**Framework**: Accessory Transport Extension  
**Kind**: case

An error indicating the transport failed but may recover.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)

## Declaration

```swift
case transportFailed
```

#### Discussion

The system retries message delivery when you return this error.

## See Also

- [AccessoryMessage.Error.transportUnavailable](accessorymessage/error/transportunavailable.md)
  An error indicating the transport is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/error/transportfailed)*