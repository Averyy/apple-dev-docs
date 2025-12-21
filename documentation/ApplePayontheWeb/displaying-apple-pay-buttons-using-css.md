# Displaying Apple Pay Buttons Using CSS

**Framework**: Apple Pay on the Web

Use CSS templates to display Apple Pay buttons in Safari.

#### Overview

Apple Pay provides a variety of Apple Pay buttons that you can use on your website to initiate a transaction. You can specify which button type to display and edit its appearance and size to fit your webpage. Before using a button, check if it’s available in the version of Safari the device is running. To draw Apple Pay buttons on devices with earlier iOS or macOS versions where Safari doesn’t support all button types, see [`Displaying Apple Pay Buttons Using CSS`](displaying-apple-pay-buttons-using-css#Draw-Apple-Pay-Buttons.md).

##### Choose a Button Type

Choose an Apple Pay button that best fits with the terminology and flow of your application. Specify the type of Apple Pay button to display by setting the `-apple-pay-button-type` property to one of the Apple Pay button values.

The following Apple Pay button values are available starting with Apple Pay on the Web version 2:

The following Apple Pay button values are available starting with Apple Pay on the Web version 4:

The following Apple Pay button values are available starting with Apple Pay on the Web version 10:

The following Apple Pay button values are available starting with Apple Pay on the Web version 12:

For more version information, see [`Apple Pay on the Web version history`](apple-pay-on-the-web-version-history.md).   For more information about button types and their usage, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/buttons-and-marks/).

##### Display an Apple Pay Button Using Css

