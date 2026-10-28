# fontName

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The font face name.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fontName: String { get }
```

```objc
@property (nonatomic, strong, readonly) NSString * fontName;
```

## Discussion

The font name is a name such as `HelveticaBold` that incorporates the family name and any specific style information for the font. The value in this property is intended for an application’s internal usage only and should not be displayed.

## See Also

### Getting Font Name Attributes
- [var familyName: String](./familyname.md)
  The font family name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/fontname)*