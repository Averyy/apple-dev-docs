# getHIDDescriptorInfo

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit
- macOS

## Declaration

```c
kern_return_t getHIDDescriptorInfo(uint8_t type, const IOUSBHostHIDDescriptorInfo **info, uint8_t *index);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## See Also

### Configuring Private Settings
- [initPipes](./initpipes.md)
- [CompleteZLP](./completezlp.md)
- [copyStringAtIndex](./copystringatindex.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/gethiddescriptorinfo)*