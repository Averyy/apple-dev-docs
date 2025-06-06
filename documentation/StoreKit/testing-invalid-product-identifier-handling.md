# Testing invalid product identifier handling

**Framework**: StoreKit

Verify that your app correctly handles invalid product identifiers.

#### Overview

Intentionally include an invalid identifier in your app’s list of product identifiers. Then do one of the following:

- In a production build, verify that the app displays the rest of its store UI and that users can purchase the valid products.
- In a development build, verify that the app brings the issue to your attention.

Check the console log and verify that you can correctly identify the invalid product identifier. Make sure you remove it after testing.

For more information on fetching product identifiers, see [`Loading in-app product identifiers`](loading-in-app-product-identifiers.md).

## See Also

- [Testing fetching product identifiers](testing-fetching-product-identifiers.md)
  Verify that your app receives the correct product identifiers by inspecting or replicating your app’s process for retrieving the identifiers.
- [Testing a product request](testing-a-product-request.md)
  Verify that requests for products function properly in the sandbox environment by inspecting the App Store response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-invalid-product-identifier-handling)*