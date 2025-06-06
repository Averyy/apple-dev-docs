# Adding a Track with Apple Wallet button

**Framework**: Apple Pay on the Web

Configure and style an Apple Wallet Button to match your website.

#### Overview

In iOS 17.0 and later and macOS 14.0 and later, Apple Wallet order tracking is available on the web and provides a variety of button types that you can use on your website. You can specify the Track with Apple Wallet button style, compactness, and localization using attributes that you supply to the JavaScript function that displays the button.

##### Add the Apple Pay Javascript Api to the Page Header

To display an Track with Apple Wallet button, add the following script tag to your webpage’s head tag to load the Apple Pay JavaScript API:

```xml
<head>
    <script async crossorigin 
      src="https://applepay.cdn-apple.com/jsapi/1.latest/apple-pay-sdk.js">
    </script>
</head>
```

The script tag contains the URL that loads the `apple-pay-sdk.js`, from the Apple Pay JS CDN. The script tag includes two additional attributes:

Additionally, ensure that your website allows a Content Security Policy for Apple Pay JS to function properly.

##### Add a Standard Apple Wallet Button

To display the button, add an `apple-wallet-button` tag to your webpage and set the `buttonstyle`, `compact`, `locale`, and `onclick` parameters. For example, this call into the Apple Pay JavaScript library provides details necessary for rendering the button localized to the US, and uses the default compactness and style:

```xml
<style>
    apple-wallet-button {
        --apple-wallet-button-border-radius: 5px;
        --apple-wallet-button-height: 40px;
        --apple-wallet-button-width: 180px;
        --apple-wallet-button-padding: 0px 0px;
        --apple-wallet-button-box-sizing: content-box;
    }
</style>
<apple-wallet-button
    buttonstyle="black"
    compact="true"
    locale="en-US"
    onclick="addOrder();"
 />
```

See [`Build a distributable order package`](https://developer.apple.comhttps://applepaydemo.apple.com/order-tracking#generatePayload) in [`Apple Pay Order Tracking Demo`](https://developer.apple.comhttps://applepaydemo.apple.com/order-tracking) for tips on generating the Order Package.

To protect user privacy, ensure the package URL the merchant system generates uses the same authenticated user session and implements the following policies, with regard to package URLs:

- It’s not possible to guess the next order package URL automatically.
- It’s not possible to scrape order packages anonymously.
- It’s not possible for a user to download an order package that belongs to a different user, even if they find out the order package’s URL.

##### Customize an Apple Wallet Button

There are several options for customizing the button’s attributes:

| Attribute | Accepted Values | Description |
| --- | --- | --- |
| `buttonstyle` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(required)` | `black`, `white-border`, or `white` | The button display style for either light mode or dark mode devices. |
| `compact` | `true` or `false` | Modifies the display style of the button to either have the default compact multi-line view or the single line view. |
| `locale` | An BCP 47 language code, such as `en-US`. | The language and region the button uses. |
| `onclick` | A JavaScript function | An inline function argument to trigger the distributable order package code. |

To customize the button’s styling, use the following:

| Atrribute | Type | Description |
| --- | --- | --- |
| `--apple-wallet-button-border-radius` | number | This CSS property rounds the corners of an element’s outer border edge. You can set a single radius to make circular corners, or two radii to make elliptical corners. |
| `--apple-wallet-button-height` | number | This CSS property specifies the height of an element. By default, the property defines the height of the content area. If you set `box-sizing` to the value of `border-box`, however, it instead determines the height of the border area. |
| `--apple-wallet-button-width` | number | This CSS property sets an element’s width. By default, it sets the width of the content area, but if you set `box-sizing` to the value of `border-box`, it sets the width of the border area. |
| `--apple-wallet-button-padding` | number | This CSS shorthand property sets the padding area on all four sides of an element at once. |
| `--apple-wallet-button-box-sizing` | `border-box` , `content-box` | The value for the `box-sizing` CSS property sets how the total width and height of an element is calculated. |

##### Determine Sizing Requirements

For sizing requirements for the Track with Apple Wallet button, along with other design guidelines, see [`Apple Pay`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pay) in the Human Interface Guidelines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/adding-a-track-with-apple-wallet-button)*