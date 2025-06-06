# setDelegate(_:queue:)

**Framework**: CallKit  
**Kind**: method

Sets a provider delegate, specifying an optional queue on which to execute delegate methods.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func setDelegate(_ delegate: (any CXProviderDelegate)?, queue: dispatch_queue_t?)
```

## Parameters

- `delegate`: An object conforming to the   protocol.
- `queue`: If  , delegate methods are performed on the main queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxprovider/setdelegate(_:queue:))*