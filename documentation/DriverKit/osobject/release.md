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

- [init](osobject/init.md)
- [retain](osobject/retain.md)
  Retains the OSObject instance
- [free](osobject/free.md)
- [OSObjectPtr](osobjectptr.md)
- [OSObjectRef](osobjectref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osobject/release)*