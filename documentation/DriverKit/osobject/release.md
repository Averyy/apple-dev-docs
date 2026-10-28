# release

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Releases the OSObject instance

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual void release() const;
```

## Discussion

Decreases the retain count of the instance by one. If the count is then zero, frees the object.

## See Also

### Managing the Object Lifecycle
- [init](./init.md)
- [retain](./retain.md)
  Retains the OSObject instance
- [free](./free.md)
- [OSObjectPtr](../osobjectptr.md)
- [OSObjectRef](../osobjectref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osobject/release)*