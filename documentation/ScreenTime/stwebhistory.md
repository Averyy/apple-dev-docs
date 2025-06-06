# STWebHistory

**Framework**: Screen Time  
**Kind**: class

The object you use to delete web-usage data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
class STWebHistory
```

#### Overview

This class provides an easy way for you to delete web history, including:

- All history
- History associated to a specific URL
- History during a specific time interval

## Topics

### Initializers
- [init(bundleIdentifier: String) throws](stwebhistory/init(bundleidentifier:).md)
  Creates a web history instance to delete web-usage data associated to the bundle identifier you specify.
- [init(bundleIdentifier: String, profileIdentifier: STWebHistory.ProfileIdentifier?) throws](stwebhistory/init(bundleidentifier:profileidentifier:).md)
  Creates a web history instance to delete web-usage data associated to the bundle identifier and profile identifier you specify.
- [init(profileIdentifier: STWebHistory.ProfileIdentifier?)](stwebhistory/init(profileidentifier:).md)
  Creates a web history instance to delete web-usage data associated to the profile identifier you specify.
### Instance methods
- [func deleteAllHistory()](stwebhistory/deleteallhistory.md)
  Deletes all web history associated with the bundle identifier you specified during initialization.
- [func deleteHistory(during: DateInterval)](stwebhistory/deletehistory(during:).md)
  Deletes web history that occurred during the date interval you specify.
- [func deleteHistory(for: URL)](stwebhistory/deletehistory(for:).md)
  Deletes all the web history for the URL you specify.
### Structures
- [STWebHistory.ProfileIdentifier](stwebhistory/profileidentifier.md)
  An identifier representing a web history profile.
### Instance Methods
- [func fetchAllHistory(completionHandler: (Set<URL>?, (any Error)?) -> Void)](stwebhistory/fetchallhistory(completionhandler:).md)
  Fetches all web history associated with the bundle identifier and profile identifier you specified during initialization.
- [func fetchHistory(during: DateInterval, completionHandler: (Set<URL>?, (any Error)?) -> Void)](stwebhistory/fetchhistory(during:completionhandler:).md)
  Fetches web history that occurred during the date interval you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebhistory)*