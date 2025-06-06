# getHIDDescriptorInfo

**Framework**: HIDDriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
kern_return_t getHIDDescriptorInfo(uint8_t type, const IOUSBHostHIDDescriptorInfo * * info, uint8_t * index);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## See Also

- [initPipes](iouserusbhosthiddevice/initpipes.md)
- [CompleteZLP](iouserusbhosthiddevice/completezlp.md)
- [copyStringAtIndex](iouserusbhosthiddevice/copystringatindex.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/gethiddescriptorinfo)*