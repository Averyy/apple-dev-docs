# wantedAttributes

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The attributes requested by the request.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var wantedAttributes: FSItem.Attribute { get set }
```

```objc
@property (nonatomic) FSItemAttribute wantedAttributes;
```

## Discussion

This property is a bit field in Objective-C and an [`OptionSet`](../../../Swift/optionset.md) in Swift.

## See Also

### Inspecting requested attributes
- [func isAttributeWanted(FSItem.Attribute) -> Bool](./isattributewanted%28_%29.md)
  A method that indicates whether the request wants given attribute.
- [FSItem.Attribute](../attribute.md)
  A value that indicates a set of item attributes to get or set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/getattributesrequest/wantedattributes)*