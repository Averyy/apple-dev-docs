# SetActive

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
virtual kern_return_t SetActive();
```

#### Return Value

0 on success, negative value in case of failure.

#### Discussion

This function is called to set the IOExtensiblePaniclog object active.

When it is set active, it is picked up and added to the extensible paniclog in case of a panic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioextensiblepaniclog/setactive)*