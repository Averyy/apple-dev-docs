# wantedAttributes

**Framework**: FSKit  
**Kind**: property

The attributes requested by the request.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var wantedAttributes: FSItem.Attribute { get set }
```

#### Discussion

This property is a bit field in Objective-C and an [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) in Swift.

## See Also

- [func isAttributeWanted(FSItem.Attribute) -> Bool](fsitem/getattributesrequest/isattributewanted(_:).md)
  A method that indicates whether the request wants given attribute.
- [FSItem.Attribute](fsitem/attribute.md)
  A value that indicates a set of item attributes to get or set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/getattributesrequest/wantedattributes)*