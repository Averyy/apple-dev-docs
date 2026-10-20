# classNameEncoded(forTrueClassName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the name of the class used to archive instances of the class with a given true name.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedArchiver instead

## Declaration

```swift
func classNameEncoded(forTrueClassName trueName: String) -> String?
```

```objc
- (NSString *) classNameEncodedForTrueClassName:(NSString *) trueName;
```

#### Return Value

The name of the class used to archive instances of the class `trueName`.

## Parameters

- `trueName`: The real name of an encoded class.

## See Also

### Substituting classes or objects
- [func encodeClassName(String, intoClassName: String)](./encodeclassname%28_,intoclassname%29.md)
  Encodes a substitute name for the class with a given true name.
- [func replace(Any, with: Any)](./replace%28_,with%29.md)
  Causes the receiver to treat subsequent requests to encode a given object as though they were requests to encode another given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver/classnameencoded(fortrueclassname:))*