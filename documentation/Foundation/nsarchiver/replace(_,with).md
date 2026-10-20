# replace(_:with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Causes the receiver to treat subsequent requests to encode a given object as though they were requests to encode another given object.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedArchiver instead

## Declaration

```swift
func replace(_ object: Any, with newObject: Any)
```

```objc
- (void) replaceObject:(id) object withObject:(id) newObject;
```

#### Discussion

Both `object` and `newObject` must be valid objects.

## Parameters

- `object`: An object in the object graph being archived.
- `newObject`: The object with which to replace `object` in the archive.

## See Also

### Substituting classes or objects
- [func classNameEncoded(forTrueClassName: String) -> String?](./classnameencoded%28fortrueclassname%29.md)
  Returns the name of the class used to archive instances of the class with a given true name.
- [func encodeClassName(String, intoClassName: String)](./encodeclassname%28_,intoclassname%29.md)
  Encodes a substitute name for the class with a given true name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/replace(_:with:))*