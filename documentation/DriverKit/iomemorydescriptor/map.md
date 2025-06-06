# Map

**Framework**: DriverKit  
**Kind**: method

Maps memory internally.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t Map(uint64_t options, uint64_t address, uint64_t length, uint64_t alignment, uint64_t * returnAddress, uint64_t * returnLength);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorydescriptor/map)*