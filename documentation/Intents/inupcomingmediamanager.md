# INUpcomingMediaManager

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The manager object you use to suggest media to the user.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INUpcomingMediaManager
```

```objc
@interface INUpcomingMediaManager : NSObject
```

## Overview

Use this class to provide Siri a list of media intents for content that the user hasn’t listened to or watched, but might be interested in. For example, a podcast app may provide the latest episodes of the podcast, or a video app may provide the most recent episodes of TV shows, or suggest new movies.

## Topics

### Getting the Upcoming-Media Manager
- [class var shared: INUpcomingMediaManager](./inupcomingmediamanager/shared.md)
  The shared upcoming media manager.
### Suggesting Media Intent Shortcuts
- [func setSuggestedMediaIntents(NSOrderedSet)](./inupcomingmediamanager/setsuggestedmediaintents%28_%29.md)
  Provides Siri with a list of media intents to suggest to the user.
### Setting Prediction Modes
- [func setPredictionMode(INUpcomingMediaPredictionMode, for: INMediaItemType)](./inupcomingmediamanager/setpredictionmode%28_,for%29.md)
  Suggests how Siri should predict media intent shortcuts.
- [enum INUpcomingMediaPredictionMode](./inupcomingmediapredictionmode.md)
  Prediction modes for upcoming media intent shortcuts.

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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupcomingmediamanager)*