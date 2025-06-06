# SetEnable

**Framework**: NetworkingDriverKit  
**Kind**: method

Enables or disables the queue.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t SetEnable(bool isEnable);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `isEnable`: If  , prepare the queue to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueue/setenable-76sm5)*