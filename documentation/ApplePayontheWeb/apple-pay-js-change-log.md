# Apple Pay JS change log

**Framework**: Apple Pay on the Web

Learn about new features and updates in the Apple Pay JS SDK.

#### Overview

With the Apple Pay JS SDK, you can accept Apple Pay payments from customers on your website. Use this changelog to learn about feature updates, deprecations, and removals. You can learn more about Apple Pay JS version numbers and how to automatically link the latest available version in [`Loading the latest version of the Apple Pay JS SDK`](loading-the-latest-version-of-apple-pay-js.md).

#### 138

**Fixed**

- Fixed an error that might occur when the Apple Pay JS SDK loads more than once on a page.
- Fixed the payment modal briefly flashing white when displayed in Dark Mode.
- Fixed misalignment of the modal close button in Arabic (RTL) layouts.

**Added**

- Added the Apple Pay Merchandising web component for displaying Apple Pay and installment payment provider messaging.
- Added the script tag for the Apple Pay JS SDK version 1.3.8:

```javascript
<script src="https://applepay.cdn-apple.com/jsapi/v1.3.8/apple-pay-sdk.js" integrity="sha384-u/9mOkmShCO0v+dqCAZFhiutJuORfzvuyM5i+676iy7mLSWS6rlllHrIt15f/mqH" crossorigin="anonymous"></script>
```

- Added the URL for the Apple Pay JS SDK version 1.3.8: - `https://applepay.cdn-apple.com/jsapi/v1.3.8/apple-pay-sdk.js`
- Added the hash for the Apple Pay JS SDK version 1.3.8: - `sha384-u/9mOkmShCO0v+dqCAZFhiutJuORfzvuyM5i+676iy7mLSWS6rlllHrIt15f/mqH`

#### 137

**Fixed**

- Streamlined the URL structure used for the Apple Pay window for a cleaner, more direct format and improved performance.
- Fixed Apple Pay button styling under strict Content Security Policy (CSP) headers, so buttons render correctly without requiring inline styles.
- Fixed console warning messages that might appear during payment initialization.
- Improved Payment Request API compatibility by enhancing parameter validation, including handling cases in which optional parameters aren’t provided.

**Added**

- Enhanced error handling and validation for Payment Request API implementations.
- Added the script tag for the Apple Pay JS SDK version 1.3.7:

```javascript
<script src="https://applepay.cdn-apple.com/jsapi/v1.3.7/apple-pay-sdk.js" integrity="sha384-m79g5rSF+8ObiCeY5RGEXjDpxURj/6A4rz0xXbEY/UEzLITgAWZ0+x3gcYjVEuVe" crossorigin="anonymous"></script>
```

- Added the URL for the Apple Pay JS SDK version 1.3.7: - `https://applepay.cdn-apple.com/jsapi/v1.3.7/apple-pay-sdk.js`
- Added the hash for the Apple Pay JS SDK version 1.3.7: - `sha384-m79g5rSF+8ObiCeY5RGEXjDpxURj/6A4rz0xXbEY/UEzLITgAWZ0+x3gcYjVEuVe`

#### 136

**Fixed**

- Removed plaintext query parameters from the new window URL, transmitting request data as a single encoded value to improve security and privacy.
- Fixed an initialization issue that might trigger a JavaScript error when configuring `ApplePayWebOptions` in Safari.

**Added**

- Improved console logging for sandbox environments so the console clearly indicates the sandbox environment state.
- Added the script tag for the Apple Pay JS SDK version 1.3.6:

```javascript
<script src="https://applepay.cdn-apple.com/jsapi/v1.3.6/apple-pay-sdk.js" integrity="sha384-7KJIkGT+8p0K2rhsEQcz7zZ+nYUFUbN573ZKSgwp9YKN7uUC+h5TAhEIdOAZgo6R" crossorigin="anonymous"></script>
```

- Added the URL for the Apple Pay JS SDK version 1.3.6: - `https://applepay.cdn-apple.com/jsapi/v1.3.6/apple-pay-sdk.js`
- Added the hash for the Apple Pay JS SDK version 1.3.6: - `sha384-7KJIkGT+8p0K2rhsEQcz7zZ+nYUFUbN573ZKSgwp9YKN7uUC+h5TAhEIdOAZgo6R`

#### 135

**Fixed**

- Ensured required query parameters are correctly passed when launching Apple Pay in a new window.

**Added**

- Introduced support for a sandbox environment configuration. When operating in sandbox mode, a “Sandbox Mode” banner displays and the console logs indicate the environment state. The `applePayCapabilities` API returns `paymentCredentialStatusUnknown` for supported browsers when tested in sandbox mode.
- Added the script tag for the Apple Pay JS SDK version 1.3.5:

```javascript
<script src="https://applepay.cdn-apple.com/jsapi/v1.3.5/apple-pay-sdk.js" integrity="sha384-PXB7Px9JgKaXn/a7SomvCNcHbTae7QLO5r9Icn2tfMy2SRslUQUeNZGUIYgKCRux" crossorigin="anonymous"></script>
```

