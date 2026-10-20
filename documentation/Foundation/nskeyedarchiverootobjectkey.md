# NSKeyedArchiveRootObjectKey

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

Archives created using the class method [`archivedData(withRootObject:)`](./nskeyedarchiver/archiveddata%28withrootobject%29.md) use this key for the root object in the hierarchy of encoded objects. The [`NSKeyedUnarchiver`](./nskeyedunarchiver.md) class method [`unarchiveObject(with:)`](./nskeyedunarchiver/unarchiveobject%28with%29.md) looks for this root key as well.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSKeyedArchiveRootObjectKey: String
```

```c
extern NSString * const NSKeyedArchiveRootObjectKey;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiverootobjectkey)*