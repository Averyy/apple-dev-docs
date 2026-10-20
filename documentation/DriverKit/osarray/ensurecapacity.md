# ensureCapacity

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Allocates capacity for members in array.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual uint32_t ensureCapacity(uint32_t newCapacity);
```

#### Return Value

New count of capacity for members in array, may return prior capacity on failure.

## Parameters

- `newCapacity`: Count of allocated capacity for members in array.

## See Also

### Inspecting an Array
- [getCount](./getcount.md)
  Returns count of members in array.
- [getCapacity](./getcapacity.md)
  Returns count of currently allocated capacity for members in array.
- [OSArrayGetCount](../osarraygetcount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/ensurecapacity)*