- Added the URL for the Apple Pay JS SDK version 1.3.5: - `https://applepay.cdn-apple.com/jsapi/v1.3.5/apple-pay-sdk.js`
- Added the hash for the Apple Pay JS SDK version 1.3.5: - `sha384-PXB7Px9JgKaXn/a7SomvCNcHbTae7QLO5r9Icn2tfMy2SRslUQUeNZGUIYgKCRux`

#### 134

**Fixed**

- Improved the new window experience in third-party browsers by updating the visible URL to use a more trusted, easier to use domain.

**Added**

- When Apple Pay launches in a new window, the window now displays the updated `pay.apple.com` domain for a cleaner, more consistent appearance.
- Added the script tag for the Apple Pay JS SDK version 1.3.4:

```javascript
<script src="https://applepay.cdn-apple.com/jsapi/v1.3.4/apple-pay-sdk.js" integrity="sha384-EkOwSYjCfsPDaNshCOrDCVP+66slBQUaEZtukKqIp2ew8lWUsPaKO/JJGxGays+y" crossorigin="anonymous"></script>
```

- Added the URL for the Apple Pay JS SDK version 1.3.4: - `https://applepay.cdn-apple.com/jsapi/v1.3.4/apple-pay-sdk.js`
- Added the hash for the Apple Pay JS SDK version 1.3.4: - `sha384-EkOwSYjCfsPDaNshCOrDCVP+66slBQUaEZtukKqIp2ew8lWUsPaKO/JJGxGays+y`

#### 133

**Fixed**

- Improved validation for merchant status checks in non-Safari browsers to align behavior with PassKit and Safari.

**Added**

- Updated the `applePayCapabilities` JavaScript API to use the latest merchant status endpoint for improved reliability and consistency during merchant verification.
- Added support for sending language and user agent information in the `getPaymentRequestResponse` payload to enhance localization and analytics.
- Added the script tag for the Apple Pay JS SDK version 1.3.3:

```javascript
<script src="https://applepay.cdn-apple.com/jsapi/v1.3.3/apple-pay-sdk.js" integrity="sha384-SmrWHrJWbmqUdhs1oyfLOcLtZZZAd9vm5D0NUvBlI4OhI2BjxZyxtcSfujdb885p" crossorigin="anonymous"></script>
```

- Added the URL for the Apple Pay JS SDK version 1.3.3: - `https://applepay.cdn-apple.com/jsapi/v1.3.3/apple-pay-sdk.js`
- Added the hash for the Apple Pay JS SDK version 1.3.3: - `sha384-SmrWHrJWbmqUdhs1oyfLOcLtZZZAd9vm5D0NUvBlI4OhI2BjxZyxtcSfujdb885p`

#### 132

**Fixed**

- Fixed localization issues.
- Fixed the overlay modal that wasn’t the topmost element for some merchants.

**Added**

- Added small enhancements to the new window flow.
- Added the script tag for the Apple Pay JS SDK version 1.3.2:

```javascript
<script src="https://applepay.cdn-apple.com/jsapi/v1.3.2/apple-pay-sdk.js" integrity="sha384-DZRWMZLyVXr+7shJfal8pIG2v4KisLoSWFjZQMUv0+GWaCwoa82qeHsWrbBIUDPU" crossorigin="anonymous"></script>
```

- Added the URL for the Apple Pay JS SDK version 1.3.2: - `https://applepay.cdn-apple.com/jsapi/v1.3.2/apple-pay-sdk.js`
- Added the hash for the Apple Pay JS SDK version 1.3.2: - `sha384-DZRWMZLyVXr+7shJfal8pIG2v4KisLoSWFjZQMUv0+GWaCwoa82qeHsWrbBIUDP`

#### 131

**Fixed**

- Fixed the [`oncancel`](applepaysession/oncancel.md) callback that wasn’t triggered when closing a modal before a scan.

**Added**

- Added the script tag for the Apple Pay JS SDK version 1.3.1:

```javascript
<script src="https://applepay.cdn-apple.com/jsapi/v1.3.1/apple-pay-sdk.js" integrity="sha384-kVWHV5PiZFlm9mRpZgyyprD3/PPkKg9gZ7z9TCHnvEkrYmFg/7nfpvTztecxMZvw" crossorigin="anonymous"></script>

```

- Added the URL for the Apple Pay JS SDK version 1.3.1: - `https://applepay.cdn-apple.com/jsapi/v1.3.1/apple-pay-sdk.js`
- Added the hash for the Apple Pay JS SDK version 1.3.1: - `sha384-kVWHV5PiZFlm9mRpZgyyprD3/PPkKg9gZ7z9TCHnvEkrYmFg/7nfpvTztecxMZvw`


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/apple-pay-js-change-log)*