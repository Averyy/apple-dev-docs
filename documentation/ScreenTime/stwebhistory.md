# STWebHistory

**Framework**: Screen Time  
**Kind**: class  
**Role**: Class

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

```objc
@interface STWebHistory : NSObject
```

## Overview

This class provides an easy way for you to delete web history, including:

- All history
- History associated to a specific URL
- History during a specific time interval

## Topics

### Initializers
- [init(bundleIdentifier: String) throws](./stwebhistory/init%28bundleidentifier%29.md)
  Creates a web history instance to delete web-usage data associated to the bundle identifier you specify.
- [init(bundleIdentifier: String, profileIdentifier: STWebHistory.ProfileIdentifier?) throws](./stwebhistory/init%28bundleidentifier,profileidentifier%29.md)
  Creates a web history instance to delete web-usage data associated to the bundle identifier and profile identifier you specify.
- [init(profileIdentifier: STWebHistory.ProfileIdentifier?)](./stwebhistory/init%28profileidentifier%29.md)
  Creates a web history instance to delete web-usage data associated to the profile identifier you specify.
### Instance methods
- [func deleteAllHistory()](./stwebhistory/deleteallhistory%28%29.md)
  Deletes all web history associated with the bundle identifier you specified during initialization.
- [func deleteHistory(during: DateInterval)](./stwebhistory/deletehistory%28during%29.md)
  Deletes web history that occurred during the date interval you specify.
- [func deleteHistory(for: URL)](./stwebhistory/deletehistory%28for%29.md)
  Deletes all the web history for the URL you specify.
### Structures
- [STWebHistory.ProfileIdentifier](./stwebhistory/profileidentifier.md)
  An identifier representing a web history profile.
### Instance Methods
- [func fetchAllHistory(completionHandler: (Set<URL>?, (any Error)?) -> Void)](./stwebhistory/fetchallhistory%28completionhandler%29.md)
  Fetches all web history associated with the bundle identifier and profile identifier you specified during initialization.
- [func fetchHistory(during: DateInterval, completionHandler: (Set<URL>?, (any Error)?) -> Void)](./stwebhistory/fetchhistory%28during,completionhandler%29.md)
  Fetches web history that occurred during the date interval you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebhistory)*