# allowsKeyedCoding

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver supports keyed coding of objects.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var allowsKeyedCoding: Bool { get }
```

```objc
@property (readonly) BOOL allowsKeyedCoding;
```

## Discussion

[`false`](../../Swift/false.md) by default. Concrete subclasses that support keyed coding, such as `NSKeyedArchiver`, need to override this property to return [`true`](../../Swift/true.md).

## See Also

### Related Documentation
- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
### Inspecting a Coder
- [func containsValue(forKey: String) -> Bool](./containsvalue%28forkey%29.md)
  Returns a Boolean value that indicates whether an encoded value is available for a string.
- [var decodingFailurePolicy: NSCoder.DecodingFailurePolicy](./decodingfailurepolicy-swift.property.md)
  The action the coder should take when decoding fails.
- [NSCoder.DecodingFailurePolicy](./decodingfailurepolicy-swift.enum.md)
  Policies describing the action the coder should take when encountering decode failures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/allowskeyedcoding)*