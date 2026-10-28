# Blueprint.Attributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a Blueprint resource.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
object Blueprint.Attributes
```

## Overview

> **Note**: When additional attributes are added by Apple, they appear automatically, without requiring a newer version of the API.

## Properties

- `name` (string): The display name of the Blueprint.
- `description` (string): A description of the Blueprint.
- `status` (BlueprintStatus): The current status of the Blueprint. See [`BlueprintStatus`](../blueprintstatus.md) for possible values.
- `appLicenseDeficient` (boolean): Indicates whether the Blueprint has insufficient app licenses for all assigned members.
- `createdDateTime` (date-time): The date and time that the Blueprint was created.
- `updatedDateTime` (date-time): The date and time that the Blueprint was last updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/blueprint/attributes-data.dictionary)*