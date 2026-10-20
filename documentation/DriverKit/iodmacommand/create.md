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
static kern_return_t Create(IOService *device, uint64_t options, const IODMACommandSpecification *specification, IODMACommand **command);
```

## See Also

### Creating a DMA Command
- [init](./init.md)
- [free](./free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodmacommand/create)*