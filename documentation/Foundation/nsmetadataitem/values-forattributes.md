# values(forAttributes:)

**Framework**: Foundation  
**Kind**: method

Returns a dictionary containing the key-value pairs for the attribute names specified by a given array of keys.

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
func values(forAttributes keys: [String]) -> [String : Any]?
```

#### Return Value

A dictionary containing the key-value pairs for the attribute names specified by `keys`.

## Parameters

- `keys`: An array containing   objects that specify the names of a metadata attributes. See the “Constants” section for a list of possible keys.

## See Also

- [var attributes: [String]](nsmetadataitem/attributes.md)
  An array containing the attribute keys for the metadata item’s values.
- [func value(forAttribute: String) -> Any?](nsmetadataitem/value(forattribute:).md)
  Returns the receiver’s metadata attribute name specified by a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataitem/values(forattributes:))*