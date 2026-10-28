# FamilyActivitySelection

**Framework**: Family Controls  
**Kind**: struct  
**Role**: Structure

A collection of applications, categories, and web domains selected by the user.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
struct FamilyActivitySelection
```

## Overview

To protect the user’s privacy, `FamilyActivitySelection` holds opaque values that represent categories, applications, and web domains selected by the user.

You can then pass these opaque values to instances and methods from the [Managed Settings](../ManagedSettings/ManagedSettings.md) and [Device Activity](../DeviceActivity/DeviceActivity.md) frameworks to set up and manage parental controls.

> ❗ **Important**: If a user, parent, or guardian revokes authorization of your app, any tokens that [`FamilyActivitySelection`](./familyactivityselection.md) provided while your app was authorized are voided.

For more information on prompting the user to select items, see [`FamilyActivityPicker`](./familyactivitypicker.md).

## Topics

### Accessing selected categories
- [var categories: Set<ActivityCategory>](./familyactivityselection/categories.md)
  A set of category instances selected by the user.
- [var categoryTokens: Set<ActivityCategoryToken>](./familyactivityselection/categorytokens.md)
  Tokens that represent categories selected by the user.
- [init(includeEntireCategory: Bool)](./familyactivityselection/init%28includeentirecategory%29.md)
  Creates a new activity selection instance.
### Accessing selected applications
- [var applications: Set<Application>](./familyactivityselection/applications.md)
  A set of application instances selected by the user.
- [var applicationTokens: Set<ApplicationToken>](./familyactivityselection/applicationtokens.md)
  Tokens that represent applications selected by the user.
### Accessing selected web domains
- [var webDomains: Set<WebDomain>](./familyactivityselection/webdomains.md)
  A set of web domain instances selected by the user.
- [var webDomainTokens: Set<WebDomainToken>](./familyactivityselection/webdomaintokens.md)
  Tokens that represent web domains selected by the user.
### Creating activity selections
- [init()](./familyactivityselection/init%28%29.md)
  Creates a new activity selection instance.
### Comparing activity selections
- [let includeEntireCategory: Bool](./familyactivityselection/includeentirecategory.md)
  A Boolean value that indicates whether the selection should include applications and web domains from the selected categories.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)

## See Also

### Activity selections
- [struct FamilyActivityPicker](./familyactivitypicker.md)
  A view in which users specify applications, web domains, and categories without revealing their choices to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityselection)*