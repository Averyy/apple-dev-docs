# userSelection

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

Returns a dictionary that contains the save options selected by the user.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var userSelection: [AnyHashable : Any]! { get }
```

```objc
@property (nonatomic, readonly) NSDictionary * userSelection;
```

## See Also

### Retrieving User Responses
- [var imageProperties: [AnyHashable : Any]!](./imageproperties.md)
  Returns a dictionary of updated image properties that reflects the user’s selection.
- [var imageUTType: String!](./imageuttype.md)
  Returns the uniform type identifier that reflects the user’s selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/iksaveoptions/userselection)*