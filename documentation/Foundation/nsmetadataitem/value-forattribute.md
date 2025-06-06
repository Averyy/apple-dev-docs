# value(forAttribute:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

The receiver’s metadata attribute name specified by `key`.

## Parameters

- `key`: The name of a metadata attribute. See the “Constants” section for a list of possible keys.

## See Also

- [var attributes: [String]](nsmetadataitem/attributes.md)
  An array containing the attribute keys for the metadata item’s values.
- [func values(forAttributes: [String]) -> [String : Any]?](nsmetadataitem/values(forattributes:).md)
  Returns a dictionary containing the key-value pairs for the attribute names specified by a given array of keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataitem/value(forattribute:))*