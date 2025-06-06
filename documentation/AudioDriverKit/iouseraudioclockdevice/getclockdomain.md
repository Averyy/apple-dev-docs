# GetClockDomain

**Framework**: AudioDriverKit  
**Kind**: method

Gets the clock domain value of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
uint32_t GetClockDomain();
```

#### Return Value

The clock domain value of the clock device.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [SetClockDomain](iouseraudioclockdevice/setclockdomain.md)
  Sets the clock domain value of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getclockdomain)*