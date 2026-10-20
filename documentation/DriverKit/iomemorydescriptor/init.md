# init

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes the memory descriptor object.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual bool init();
```

#### Return Value

[`true`](../../Swift/true.md) if initialization was successful, or [`false`](../../Swift/false.md) if it was unsuccessful.

#### Discussion

Don’t call this method directly. To allocate a memory buffer for your driver, call the [`Create`](../iobuffermemorydescriptor/create.md) method of [`IOBufferMemoryDescriptor`](../iobuffermemorydescriptor.md).

## See Also

### Configuring the Buffer
- [free](./free.md)
  Performs any final cleanup for the memory descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorydescriptor/init)*