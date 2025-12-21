# Preparing to use the app attest service

**Framework**: DeviceCheck

Test your implementation in a development environment and onboard users gradually.

#### Overview

The App Attest service records device metrics that you can’t reset. To avoid affecting the real metrics for devices that you use for development, you test your implementation in a sandbox environment. When you do start using App Attest in a production environment, use care not to overwhelm Apple’s servers with requests from too many devices at once.

##### Test Your Implementation

During development, you use a sandbox environment to test your adoption of App Attest. The App Attest service tracks the keys that you generate in this mode separately from the keys generated in production mode. This allows you to generate and attest any number of keys on a given device without polluting that device’s production key count.

If instead you want to use the App Attest production servers during development, add the [`App Attest Environment`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.devicecheck.appattest-environment) entitlement to your app’s entitlements file, and set the associated value to `production`. Regardless of how you set the entitlement, your app always operates in production mode after distribution, whether through TestFlight, the App Store, or the Apple Developer Enterprise Program.

When sending a sandbox-generated attestation object to your server, the verification procedure changes slightly. Specifically, expect to find the value `appattestsandbox` in the authenticator data’s `aaguid` field. Also, when using a sandbox-generated receipt to make the server-to-server call that obtains the fraud metric, use `https://data-development.appattest.apple.com` as the base URL.

> ❗ **Important**: You can’t use a key or receipt from the sandbox environment in the production environment, or vice versa.

##### Onboard Users Gradually

If you have a large user base, consider enabling App Attest in stages. When your app calls [`attestKey(_:clientDataHash:completionHandler:)`](dcappattestservice/attestkey(_:clientdatahash:completionhandler:).md) — which you typically do once per user per device — the DeviceCheck framework makes a call to an Apple server to perform the attestation. Apple servers might throttle attestation traffic from a particular app to avoid becoming overwhelmed if too many instances of your app make this call simultaneously. That could happen if you have a lot of users that simultaneously receive an app update enabling App Attest.

Instead, activate the feature for smaller groups of users over a period of time. As a rule of thumb, we suggest gradually and uniformly ramping up no more than 10 million users per day per app. After the initial rollout, your app makes requests only for new users, new devices, and reinstallations. This kind of traffic shouldn’t result in any throttling.

> ❗ **Important**: To avoid encountering [`attestKey(_:clientDataHash:completionHandler:)`](dcappattestservice/attestkey(_:clientdatahash:completionhandler:).md) rate limits, we generally recommend that your apps call this method fewer than 100 request per second across all installations of your apps. The rate limit threshold may fluctuate dynamically to protect Apple’s certificate signing infrastructure. Be prepared to handle these errors and to have a mechanism to pull back on requests from your apps if this occurs.

## See Also

- [Establishing your app’s integrity](establishing-your-app-s-integrity.md)
  Ensure that requests your server receives come from legitimate instances of your app.
- [Validating apps that connect to your server](validating-apps-that-connect-to-your-server.md)
  Verify that connections to your server come from legitimate instances of your app.
- [Assessing fraud risk](assessing-fraud-risk.md)
  Request and analyze risk data using server-to-server calls.
- [Attestation Object Validation Guide](attestation-object-validation-guide.md)
  Use this guide to validate your implementation of verifying the attestation object verification process.
- [class DCAppAttestService](dcappattestservice.md)
  A service that you use to validate the instance of your app running on a device.
- [App Attest Environment](../BundleResources/Entitlements/com.apple.developer.devicecheck.appattest-environment.md)
  The environment for an app that uses the App Attest service to validate itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/preparing-to-use-the-app-attest-service)*