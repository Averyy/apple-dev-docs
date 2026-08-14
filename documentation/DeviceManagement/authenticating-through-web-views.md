# Authenticating through web views

**Framework**: Device Management

Use your own custom web interfaces to authenticate users.

#### Overview

Beginning with iOS 13 and macOS 10.15, you can present a custom web interface to the user during Automated Device Enrollment. The `configuration_web_url` key in the Automated Device Enrollment [`Profile`](profile.md) defines the value of a custom URL to be presented in a web view and also supports the [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession). Use this key to define your own UI for authentication, with your preferred authentication method. After authenticating the user, the device management (MDM) enrollment profile downloads to their device.

On the initial page load of the `configuration_web_url`:

- The URL must have an `https` scheme and is a `GET` request.
- Use the certificates in the `AnchorCerts` property of the Automated Device Enrollment [`Profile`](profile.md) to pin the host to the certificates.
- A custom header `x-apple-aspen-deviceinfo` is appended to the request. It contains a base64 encoding of a Cryptographic Message Syntax (CMS) envelope that contains a property list file with device attributes. This is the same information, in the same format, as provided in the initial `POST` request with token-based ADE enrollments.

On subsequent page loads:

- If navigation requires trust evaluation using certificates not normally trusted by the system, they must be included in `AnchorCerts`.
- The user interacts with the web view until the device management service provides a `.mobileconfig` file to the client. The `.mobileconfig` file must have a MIME type of `application/x-apple-aspen-config`. Then web view closes and the device attempts to install the profile, which must be a device management (MDM) enrollment profile.
- Although the web view allows the user to navigate to arbitrary pages at arbitrary sites, the device management (MDM) enrollment profile must originate from a host where the last two components of the domain name match the last two components of the `configuration_web_url` domain name.

For iOS, iPadOS, tvOS, and visionOS this flow is supported during initial setup of an erased device. For macOS, this flow is supported both within Setup Assistant and when enrollment is enforced when it was skipped during Setup Assistant.

## See Also

- [Authenticating for Automated Device Enrollment](authenticating-for-automated-device-enrollment.md)
  Communicate securely with the web service using a server token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/authenticating-through-web-views)*