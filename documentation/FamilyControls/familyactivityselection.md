# FamilyActivitySelection

**Framework**: FamilyControls  
**Kind**: struct

A collection of applications, categories, and web domains selected by the user.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct FamilyActivitySelection
```

#### Overview

To protect the user’s privacy, `FamilyActivitySelection` holds opaque values that represent categories, applications, and web domains selected by the user.

You can then pass these opaque values to instances and methods from the [`ManagedSettings`](https://developer.apple.com/documentation/ManagedSettings) and [`DeviceActivity`](https://developer.apple.com/documentation/DeviceActivity) frameworks to set up and manage parental controls.

> ❗ **Important**: If a user, parent, or guardian revokes authorization of your app, any tokens that [`FamilyActivitySelection`](familyactivityselection.md) provided while your app was authorized are voided.

If a user, parent, or guardian revokes authorization of your app, any tokens that [`FamilyActivitySelection`](familyactivityselection.md) provided while your app was authorized are voided.

For more information on prompting the user to select items, see [`FamilyActivityPicker`](familyactivitypicker.md).

## Topics

### Accessing Selected Categories
- [var categories: Set<ActivityCategory>](familyactivityselection/categories.md)
  A set of category instances selected by the user.
- [var categoryTokens: Set<ActivityCategoryToken>](familyactivityselection/categorytokens.md)
  Tokens that represent categories selected by the user.
### Accessing Selected Applications
- [var applications: Set<Application>](familyactivityselection/applications.md)
  A set of application instances selected by the user.
- [var applicationTokens: Set<ApplicationToken>](familyactivityselection/applicationtokens.md)
  Tokens that represent applications selected by the user.
### Accessing Selected Web Domains
- [var webDomains: Set<WebDomain>](familyactivityselection/webdomains.md)
  A set of web domain instances selected by the user.
- [var webDomainTokens: Set<WebDomainToken>](familyactivityselection/webdomaintokens.md)
  Tokens that represent web domains selected by the user.
### Creating Activity Selections
- [init()](familyactivityselection/init.md)
  Creates a new activity selection instance.
- [init(from: any Decoder) throws](familyactivityselection/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Encoding Activity Selections
- [func encode(to: any Encoder) throws](familyactivityselection/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing Activity Selections
- [static func == (FamilyActivitySelection, FamilyActivitySelection) -> Bool](familyactivityselection/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](familyactivityselection/!=(_:_:).md)
  Returns a Boolean value that indicates whether two activity selections aren’t equal.
### Initializers
- [init(includeEntireCategory: Bool)](familyactivityselection/init(includeentirecategory:).md)
  Creates a new activity selection instance.
### Instance Properties
- [let includeEntireCategory: Bool](familyactivityselection/includeentirecategory.md)
  A Boolean value that indicates whether the selection should include applications and web domains from the selected categories.
### Default Implementations
- [Equatable Implementations](familyactivityselection/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct FamilyActivityPicker](familyactivitypicker.md)
  A view in which users specify applications, web domains, and categories without revealing their choices to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityselection)*