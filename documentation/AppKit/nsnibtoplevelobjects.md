# NSNibTopLevelObjects

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

An `NSMutableArray` object that, if present, is populated with the top-level objects of the newly instantiated nib.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern NSString * NSNibTopLevelObjects;
```

#### Discussion

Because you must allocate this array, you are responsible for its disposal. This key is optional.

## See Also

### Constants
- [NSNibOwner](./nsnibowner.md)
  The external object that is responsible for the instantiated nib.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsnibtoplevelobjects)*