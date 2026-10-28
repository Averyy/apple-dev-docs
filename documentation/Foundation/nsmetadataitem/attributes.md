# attributes

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An array containing the attribute keys for the metadata item’s values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var attributes: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * attributes;
```

## Discussion

This property contains an array of attribute keys, representing the values available from this metadata item. For a list of possible keys, see `Attribute Keys`.

## See Also

### Getting Item Attributes
- [func value(forAttribute: String) -> Any?](./value%28forattribute%29.md)
  Returns the receiver’s metadata attribute name specified by a given key.
- [func values(forAttributes: [String]) -> [String : Any]?](./values%28forattributes%29.md)
  Returns a dictionary containing the key-value pairs for the attribute names specified by a given array of keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataitem/attributes)*