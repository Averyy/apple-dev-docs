# Authenticating Through Web Views

**Framework**: Device Management

Use your own custom web interfaces to authenticate users.

#### Overview

Beginning with iOS 13 and macOS 10.15, enterprises can use their own custom web interface to authenticate with the Device Enrollment Program (DEP). The `configuration_web_url` key in the DEP [`Profile`](profile.md) defines the value of the custom URL to present to the user in a web view. Use this key to define your own UI for authentication, with your preferred authentication method. After the user is authenticated, the MDM enrollment profile is downloaded.

On the initial page load of the `configuration_web_url:`

- The URL must have an `https` scheme and is a `GET` request.
- Use the certificates in the `AnchorCerts` property of the [`Profile`](profile.md) to pin the host to the certificates.
- A custom header `x-apple-aspen-deviceinfo` is appended to the request. It contains a base64 encoding of a CMS (Cryptographic Message Syntax) envelope that contains a plist with device attributes. This is the same information, in the same format, as provided in the initial `POST` request with token-based DEP enrollments.

On subsequent page loads:

- If navigation requires trust evaluation using certs not normally trusted by the system, they must be included in `AnchorCerts`.
- The user interacts with the web view until the server provides a `.mobileconfig` file to the client. The `.mobileconfig` file must have a MIME type of `application/x-apple-aspen-config`. Then web view closes and the OS attempts to install the profile, which must be an MDM enrollment profile.
- Although the web view allows the user to navigate to arbitrary pages at arbitrary sites, the enrollment profile must originate from a host where the last two components of the domain name match the last two components of the `configuration_web_url` domain name.

For iOS, this flow is supported during initial setup of an erased device. For macOS, this flow is supported both within Setup Assistant and also via the Profiles pref pane, if DEP enrollment was skipped during Setup Assistant.

## See Also

- [Authenticating with a Device Enrollment Program (DEP) Server](authenticating-with-a-device-enrollment-program-dep-server.md)
  Communicate securely with a DEP web service, using a server token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/authenticating-through-web-views)*