# Displaying Apple Pay Buttons Using JavaScript

**Framework**: Apple Pay on the Web

Load and configure the JavaScript Apple Pay button.

#### Overview

The JavaScript Apple Pay button provides a variety of Apple Pay button types that you can use on your website to initiate a transaction. You can specify the Apple Pay button style, type, and localization using attributes. Use CSS to set other properties, such as the size and corner radius.

Use the following code to load the button script into your webpage from the content delivery network:

```javascript
<script src="https://applepay.cdn-apple.com/jsapi/1.latest/apple-pay-sdk.js"></script>
```

##### Display the Button

Add an `apple-pay-button` element to your webpage to display the button. Set the style, type, and locale when you add the button. The following code adds a black Buy with Apple Pay button localized to Greek, using the default size and corner radius:

```javascript
<apple-pay-button buttonstyle="black" type="buy" locale="el-GR"></apple-pay-button>
```

Use CSS to customize the size and other attributes. The following example adds the same Greek button with a height of `40` pixels, a width of `140` pixels, and a corner radius of `5` pixels. The height includes the top and bottom padding.

```javascript
<style>
apple-pay-button {
  --apple-pay-button-width: 140px;
  --apple-pay-button-height: 30px;
  --apple-pay-button-border-radius: 5px;
  --apple-pay-button-padding: 5px 0px;
}
</style>
<apple-pay-button buttonstyle="black" type="buy" locale="el-GR"></apple-pay-button>
```

The CSS properties for the button are:

The minimum value for the width of a plain Apple Pay button is `100` pixels.

The minimum value for the width of all other Apple Pay buttons is `140` pixels.

The button renders at the minimum width when the specified value is less than the minimum.

The default and minimum value for the height is `30` pixels.

The button renders at the minimum height when the specified value is less than the minimum.

The default value is `4` pixels.

The default value is `0` pixels.

For design guidance, see [`Human Interface Guidelines > Apple Pay > Buttons and Marks`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/buttons-and-marks/).

## See Also

- [ApplePayButton](applepaybutton.md)
  An object that displays a button either to trigger payments through Apple Pay or to prompt the user to set up a card.
- [Displaying Apple Pay Buttons Using CSS](displaying-apple-pay-buttons-using-css.md)
  Use CSS templates to display Apple Pay buttons in Safari.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/displaying-apple-pay-buttons-using-javascript)*