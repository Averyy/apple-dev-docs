# encodeClassName(_:intoClassName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Encodes a substitute name for the class with a given true name.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedArchiver instead

## Declaration

```swift
func encodeClassName(_ trueName: String, intoClassName inArchiveName: String)
```

```objc
- (void) encodeClassName:(NSString *) trueName intoClassName:(NSString *) inArchiveName;
```

#### Discussion

Any subsequently encountered objects of class `trueName` are archived as instances of class `inArchiveName`. It is safest not to invoke this method during the archiving process (that is, within an [`encode(with:)`](../nscoding/encode%28with%29.md) method). Instead, invoke it before [`encodeRootObject(_:)`](./encoderootobject%28_%29.md).

## Parameters

- `trueName`: The real name of a class in the object graph being archived.
- `inArchiveName`: The name of the class to use in the archive in place of `trueName`.

## See Also

### Substituting classes or objects
- [func classNameEncoded(forTrueClassName: String) -> String?](./classnameencoded%28fortrueclassname%29.md)
  Returns the name of the class used to archive instances of the class with a given true name.
- [func replace(Any, with: Any)](./replace%28_,with%29.md)
  Causes the receiver to treat subsequent requests to encode a given object as though they were requests to encode another given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/encodeclassname(_:intoclassname:))*