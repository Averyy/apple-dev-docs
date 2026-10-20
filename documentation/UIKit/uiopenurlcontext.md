# UIOpenURLContext

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A system-provided object that contains the information you need to open a single URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIOpenURLContext
```

```objc
@interface UIOpenURLContext : NSObject
```

#### Overview

UIKit provides a [`UIOpenURLContext`](./uiopenurlcontext.md) object when your app receives a URL to open, such as in your implementation of [`scene(_:openURLContexts:)`](./uiscenedelegate/scene%28_,openurlcontexts%29.md). The object contains the URL itself and any options needed to handle the URL correctly. Don’t create [`UIOpenURLContext`](./uiopenurlcontext.md) objects yourself.

## Topics

### Getting the URL
- [var url: URL](./uiopenurlcontext/url.md)
  The URL to open.
- [var options: UIScene.OpenURLOptions](./uiopenurlcontext/options.md)
  Additional information for determining how to open the URL.
- [UIScene.OpenURLOptions](./uiscene/openurloptions.md)
  Options that UIKit provides when asking your app to open a URL.

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

## See Also

### URL management
- [UIScene.OpenExternalURLOptions](./uiscene/openexternalurloptions.md)
  Options you specify when asking a scene to open a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiopenurlcontext)*