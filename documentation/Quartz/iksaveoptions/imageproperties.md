# imageProperties

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

Returns a dictionary of updated image properties that reflects the user’s selection.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var imageProperties: [AnyHashable : Any]! { get }
```

```objc
@property (nonatomic, readonly) NSDictionary * imageProperties;
```

## See Also

### Retrieving User Responses
- [var imageUTType: String!](./imageuttype.md)
  Returns the uniform type identifier that reflects the user’s selection.
- [var userSelection: [AnyHashable : Any]!](./userselection.md)
  Returns a dictionary that contains the save options selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/iksaveoptions/imageproperties)*