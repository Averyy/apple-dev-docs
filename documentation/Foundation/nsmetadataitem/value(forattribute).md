# value(forAttribute:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s metadata attribute name specified by a given key.

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
func value(forAttribute key: String) -> Any?
```

```objc
- (id) valueForAttribute:(NSString *) key;
```

## Return Value

The receiver’s metadata attribute name specified by `key`.

## Parameters

- `key`: The name of a metadata attribute. See the “Constants” section for a list of possible keys.

## See Also

### Getting Item Attributes
- [var attributes: [String]](./attributes.md)
  An array containing the attribute keys for the metadata item’s values.
- [func values(forAttributes: [String]) -> [String : Any]?](./values%28forattributes%29.md)
  Returns a dictionary containing the key-value pairs for the attribute names specified by a given array of keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataitem/value(forattribute:))*