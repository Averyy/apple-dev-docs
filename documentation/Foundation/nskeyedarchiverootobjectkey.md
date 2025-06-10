# NSKeyedArchiveRootObjectKey

**Framework**: Foundation  
**Kind**: var

Archives created using the class method [`archivedData(withRootObject:)`](nskeyedarchiver/archiveddata(withrootobject:).md) use this key for the root object in the hierarchy of encoded objects. The [`NSKeyedUnarchiver`](nskeyedunarchiver.md) class method [`unarchiveObject(with:)`](nskeyedunarchiver/unarchiveobject(with:).md) looks for this root key as well.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiverootobjectkey)*