# characters

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A string that represents the text value of the key combined with any active modifier keys.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- tvOS 13.4+
- visionOS 1.0+

## Declaration

```swift
var characters: String { get }
```

```objc
@property (nonatomic, readonly) NSString * characters;
```

#### Discussion

When the user holds one or more modifier keys, this property contains the modified characters according to the rules of the particular modifier keys. For example, if the user holds Shift while pressing a letter button on a Latin keyboard, this property contains a capital letter.

## See Also

### Getting key characters
- [var charactersIgnoringModifiers: String](./charactersignoringmodifiers.md)
  A string that represents the text value of the key without modifier keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikey/characters)*