# SetInactive

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
virtual kern_return_t SetInactive();
```

#### Return Value

True in case of success. False in case of an error.

#### Discussion

This function is called to set the IOExtensiblePaniclog object inactive.

When it is set inactive, this buffer is not picked up in case of a panic


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioextensiblepaniclog/setinactive)*