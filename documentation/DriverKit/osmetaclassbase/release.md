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

- [retain](osmetaclassbase/retain.md)
  Retains the OSObject instance


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osmetaclassbase/release)*