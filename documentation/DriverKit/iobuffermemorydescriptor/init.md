# init

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes the buffer memory descriptor object.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual bool init();
```

## Return Value

`true` if initialization was successful, or `false` if it was unsuccessful.

## Discussion

Don’t call this method directly. Use the [`Create`](./create.md) method instead.

## See Also

### Creating a Memory Buffer
- [Create](./create.md)
  Creates a new memory buffer descriptor object in the current process space.
- [free](./free.md)
  Performs any final cleanup for the memory buffer descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iobuffermemorydescriptor/init)*