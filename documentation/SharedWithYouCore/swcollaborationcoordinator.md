# SWCollaborationCoordinator

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

An object that contains the shared collaboration coordinator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWCollaborationCoordinator
```

```objc
@interface SWCollaborationCoordinator : NSObject
```

## Overview

`SWCollaborationCoordinator` is a singleton, meaning there’s a global shared instance. The singleton invokes its [`actionHandler`](./swcollaborationcoordinator/actionhandler.md) delegate to coordinate new collaborations and updates to existing collaborations.

Register the delegate soon after launch and handle actions immediately to avoid timeouts. Here’s how to set up the collaboration coordinator after your app finishes launching:

1. Access the singleton coordinator instance through the shared property.
2. Then, in the app delegate’s [`application(_:didFinishLaunchingWithOptions:)`](../UIKit/uiapplicationdelegate/application%28_,didfinishlaunchingwithoptions%29.md) method, set the `actionHandler` property to an object that conforms to the [`SWCollaborationActionHandler`](./swcollaborationactionhandler.md) protocol.

> **Related Sessions from WWDC22**:  Session 10093: [Integrate your custom collaboration app with Messages](https://developer.apple.com/videos/play/wwdc2022/10093/)

## Topics

### Accessing coordinator attributes
- [class var shared: SWCollaborationCoordinator](./swcollaborationcoordinator/shared.md)
  The shared collaboration coordinator.
- [var actionHandler: (any SWCollaborationActionHandler)?](./swcollaborationcoordinator/actionhandler.md)
  The collaboration action handler.

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

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationcoordinator)*