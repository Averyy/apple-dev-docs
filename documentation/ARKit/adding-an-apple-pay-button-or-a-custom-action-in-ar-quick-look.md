# Adding an Apple Pay Button or a Custom Action in AR Quick Look

**Framework**: ARKit

Provide a banner that users can tap to make a purchase or perform a custom action in an AR experience.

#### Overview

For AR experiences initiated through the web in iOS 13.3 or later, you can display an Apple Pay button so users can make purchases from your website.

![Screenshot of an AR experience featuring a banner that contains an Apple Pay button.](https://docs-assets.developer.apple.com/published/24a6635aab8ced19bff58a3c4231d0aa/media-3432381%402x.png)

Alternatively, you can provide text in the banner that users can tap to invoke a custom action in your website, like adding a previewed item to a shopping cart.

![Screenshot of a banner featuring a custom hyperlink that reads “Add to cart”.](https://docs-assets.developer.apple.com/published/33f2cfa8289f72df4263aa05f90ca3e9/media-3425396%402x.png)

In addition, you can supply AR Quick Look with custom HTML that completely customizes the banner’s graphics.

![Screenshot of a banner in which a custom HTML file rendered the contents.](https://docs-assets.developer.apple.com/published/4ae350e30a26b60ba6778dc31898455c/media-3425393%402x.png)

To add an Apple Pay button or custom text or graphics in a banner, choose URL parameters to configure AR Quick Look for your website. Finally, detect and react to customer taps to the banner.

##### Choose an Apple Pay Button Style

To select a style of Apple Pay button for your AR experience, append the `applePayButtonType` parameter to your website URL.

```javascript
https://example.com/biplane.usdz#applePayButtonType=plain
```

You can choose from the button options using the button type values shown here.

![Figure showing each of the seven Apple Pay button options, annotated by the the button type value parameter associated with the button style.](https://docs-assets.developer.apple.com/published/c17be74f46391236a827e7f35eb23947/media-3421819%402x.png)

##### Provide Custom Text

Instead of an Apple Pay button, you can supply text that AR Quick Look displays as a custom action button, as in the following image.

![Screenshot of a banner that features a custom action button using text that you supply.](https://docs-assets.developer.apple.com/published/f00d882d960a5b4acf1ba1db8d481d53/media-3425397%402x.png)

Append the `callToAction` URL parameter with the custom text as the value. The following example URL renders a banner with the text “Add to cart”:

```javascript
https://example.com/biplane.usdz#callToAction=Add%20to%20cart
```

Because URLs can’t contain spaces, be sure to URL-encode the custom text before appending it as a URL parameter. If your website supports multiple languages, localize the custom text before URL-encoding it for the URL parameter list.

##### Define the Item

When you add an Apple Pay button or a custom action button to AR Quick Look, set the description of the previewed items using the `checkoutTitle`, `checkoutSubtitle`, and `price` URL parameters. AR Quick Look displays the subtitle and price separated by a comma below the title.

![Screenshot of a banner with the item’s title, subtitle, and price highlighted.](https://docs-assets.developer.apple.com/published/1b0c4551566c670f5c1b8c0c087babf2/media-3425394%402x.png)

If AR Quick Look can’t fit the subtitle and price on one line, it truncates the subtitle with an ellipsis. The following example URL renders the banner.

```javascript
https://example.com/biplane.usdz#applePayButtonType=buy&checkoutTitle=Biplane%20Toy&checkoutSubtitle=Rustic%20finish%20with%20rotating%20propeller&price=$15
```

If your website supports multiple languages, localize the item title, subtitle, and price before URL-encoding them for the URL parameter list.

##### Display a Custom Banner

To take full control of the banner’s graphics, supply a custom HTML file through the `custom` URL parameter. The following example URL renders a banner from a custom file named `comingSoonBanner`.

```swift
https://example.com/biplane.usdz#custom=https://example.com/customBanners/comingSoonBanner.html

```

This example URL creates the AR experience illustrated below.

![Screenshot of an AR experience that features a banner that AR Quick Look renders with your custom HTML file.](https://docs-assets.developer.apple.com/published/d1207e7ba8e09fcdf7249486169581e2/media-3425395%402x.png)

If you use the `custom` URL parameter, the value must be an absolute URL. To comply with AR Quick Look’s security standards, ensure the server sends the HTML resource over HTTPS.

> ❗ **Important**:  AR Quick Look displays the contents of the HTML only. If you embed actions such as links or events, AR Quick Look ignores them.

##### Define the Custom Banners Height

When you display a custom banner, you can set the banner height using the `customHeight` URL parameter.

Supply a value of `small`, `medium`, or `large` to set the banner height to 81, 121, or 161 points, respectively. For example:

```javascript
https://example.com/biplane.usdz#custom=https://example.com/my-custom-page.html&customHeight=large
```

AR Quick Look automatically scales the width of the banner to the size and orientation of the device on which it displays. The maximum width of the custom banner is 450 points. If you omit the `customHeight` URL parameter, AR Quick Look uses the default value, `small`.

##### Detect a Tap

When the user taps the Apple Pay button or custom action button, WebKit sends a DOM message to the `<a>` element of your code that references the 3D asset.

```javascript
<a id="ar-link" rel="ar" href="https://example.com/cool-model.usdz#applePayButtonType=pay....etc">  <img src="poster.jpg"></a>
```

To be notified of the tap, define a JavaScript listener for the `message` event on your anchor.

```javascript
const linkElement = document.getElementById("ar-link");
linkElement.addEventListener("message", function (event) { ... }, false);
```

When WebKit invokes your listener, check the `data` property. A value of `_apple_ar_quicklook_button_tapped` confirms the user tapped the banner in AR Quick Look.

```swift
const linkElement = document.getElementById("ar-link");
linkElement.addEventListener("message", function (event) {   
    if (event.data == "_apple_ar_quicklook_button_tapped") {
        // Handle the user tap.   
    }
}, false);
```

The `message` event follows normal DOM processing rules. Rather than adding a listener for a specific anchor, you can add a listener at the document root for all AR links, and use the `event.target` to determine which anchor the user invoked.

##### React to a Tap

Define the actions your website takes in response to a user tap in your event listener. When the user taps the custom action button, you might add the previewed item to a shopping cart or take the user to a checkout page, depending on the banner’s text and custom action.

If your banner displays an Apple Pay button, bring up the Apple Pay prompt using [`Apple Pay JS API`](https://developer.apple.com/documentation/ApplePayontheWeb/apple-pay-js-api).

If your banner displays an Apple Messages for Business button, send the user to Messages using your company’s custom Apple Messages for Business URL. For more infomation, see [`Starting a Chat from a URL`](https://developer.apple.comhttps://register.apple.com/resources/messages/messaging-documentation/chat-with-customers#starting-a-chat-from-a-url).

## See Also

- [Previewing a Model with AR Quick Look](previewing-a-model-with-ar-quick-look.md)
  Display a model or scene that the user can move, scale, and share with others.
- [Adding Visual Effects in AR Quick Look and RealityKit](adding-visual-effects-in-ar-quick-look-and-realitykit.md)
  Balance the appearance and performance of your AR experiences with modeling strategies.
- [USDZ schemas for AR](../RealityKit/usdz-schemas-for-ar.md)
  Add augmented reality functionality to your 3D content using USDZ schemas.
- [Specifying a lighting environment in AR Quick Look](specifying-a-lighting-environment-in-ar-quick-look.md)
  Add metadata to your USDZ file to specify its lighting characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/adding-an-apple-pay-button-or-a-custom-action-in-ar-quick-look)*