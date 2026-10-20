# charactersIgnoringModifiers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A string that represents the text value of the key without modifier keys.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- tvOS 13.4+
- visionOS 1.0+

## Declaration

```swift
var charactersIgnoringModifiers: String { get }
```

```objc
@property (nonatomic, readonly) NSString * charactersIgnoringModifiers;
```

## Mentions

- [Handling key presses made on a physical keyboard](../handling-key-presses-made-on-a-physical-keyboard.md)

#### Discussion

For Latin-based languages, always expect a lowercase property value. If the user is pressing only a modifier key, the property value is an empty string.

To check for special keys, compare [`charactersIgnoringModifiers`](./charactersignoringmodifiers.md) to constants listed in [Input strings for special keys](../input-strings-for-special-keys.md).

## See Also

### Getting key characters
- [var characters: String](./characters.md)
  A string that represents the text value of the key combined with any active modifier keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikey/charactersignoringmodifiers)*