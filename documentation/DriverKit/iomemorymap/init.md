# init

**Framework**: DriverKit  
**Kind**: method

Initializes the memory map object.

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

Don’t call this method directly. To create a memory map object, call the [`CreateMapping`](iomemorydescriptor/createmapping.md) method of [`IOMemoryDescriptor`](iomemorydescriptor.md).

## See Also

- [free](iomemorymap/free.md)
  Performs any final cleanup for the memory map object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorymap/init)*