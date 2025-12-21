# Apple Pay JS change log

**Framework**: Apple Pay on the Web

Learn about new features and updates in the Apple Pay JS SDK.

#### Overview

With the Apple Pay JS SDK, you can accept Apple Pay payments from customers on your website. Use this changelog to learn about feature updates, deprecations, and removals. You can learn more about Apple Pay JS version numbers and how to automatically link the latest available version in [`Loading the latest version of the Apple Pay JS SDK`](loading-the-latest-version-of-apple-pay-js.md).

#### 132

- Fixed localization issues.
- Fixed the overlay modal that wasn’t the topmost element for some merchants.

- Added small enhancements to the new window flow.
- Added the script tag for the Apple Pay JS SDK version 1.3.2:

```javascript
<script src="https://applepay.cdn-apple.com/jsapi/v1.3.2/apple-pay-sdk.js" integrity="sha384-DZRWMZLyVXr+7shJfal8pIG2v4KisLoSWFjZQMUv0+GWaCwoa82qeHsWrbBIUDPU" crossorigin="anonymous"></script>
```

- Added the URL for the Apple Pay JS SDK version 1.3.2: - `https://applepay.cdn-apple.com/jsapi/v1.3.2/apple-pay-sdk.js`
- Added the hash for the Apple Pay JS SDK version 1.3.2: - `sha384-DZRWMZLyVXr+7shJfal8pIG2v4KisLoSWFjZQMUv0+GWaCwoa82qeHsWrbBIUDP`

#### 131

- Fixed the [`oncancel`](applepaysession/oncancel.md) callback that wasn’t triggered when closing a modal before a scan.

- Added the script tag for the Apple Pay JS SDK version 1.3.1:

```javascript
<script src="https://applepay.cdn-apple.com/jsapi/v1.3.1/apple-pay-sdk.js" integrity="sha384-kVWHV5PiZFlm9mRpZgyyprD3/PPkKg9gZ7z9TCHnvEkrYmFg/7nfpvTztecxMZvw" crossorigin="anonymous"></script>

```

- Added the URL for the Apple Pay JS SDK version 1.3.1: - `https://applepay.cdn-apple.com/jsapi/v1.3.1/apple-pay-sdk.js`
- Added the hash for the Apple Pay JS SDK version 1.3.1: - `sha384-kVWHV5PiZFlm9mRpZgyyprD3/PPkKg9gZ7z9TCHnvEkrYmFg/7nfpvTztecxMZvw`


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/apple-pay-js-change-log)*