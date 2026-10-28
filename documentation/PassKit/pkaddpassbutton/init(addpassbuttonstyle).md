# init(addPassButtonStyle:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Initializes a new Add Pass button.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(addPassButtonStyle style: PKAddPassButtonStyle)
```

```objc
- (instancetype) initWithAddPassButtonStyle:(PKAddPassButtonStyle) style;
```

## Return Value

Returns a [`PKAddPassButton`](../pkaddpassbutton.md) instance with the specified style.

## Parameters

- `style`: The button’s style. For a complete list of styles, see [`PKAddPassButtonStyle`](../pkaddpassbuttonstyle.md).

## See Also

### Creating add pass buttons
- [+ addPassButtonWithStyle:](./addpassbuttonwithstyle_.md)
  Returns a button that prompts the user to add a pass to Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassbutton/init(addpassbuttonstyle:))*