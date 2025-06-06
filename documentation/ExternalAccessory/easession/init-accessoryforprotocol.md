# init(accessory:forProtocol:)

**Framework**: External Accessory  
**Kind**: init

Initializes the session for the specified accessory and protocol.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init?(accessory: EAAccessory, forProtocol protocolString: String)
```

#### Return Value

The initialized session object. This method may return `nil` if the accessory does not recognize the specified protocol or there was an error communicating with the accessory.

#### Discussion

There can be only one session object at a time for a given accessory and protocol combination.

## Parameters

- `accessory`: The accessory with which you want to communicate. You can get a list of accessory objects from the   object.
- `protocolString`: The protocol to use when communicating with the accessory. This protocol must be one that the accessory understands. All communications with the accessory are expected to use this protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/easession/init(accessory:forprotocol:))*