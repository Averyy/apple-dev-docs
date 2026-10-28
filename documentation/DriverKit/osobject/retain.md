# retain

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Retains the OSObject instance

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual void retain() const;
```

## Discussion

Increases the retain count of the instance by one.

## See Also

### Managing the Object Lifecycle
- [init](./init.md)
- [release](./release.md)
  Releases the OSObject instance
- [free](./free.md)
- [OSObjectPtr](../osobjectptr.md)
- [OSObjectRef](../osobjectref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osobject/retain)*