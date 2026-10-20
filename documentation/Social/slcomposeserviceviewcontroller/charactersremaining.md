# charactersRemaining

**Framework**: Social  
**Kind**: property  
**Role**: Instance Property

The number of characters remaining in a custom character limit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```swift
var charactersRemaining: NSNumber! { get set }
```

*iOS, iPadOS, Mac Catalyst*

```objc
@property (nonatomic, strong) NSNumber * charactersRemaining;
```

*macOS*

```objc
@property (atomic, strong) NSNumber * charactersRemaining;
```

#### Discussion

Set this property to a non-`nil` value when you want to make the character count view appear in the compose view (changing the value redraws the character count view). The default value of this property is `nil`.

## See Also

### Validating Content
- [func isContentValid() -> Bool](./iscontentvalid%28%29.md)
  A Boolean value that indicates whether the current content and attachments are valid.
- [func validateContent()](./validatecontent%28%29.md)
  Performs validation of the current content and updates the state of the Post button, if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/charactersremaining)*