# Integrating the Apple Pay merchandising component

**Framework**: Apple Pay on the Web

Display Apple Pay installment payment options and merchandising information to customers using the Apple Pay Merchandising web component.

#### Overview

The Apple Pay Merchandising component is a native web component that displays payment installment options from various payment providers. It helps merchants showcase flexible payment options to customers by making payment terms clear and accessible.

The Apple Pay Merchandising component, `<apple-pay-merchandising>` provides a seamless way to display installment payment information on your website. The component automatically fetches and displays relevant payment options based on the purchase amount, currency, and available payment providers.

##### Load the Apple Pay Sdk with Components

To use the Apple Pay Merchandising component, load the Apple Pay JS SDK with the desired components:

```html
<head>
    <script crossorigin
      src="https://applepay.cdn-apple.com/jsapi/1.latest/apple-pay-sdk.js?components=apple-pay-button,wallet-button,apple-pay-merchandising"
      crossorigin="anonymous">
    </script>
</head>
```

Available components:

- `apple-pay-button`: The Apple Pay button component.
- `wallet-button`: The Apple Wallet button component.
- `apple-pay-merchandising`: The Apple Pay merchandising widget.

> ❗ **Important**: If the `components` query parameter is not specified, `apple-pay-button` and `wallet-button` are loaded by default. When you specify the `components` parameter, you must explicitly list all components you need, including `apple-pay-button` and `wallet-button` if you are using them.

##### Add the Element to Your Page

Add the `<apple-pay-merchandising>` element to your page with the required attributes:

```html
<apple-pay-merchandising
  amount="99.99"
  currency="USD"
  type="installments-logos">
</apple-pay-merchandising>
```

##### Choose a Widget Type

The component supports three widget types to display payment information in different formats:

- **`installments-logos`**: Displays multiple payment provider logos with installment information.
- **`installments-text`**: A text-focused display of installment options without prominent logos.
- **`installments-how-to`**: A simplified view explaining how installment payments work.

##### Add the Required Attributes

The following attributes are required for the component to function:

- **`amount`**: The purchase amount, for example “99.99”.
- **`currency`**: The three-letter currency code, for example “USD”, “EUR”, “GBP”.

##### Configure Optional Attributes

Customize the component behavior with these optional attributes:

- **`type`**: The widget display type (default: “installments-logos”).
- **`partners`**: A JSON array of payment provider names to display, for example [`"affirm", "klarna"`].
- **`theme`**: A visual theme: “light”, “dark”, or “auto” (default: “auto”).
- **`language`**: The language/locale code (default: “en”).
- **`country`**: The country code for region-specific payment options, for example “US”, “CA”.
- **`version`**: The API version (default: “v1”).
- **`origin-url`**: The merchant’s website origin URL for analytics for example, “https://example.com”.
- **`apple-pay-mid`**: Apple Pay Merchant Identifier for analytics, for example “merchant.com.example.store”.
- **`merchant-name`**: The merchant’s display name for analytics for example, “Example Store”.
- **`debug`**: Enables debug mode for development (default: false).

The following example shows the merchandising component with multiple payment partner providers.

```html
<apple-pay-merchandising
  amount="499.00"
  currency="USD"
  type="installments-logos"
  partners='["affirm", "klarna", "afterpay"]'
  theme="light"
  language="en-US"
  country="US">
</apple-pay-merchandising>
```

##### Add Dark Mode Support

The component automatically adapts to the user’s system color scheme when `theme="auto"` is set (default). You can also explicitly set light or dark themes:

```html
<!-- Automatically adapts to system preference -->
<apple-pay-merchandising
  amount="99.99"
  currency="USD"
  theme="auto">
</apple-pay-merchandising>

<!-- Always use dark theme -->
<apple-pay-merchandising
  amount="99.99"
  currency="USD"
  theme="dark">
</apple-pay-merchandising>
```

##### Access the Component Programmatically

You can interact with the component using JavaScript:

```javascript
// Get the component reference.
const widget = document.querySelector('apple-pay-merchandising');

// Update the attributes dynamically.
widget.setAttribute('amount', '299.99');
widget.setAttribute('theme', 'dark');

// Access the widget data.
widget.data.then(data => {
  console.log('Widget identifier:', data.widgetIdentifier);
});
```

##### Configure a Content Security Policy

When implementing Content Security Policy (CSP), include the following directives to allow the merchandising component to function properly:

```html
img-src https://applepay.cdn-apple.com;
frame-src https://applepay.cdn-apple.com;
script-src https://applepay.cdn-apple.com;
connect-src https://applepay.cdn-apple.com;
```

##### Support Accessibility Interactions

The Apple Pay Merchandising component is built with accessibility in mind. Some of the accessible features of the component include:

- Uses semantic HTML structure for screen readers.
- Uses proper ARIA labels for images and interactive elements.
- Supports keyboard navigation for interactive elements.
- Supports right-to-left (RTL) language for Arabic, Hebrew, and other RTL languages.
- Allows the choice of the person’s system color scheme preferences.

##### Optimize the Component for Your Site

- Place prominently: Display the component near product pricing or on the cart page where customers make purchase decisions.
- Update dynamically: Update the `amount` attribute when the cart total changes to show accurate installment information.
- Match your theme: Use the `theme` attribute to match your website’s design.
- Test with real amounts: Test with various price points to ensure installment options display correctly.
- Consider mobile: The component is responsive and adapts to different screen sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/integrating-the-apple-pay-merchandising-component)*