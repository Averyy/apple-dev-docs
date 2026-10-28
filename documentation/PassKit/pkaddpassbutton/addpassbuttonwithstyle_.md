# addPassButtonWithStyle:

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Returns a button that prompts the user to add a pass to Wallet.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) addPassButtonWithStyle:(PKAddPassButtonStyle) addPassButtonStyle;
```

## Return Value

Returns a [`PKAddPassButton`](../pkaddpassbutton.md) instance with the specified style.

## Parameters

- `addPassButtonStyle`: The button’s style. For a complete list of styles, see [`PKAddPassButtonStyle`](../pkaddpassbuttonstyle.md).

## See Also

### Creating add pass buttons
- [init(addPassButtonStyle: PKAddPassButtonStyle)](./init%28addpassbuttonstyle%29.md)
  Initializes a new Add Pass button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassbutton/addpassbuttonwithstyle:)*