The code example below uses CSS properties to display Apple Pay buttons. The code supports devices running macOS 10.12 and later, and iOS 10 and later, by using the CSS `@supports` feature to determine if the `-webkit-appearance: -apple-pay-button` property is available. For devices with earlier iOS or macOS versions where Safari doesn’t support these button types, use the plain Apple Pay button instead (see [`Displaying Apple Pay Buttons Using CSS`](displaying-apple-pay-buttons-using-css#Draw-Apple-Pay-Buttons.md)).

```other
/* HTML */
<div class="apple-pay-button apple-pay-button-black">
</div>

/* CSS */
.apple-pay-button {
    display: inline-block;
    -webkit-appearance: -apple-pay-button;
    -apple-pay-button-type: donate; /* Use any supported button type. */
}
.apple-pay-button-black {
    -apple-pay-button-style: black;
}
.apple-pay-button-white {
    -apple-pay-button-style: white;
}
.apple-pay-button-white-with-line {
    -apple-pay-button-style: white-outline;
}
```

##### Draw Apple Pay Buttons

When your app runs on older versions of macOS and iOS where Safari doesn’t support the `-webkit-appearance: -apple-pay-button` property, you must draw the Apple Pay button. The sample code listings below use `@supports` to determine whether the browser supports `-apple-pay-button` property, and draw the buttons if it’s not supported. The two buttons you can choose to draw are the plain Apple Pay button, and the Buy with Apple Pay button.

The following code example displays a plain Apple Pay button.

```other
/* Template for logo only button (height independent). */
/* HTML */
<div class="apple-pay-button apple-pay-button-white"></div>

/* CSS */
@supports (-webkit-appearance: -apple-pay-button) { 
    .apple-pay-button {
        display: inline-block;
        -webkit-appearance: -apple-pay-button;
    }
    .apple-pay-button-black {
        -apple-pay-button-style: black;
    }
    .apple-pay-button-white {
        -apple-pay-button-style: white;
    }
    .apple-pay-button-white-with-line {
        -apple-pay-button-style: white-outline;
    }
}

@supports not (-webkit-appearance: -apple-pay-button) {
    .apple-pay-button {
        display: inline-block;
        background-size: 100% 60%;
        background-repeat: no-repeat;
        background-position: 50% 50%;
        border-radius: 5px;
        padding: 0px;
        box-sizing: border-box;
        min-width: 200px;
        min-height: 32px;
        max-height: 64px;
    }
    .apple-pay-button-black {
        background-image: -webkit-named-image(apple-pay-logo-white);
        background-color: black;
    }
    .apple-pay-button-white {
        background-image: -webkit-named-image(apple-pay-logo-black);
        background-color: white;
    }
    .apple-pay-button-white-with-line {
        background-image: -webkit-named-image(apple-pay-logo-black);
        background-color: white;
        border: .5px solid black;
    } 
}
```

The following code example displays a Buy with Apple Pay button.

```other
/* Template for "Buy with" button with height: 32 */
/* HTML */
<div class="apple-pay-button-with-text apple-pay-button-white-with-text">
  <span class="text">Buy with</span>
  <span class="logo"></span>
</div>

/* CSS */
@supports (-webkit-appearance: -apple-pay-button) {
    .apple-pay-button-with-text {
        display: inline-block;
        -webkit-appearance: -apple-pay-button;
        -apple-pay-button-type: buy;
    }
    .apple-pay-button-with-text > * {
        display: none;
    }
    .apple-pay-button-black-with-text {
        -apple-pay-button-style: black;
    }
    .apple-pay-button-white-with-text {
        -apple-pay-button-style: white;
    }
    .apple-pay-button-white-with-line-with-text {
        -apple-pay-button-style: white-outline;
    }
}

@supports not (-webkit-appearance: -apple-pay-button) {
    .apple-pay-button-with-text {
        --apple-pay-scale: 1; /* (height / 32) */
        display: inline-flex;
        justify-content: center;
        font-size: 12px;
        border-radius: 5px;
        padding: 0px;
        box-sizing: border-box;
        min-width: 200px;
        min-height: 32px;
        max-height: 64px;
    }
    .apple-pay-button-black-with-text {
        background-color: black;
        color: white;
    }
    .apple-pay-button-white-with-text {
        background-color: white;
        color: black;
    }
    .apple-pay-button-white-with-line-with-text {
        background-color: white;
        color: black;
        border: .5px solid black;
    }
    .apple-pay-button-with-text.apple-pay-button-black-with-text > .logo {
        background-image: -webkit-named-image(apple-pay-logo-white);
        background-color: black;
    }
    .apple-pay-button-with-text.apple-pay-button-white-with-text > .logo {
        background-image: -webkit-named-image(apple-pay-logo-black);
        background-color: white;
    }
    .apple-pay-button-with-text.apple-pay-button-white-with-line-with-text > .logo {
        background-image: -webkit-named-image(apple-pay-logo-black);
        background-color: white;
    }
    .apple-pay-button-with-text > .text {
        font-family: -apple-system;
        font-size: calc(1em * var(--apple-pay-scale));
        font-weight: 300;
        align-self: center;
        margin-right: calc(2px * var(--apple-pay-scale));
    }
    .apple-pay-button-with-text > .logo {
        width: calc(35px * var(--scale));
        height: 100%;
        background-size: 100% 60%;
        background-repeat: no-repeat;
        background-position: 0 50%;
        margin-left: calc(2px * var(--apple-pay-scale));
        border: none;
    }
}
   
```

## Topics

### Styling the Apple Pay Button
- [Styling the Apple Pay Button Using CSS](styling-the-apple-pay-button-using-css.md)
  Choose a button color and size to suit your webpage.
- [Localizing Apple Pay Buttons Using CSS](localizing-apple-pay-buttons-using-css.md)
  Set the language of an Apple Pay button.

## See Also

- [Displaying Apple Pay Buttons Using JavaScript](displaying-apple-pay-buttons-using-javascript.md)
  Load and configure the JavaScript Apple Pay button.
- [ApplePayButton](applepaybutton.md)
  An object that displays a button either to trigger payments through Apple Pay or to prompt the user to set up a card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/displaying-apple-pay-buttons-using-css)*