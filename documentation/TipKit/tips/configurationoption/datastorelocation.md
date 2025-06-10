# DatastoreLocation

**Framework**: TipKit  
**Kind**: struct

A type for specifying a custom location for your tips datastore.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct DatastoreLocation
```

#### Overview

For more information on datastore location, see [`datastoreLocation(_:)`](tips/configurationoption/datastorelocation(_:).md).

## Topics

### Type Properties
- [static var applicationDefault: Tips.ConfigurationOption.DatastoreLocation](tips/configurationoption/datastorelocation/applicationdefault.md)
  The default location for persisting tips, which is generally your application’s support directory.
### Type Methods
- [static func groupContainer(identifier: String) throws -> Tips.ConfigurationOption.DatastoreLocation](tips/configurationoption/datastorelocation/groupcontainer(identifier:).md)
  DatastoreLocation for persisting tips in a group container.
- [static func url(URL) -> Tips.ConfigurationOption.DatastoreLocation](tips/configurationoption/datastorelocation/url(_:).md)
  DatastoreLocation for persisting tips at a custom URL.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/configurationoption/datastorelocation)*