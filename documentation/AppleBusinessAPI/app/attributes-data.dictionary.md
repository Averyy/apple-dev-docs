# App.Attributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

Attributes that describe an app resource.

**Availability**:
- Apple Business API 2.7+

## Declaration

```
object App.Attributes
```

## Overview

> **Note**: When additional attributes are added by Apple, they appear automatically, without requiring a newer version of the API.

## Properties

- `name` (string): The display name of the app.
- `bundleId` (string): The bundle identifier of the app.
- `websiteUrl` (string): The website URL for the app.
- `version` (string): The current version of the app.
- `supportedOS` ([SupportedOS]): The list of operating systems the app supports. See [`SupportedOS`](../supportedos.md) for possible values.
- `isCustomApp` (boolean): Indicates whether this is a custom B2B app.
- `appStoreUrl` (string): The App Store URL for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/app/attributes-data.dictionary)*