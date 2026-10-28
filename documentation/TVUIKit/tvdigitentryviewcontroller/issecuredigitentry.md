# isSecureDigitEntry

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether an entered digit is immediately obscured.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var isSecureDigitEntry: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isSecureDigitEntry) BOOL secureDigitEntry;
```

## Discussion

The defualt value is `NO`.

## See Also

### Configuring the Digit Entry View
- [var numberOfDigits: Int](./numberofdigits.md)
  The number of required digits.
- [var titleText: String?](./titletext.md)
  The title of the digit entry view.
- [var promptText: String?](./prompttext.md)
  A prompt that displays any additional required information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller/issecuredigitentry)*