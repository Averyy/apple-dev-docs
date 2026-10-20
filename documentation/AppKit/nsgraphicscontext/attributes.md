# attributes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The attributes used to create this instance.

**Availability**:
- macOS

## Declaration

```swift
var attributes: [NSGraphicsContext.AttributeKey : Any]? { get }
```

```objc
@property (copy, readonly, nullable) NSDictionary<NSString *,id> * attributes;
```

#### Discussion

Screen-based graphics contexts do not store attributes, even if you create them using [`init(attributes:)`](./init%28attributes%29.md).

## See Also

### Getting Information About the Context
- [NSGraphicsContext.AttributeKey](./attributekey.md)
  Constants that specify the dictionary keys for the attributes of the graphics context.
- [NSGraphicsContext.RepresentationFormatName](./representationformatname.md)
  Constants that specify values for the representation format name key in a graphic context’s attributes dictionary.
- [var isFlipped: Bool](./isflipped.md)
  A Boolean value that indicates the graphics context’s flipped state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/attributes)*