# CPLimitableUserInterface

**Framework**: CarPlay  
**Kind**: struct  
**Role**: Structure

The types of interfaces to which a vehicle can limit access.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct CPLimitableUserInterface
```

```c
enum CPLimitableUserInterface : NSUInteger;
```

## Overview

A vehicle might limit access to specific features for safety reasons or to support vehicle constraints. For example, a vehicle might limit access to virtual keyboards when the vehicle is in motion. A [`CPSessionConfiguration`](./cpsessionconfiguration.md) object reports these limitations in its [`limitedUserInterfaces`](./cpsessionconfiguration/limiteduserinterfaces.md) property, which stores a bitmask of the available constants.

## Topics

### Getting the user interface limits
- [static var keyboard: CPLimitableUserInterface](./cplimitableuserinterface/keyboard.md)
  A type that indicates the vehicle limits the display of virtual keyboards.
- [static var lists: CPLimitableUserInterface](./cplimitableuserinterface/lists.md)
  A type that indicates the vehicle limits the number of items you can display in lists.
### Creating a limit value
- [init(rawValue: UInt)](./cplimitableuserinterface/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Getting the configuration details
- [var contentStyle: CPContentStyle](./cpsessionconfiguration/contentstyle.md)
  The preferred interface style for your app’s content.
- [var limitedUserInterfaces: CPLimitableUserInterface](./cpsessionconfiguration/limiteduserinterfaces.md)
  A bitmask of the interface restrictions that currently apply to your app.
- [var supportsVideoPlayback: Bool](./cpsessionconfiguration/supportsvideoplayback.md)
  A Boolean value that indicates whether CarPlay supports playing video content.
- [struct CPContentStyle](./cpcontentstyle.md)
  The types of content style that the vehicle allows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplimitableuserinterface)*