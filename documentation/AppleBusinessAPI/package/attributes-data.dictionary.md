# Package.Attributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a package resource.

**Availability**:
- Apple Business API 2.7+

## Declaration

```
object Package.Attributes
```

## Overview

> **Note**: When additional attributes are added by Apple, they appear automatically, without requiring a newer version of the API.

## Properties

- `name` (string): The display name of the package.
- `url` (string): The HTTPS URL to download the package.
- `hash` (string): The hex string hash of the package file.
- `bundleIds` ([string]): The list of bundle identifiers contained in the package.
- `description` (string): A short description of the package.
- `version` (string): The version string of the package.
- `createdDateTime` (date-time): The date and time that the package was created.
- `updatedDateTime` (date-time): The date and time that the package was last updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/package/attributes-data.dictionary)*