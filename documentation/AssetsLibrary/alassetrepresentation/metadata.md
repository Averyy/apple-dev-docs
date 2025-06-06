# metadata()

**Framework**: Assets Library  
**Kind**: method

Returns a dictionary of dictionaries of metadata for the representation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func metadata() -> [AnyHashable : Any]!
```

#### Return Value

A dictionary of dictionaries of metadata for the representation. Returns `nil` if the representation is one that the system cannot interpret.

#### Discussion

The returned dictionary holds the same values that would be returned by [`CGImageSourceCopyPropertiesAtIndex(_:_:_:)`](https://developer.apple.com/documentation/ImageIO/CGImageSourceCopyPropertiesAtIndex(_:_:_:)).

## See Also

- [func uti() -> String!](alassetrepresentation/uti.md)
  Returns the representation’s UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/metadata())*