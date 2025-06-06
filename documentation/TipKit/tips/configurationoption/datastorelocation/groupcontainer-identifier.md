# groupContainer(identifier:)

**Framework**: TipKit  
**Kind**: method

DatastoreLocation for persisting tips in a group container.

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
static func groupContainer(identifier: String) throws -> Tips.ConfigurationOption.DatastoreLocation
```

## Parameters

- `identifier`: A string that names the group whose shared directory you want to obtain. This input should exactly match one of the strings in the app’s App Groups Entitlement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/configurationoption/datastorelocation/groupcontainer(identifier:))*