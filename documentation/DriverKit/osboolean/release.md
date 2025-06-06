# release

**Framework**: DriverKit  
**Kind**: method

Releases the OSObject instance

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void release() const;
```

#### Discussion

Decreases the retain count of the instance by one. If the count is then zero, frees the object.

## See Also

- [free](osboolean/free.md)
- [retain](osboolean/retain.md)
  Retains the OSObject instance
- [OSBooleanPtr](osbooleanptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osboolean/release)*