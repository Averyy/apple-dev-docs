# Styling the Apple Pay Button Using CSS

**Framework**: Apple Pay on the Web

Choose a button color and size to suit your webpage.

#### Overview

You can experiment with styling and display of an Apple Pay button using the [`Apple Pay on the Web Demo`](https://developer.apple.comhttps://applepaydemo.apple.com). To support devices running iOS 10 and macOS 10.12, use the CSS template sample code in [`Displaying Apple Pay Buttons Using CSS`](https://developer.apple.com/documentation/apple_pay_on_the_web/displaying_apple_pay_buttons_using_css) to draw the appropriate button.

To display an Apple Pay button set the `-webkit-appearance` CSS property of the element to `-apple-pay-button`.

See the [`Human Interface Guidelines > Apple Pay`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/buttons-and-marks/) for more information.

##### Set the Button Size

You can resize the Apple Pay button to fit your website. The minimum displayed width and height for Apple Pay buttons are:

- For plain Apple Pay buttons the minimum displayed width is 100 points with a minimum displayed height of 30 points.
- For Apple Pay buttons that include a directive, such as “Buy with Apple Pay” or “Donate with Apple Pay,” the minimum displayed width is 140 points with a minimum displayed height of 30 points.

##### Set the Button Style

You can choose from several style options for the Apple Pay button to match your web site. See [`Human Interface Guidelines > Apple Pay`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/buttons-and-marks/) for guidance on which style to choose.

To display the black Apple Pay button, set the `-apple-pay-button-style` CSS property to `black`.

For example, the following example produces a black Apple Pay button:

```xml
<div style="display: inline-block;
-webkit-appearance: -apple-pay-button;
-apple-pay-button-type: plain;
-apple-pay-button-style: black;"
lang=en></div>
```

The color options for the `-apple-pay-button-style` CSS property are `white`, `white-outline`, or `black`.

##### Set the Buttons Corner Radius

You may configure the border radius of your Apple Pay button using the css `border-radius` property. The Apple Pay button supports a single `border-radius` value. If you set multiple `border-radius` properties, the largest value applies to all corners.

Use border radius to match the styles of other buttons on your website. The default border radius is 4 points`.`

In the following example, setting border radius to `0pt` displays a squared off button:

```xml
<div style="display: inline-block;
border-radius: 0pt;
-webkit-appearance: -apple-pay-button;
-apple-pay-button-type: plain;
-apple-pay-button-style: white-outline;"
lang=en></div>
```

## See Also

- [Localizing Apple Pay Buttons Using CSS](localizing-apple-pay-buttons-using-css.md)
  Set the language of an Apple Pay button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/styling-the-apple-pay-button-using-css)*