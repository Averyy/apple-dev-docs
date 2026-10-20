# SFContentBlockerManager

**Framework**: Safari Services  
**Kind**: class  
**Role**: Class

A class that your app uses to interact with a content blocker extension.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.4+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
class SFContentBlockerManager
```

```objc
@interface SFContentBlockerManager : NSObject
```

#### Overview

Use this class to determine the state of your content blocker and reload the content-blocking rules used by Safari.

## Topics

### Acting Based on the State of Your Content Blocker
- [class func getStateOfContentBlocker(withIdentifier: String, completionHandler: (SFContentBlockerState?, (any Error)?) -> Void)](./sfcontentblockermanager/getstateofcontentblocker%28withidentifier,completionhandler%29.md)
  Determines the state of your content blocker.
### Reloading Your Content-Blocking Rules
- [class func reloadContentBlocker(withIdentifier: String, completionHandler: (((any Error)?) -> Void)?)](./sfcontentblockermanager/reloadcontentblocker%28withidentifier,completionhandler%29.md)
  Tells Safari to reload the specified extension’s content-blocking rules.

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

## See Also

### Content blockers
- [Creating a content blocker](./creating-a-content-blocker.md)
  Create a content blocker for Safari in Xcode.
- [class SFContentBlockerState](./sfcontentblockerstate.md)
  The state of a content blocker extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager)*