# NSModelPathKey

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

Dictionary key for the managed object model path (an instance of `NSURL`) extracted from an external record file.

**Availability**:
- macOS 10.6+ - Deprecated in 10.13

> **Deprecated**: Spotlight integration is deprecated. Use CoreSpotlight integration instead.

## Declaration

```swift
let NSModelPathKey: String
```

```c
extern NSString * const NSModelPathKey;
```

## Discussion

This is resolved to the `model.mom` path contained in the external record file directory.

## See Also

### Constants
- [let NSEntityNameInPathKey: String](./nsentitynameinpathkey.md)
  Dictionary key for the entity name extracted from an external record file.
- [let NSStoreUUIDInPathKey: String](./nsstoreuuidinpathkey.md)
  Dictionary key for the store UUID extracted from an external record file.
- [let NSStorePathKey: String](./nsstorepathkey.md)
  Dictionary key for the store path (an instance of `NSURL`) extracted from an external record file.
- [let NSObjectURIKey: String](./nsobjecturikey.md)
  Dictionary key for the object URI extracted from an external record file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmodelpathkey)*