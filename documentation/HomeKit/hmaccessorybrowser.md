# HMAccessoryBrowser

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

A network browser you can use to discover new accessories in a home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
class HMAccessoryBrowser
```

```objc
@interface HMAccessoryBrowser : NSObject
```

## Overview

Discovering new network accessories is an expensive operation in terms of time and power. Only start searching for new accessories when the user explicitly asks to do so, and stop searching as soon as the user has chosen the new accessories to add to their home.

> ❗ **Important**:  To enable a consistent user experience across HomeKit enabled apps, use either the [`addAndSetupAccessories(completionHandler:)`](./hmhome/addandsetupaccessories%28completionhandler%29.md) or the [`addAndSetupAccessories(with:completionHandler:)`](./hmhome/addandsetupaccessories%28with,completionhandler%29.md) method of the [`HMHome`](./hmhome.md) class instead of an accessory browser. These calls manage all the details of the accessory search process for you.

## Topics

### Discovering accessories
- [var discoveredAccessories: [HMAccessory]](./hmaccessorybrowser/discoveredaccessories.md)
  An array of accessories discovered during a search.
- [func startSearchingForNewAccessories()](./hmaccessorybrowser/startsearchingfornewaccessories%28%29.md)
  Starts searching for accessories not yet associated with a home.
- [func stopSearchingForNewAccessories()](./hmaccessorybrowser/stopsearchingfornewaccessories%28%29.md)
  Stops searching for new accessories.
### Tracking the addition or removal of accessories
- [var delegate: (any HMAccessoryBrowserDelegate)?](./hmaccessorybrowser/delegate.md)
  A delegate that receives updates on the discovered accessories.
- [protocol HMAccessoryBrowserDelegate](./hmaccessorybrowserdelegate.md)
  An interface used to notify an accessory browser delegate of new accessories.
### Initializers
- [init()](./hmaccessorybrowser/init%28%29.md)

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorybrowser)*