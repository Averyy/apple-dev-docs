# init

**Framework**: DriverKit  
**Kind**: method

Initializes the memory descriptor object.

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

[`true`](https://developer.apple.com/documentation/swift/true) if initialization was successful, or [`false`](https://developer.apple.com/documentation/swift/false) if it was unsuccessful.

#### Discussion

Don’t call this method directly. To allocate a memory buffer for your driver, call the [`Create`](iobuffermemorydescriptor/create.md) method of [`IOBufferMemoryDescriptor`](iobuffermemorydescriptor.md).

## See Also

- [free](iomemorydescriptor/free.md)
  Performs any final cleanup for the memory descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorydescriptor/init)*