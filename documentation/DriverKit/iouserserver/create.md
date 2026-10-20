# Create

**Framework**: DriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
static kern_return_t Create(const char name[64], uint64_t tag, uint64_t options, OSString *bundleID, IOUserServer **server);
```

## See Also

### Configuring the User Server
- [init](./init.md)
- [free](./free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserserver/create)*