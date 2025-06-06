# Adding an Apple Pay Later visual merchandising widget

**Framework**: Applepayontheweb

Configure and style Apple Pay Later visual merchandising widgets to match your website.

#### Overview

> **Note**:  Apple Pay Later is deprecated.

In iOS and iPadOS 16.4 and later, Apple Pay on the Web provides a variety of Apple Pay merchandising widget types that you can use on your website. You can specify the Apple Pay merchandising widget style, type, and localization using attributes that you supply to a JavaScript function that displays the widget.

##### Add the Apple Pay Javascript Api to the Page Header

To display an Apple Pay Later visual merchandising widget, add the following script tag to your webpage’s `head` tag to load the Apple Pay JavaScript API:

```xml
<head>
    <script src="https://applepay.cdn-apple.com/jsapi/v1.1.0/apple-pay-sdk.js"
    crossorigin async data-initial-token="Your Apple Pay JS token"></script>
</head>
```

The script tag contains the URL that loads the `apple-pay-sdk.js`, from the Apple Pay JS CDN. The script tag includes three additional attributes:

Additionally, you need to ensure that your website allows a Content Security Policy for Apple Pay JS to function properly.

##### Add a Standard Widget

To display the widget, add an `apple-pay-merchandising` tag to your webpage and set the amount, style, type, and locale parameters. For example, this call into the Apple Pay JavaScript library provides details necessary for rendering the widget localized to the US, and uses the default size and type:

```xml
<apple-pay-merchandising 
    amount="108" 
    type="plain" 
    locale="en-US" 
    country-code="US">
</apple-pay-merchandising>
```

There are several options for customizing the widget’s appearance:

| Attribute | Type | Description |
| --- | --- | --- |
| `amount` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (required) | A string that represents the amount of the transaction as a decimal number, for example `“108”`. | The payment amount displayed in the widget, usually a product’s price. |
| `type` | `badge`, `plain`, `price`, or `checkout` | A string that describes the kind of Apple Pay Later visual merchandising widget. |
| `modal-type` | `learn-more` or `calculator` | A string that defines the contents of the modal that the visual merchandising widget displays. Use `learn-more` to display information about Apple Pay Later or `calculator` to display a breakdown of payments. |
| `locale` | An BCP 47 language code, such as `en-US`. | The language and region the widget uses for the Apple Pay Later visual merchandising widget. |
| `country-code`  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (required) | A two-letter [`ISO-3166`](https://developer.apple.comhttps://www.iso.org/iso-3166-country-codes.html) country code. | The country or region of the merchant’s principal place of business. |
| `currency-code`  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (required) | A three letter [`ISO-4217`](https://developer.apple.comhttps://www.iso.org/iso-4217-currency-codes.html) currency code. | The currency in use at the merchant’s principal place of business |
| `theme` | `dark`, `light`, or `auto` | The appearance of the widget. Defaults to `auto` if no value is specified. |
| `debug` | `true` or `false` | The setting to use for testing purposes to force the widget to display on all devices and operating systems.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) You need to remove this setting before deploying to production. |

##### Determine Sizing Requirements

For sizing requirements for the Apple Pay Later visual merchandising widget, along with other design guidelines, see [`Apple Pay`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pay) in the Human Interface Guidelines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ApplePayontheWeb/adding-an-apple-pay-later-visual-merchandising-widget)*