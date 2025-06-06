# isEqualTo

**Framework**: DriverKit  
**Kind**: method

Compares two objects

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool isEqualTo(const OSMetaClassBase * anObject) const;
```

#### Discussion

The default implementation only compares the object pointers, however many container classes override to provide deeper comparison.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osmetaclassbase/isequalto)*