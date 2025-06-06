# UIOpenURLContext

**Framework**: UIKit  
**Kind**: class

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

#### Overview

UIKit provides a [`UIOpenURLContext`](uiopenurlcontext.md) object when your app receives a URL to open. The object contains the URL itself and any options needed to handle the URL correctly. Don’t create [`UIOpenURLContext`](uiopenurlcontext.md) objects yourself.

## Topics

### Getting the URL
- [var url: URL](uiopenurlcontext/url.md)
  The URL to open.
- [var options: UIScene.OpenURLOptions](uiopenurlcontext/options.md)
  Additional information for determining how to open the URL.
- [UIScene.OpenURLOptions](uiscene/openurloptions.md)
  Options that UIKit provides when asking your app to open a URL.

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
- [Sendable](../Swift/Sendable.md)

## See Also

- [UIScene.OpenExternalURLOptions](uiscene/openexternalurloptions.md)
  Options you specify when asking a scene to open a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiopenurlcontext)*