# Formatting data for blocking and identity information

**Framework**: SMS and Call Reporting

Set up your PIR payload for call blocking and identity information.

#### Overview

With Live Caller ID Lookup, when a device receives an incoming call, the system reaches out to a third-party service to fetch private information retrieval (PIR) data from your server. You need to format that data so the system can make the following requests:

- A blocking information request
- An identity information request

For more information, see the [`Swift homomorphic encryption library`](https://developer.apple.comhttps://github.com/apple/swift-homomorphic-encryption).

##### Block a Caller

The blocking information request is a single byte with two defined values:

##### Identify Caller Information

The identity request displays caller information on the device. This information is a serialized protocol buffer message of type `CallIdentity`. The following example shows the response formatting for an identity request:

```c
syntax = "proto3";

// The image format.
enum ImageFormat {
  // The unspecified format.
  IMAGE_FORMAT_UNSPECIFIED = 0;
  // The High Efficiency Image File Format (HEIF/HEIC).
  IMAGE_FORMAT_HEIC = 1;
}

// The identity category.
// The system might show identity information differently based on the category. 
enum IdentityCategory {
  IDENTITY_CATEGORY_UNSPECIFIED = 0;
  IDENTITY_CATEGORY_PERSON = 1;
  IDENTITY_CATEGORY_BUSINESS = 2;
}

// The icon.
message Icon {
  // The image format for the icon.
  ImageFormat format = 1;
  // The encoded image in the specified format.
  bytes image = 2;
}

// The caller identity.
message CallIdentity {
  // The identity information.
  string name = 1;
  // The icon that displays the identity.
  Icon icon = 2;
  // The cache expiration in minutes.
  // The system reuses this response for the specified minutes before requesting it again.
  uint32 cache_expiry_minutes = 3;
  // The identity category.
  IdentityCategory category = 4;
}
```

## See Also

- [Understanding how Live Caller ID Lookup preserves privacy](understanding-how-live-caller-id-lookup-preserves-privacy.md)
  Use Live Caller ID Lookup to protect user privacy by hiding the client’s IP address, using anonymous authentication, and hiding the incoming phone number.
- [Setting up the HTTP endpoints for Live Caller ID Lookup](setting-up-the-http-endpoints-for-live-caller-id-lookup.md)
  Connect the on-device system to your server.
- [Getting up-to-date calling and blocking information for your app](getting-up-to-date-calling-and-blocking-information-for-your-app.md)
  Implement the Live Caller ID Lookup app extension to provide call-blocking and identity services.
- [protocol LiveCallerIDLookupProtocol](livecalleridlookupprotocol.md)
  Information the system uses to query the app extension for context.
- [protocol LiveCallerIDLookupExtensionConfiguration](livecalleridlookupextensionconfiguration.md)
  An object that allows the system to query the app extension.
- [struct LiveCallerIDLookupExtensionContext](livecalleridlookupextensioncontext.md)
  The information the system uses for configuration.
- [enum CallLookupExtensionStatus](calllookupextensionstatus.md)
  Returns a value with the current state of the app extension.
- [class LiveCallerIDLookupManager](livecalleridlookupmanager.md)
  The entry point that provides access to a collection of functions that help manage the state of the Live Caller ID Lookup app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/formatting-data-for-blocking-and-identity-information)*