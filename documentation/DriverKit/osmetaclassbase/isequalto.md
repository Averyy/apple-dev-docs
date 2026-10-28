# isEqualTo

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Compares two objects

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual bool isEqualTo(const OSMetaClassBase *anObject) const;
```

## Discussion

The default implementation only compares the object pointers, however many container classes override to provide deeper comparison.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osmetaclassbase/isequalto)*