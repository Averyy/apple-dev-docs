# consumedAttributes

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The attributes successfully used by the file system.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var consumedAttributes: FSItem.Attribute { get set }
```

```objc
@property (nonatomic) FSItemAttribute consumedAttributes;
```

#### Discussion

This property is a bit field in Objective-C and an [`OptionSet`](../../../Swift/optionset.md) in Swift.

## See Also

### Inspecting used attributes
- [func wasAttributeConsumed(FSItem.Attribute) -> Bool](./wasattributeconsumed%28_%29.md)
  A method that indicates whether the file system used the given attribute.
- [FSItem.Attribute](../attribute.md)
  A value that indicates a set of item attributes to get or set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/setattributesrequest/consumedattributes)*