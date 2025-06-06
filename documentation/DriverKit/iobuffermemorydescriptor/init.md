# init

**Framework**: DriverKit  
**Kind**: method

Initializes the buffer memory descriptor object.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool init();
```

#### Return Value

`true` if initialization was successful, or `false` if it was unsuccessful.

#### Discussion

Don’t call this method directly. Use the [`Create`](iobuffermemorydescriptor/create.md) method instead.

## See Also

- [Create](iobuffermemorydescriptor/create.md)
  Creates a new memory buffer descriptor object in the current process space.
- [free](iobuffermemorydescriptor/free.md)
  Performs any final cleanup for the memory buffer descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iobuffermemorydescriptor/init)*