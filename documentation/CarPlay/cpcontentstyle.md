# CPContentStyle

**Framework**: CarPlay  
**Kind**: struct  
**Role**: Structure

The types of content style that the vehicle allows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct CPContentStyle
```

```c
enum CPContentStyle : NSUInteger;
```

## Overview

The vehicle selects the content style according to the ambient light level. Your navigation app can use this value to determine the most appropriate style of map content to draw in its base view. The content style is independent of the user interface style, which controls light and dark mode.

You don’t create instances of `CPContentStyle`. Instead, the session configuration provides the current content style, and it notifies its delegate of any changes. See [`CPSessionConfiguration`](./cpsessionconfiguration.md) for more information.

## Topics

### Getting the content styles
- [static var dark: CPContentStyle](./cpcontentstyle/dark.md)
- [static var light: CPContentStyle](./cpcontentstyle/light.md)
### Creating a content style
- [init(rawValue: UInt)](./cpcontentstyle/init%28rawvalue%29.md)

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
- [struct CPLimitableUserInterface](./cplimitableuserinterface.md)
  The types of interfaces to which a vehicle can limit access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontentstyle)*