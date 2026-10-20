# ASPresentationAnchor

**Framework**: Authentication Services  
**Kind**: typealias  
**Role**: Type Alias

A platform-specific type that indicates the kind of user interface element to use as a presentation anchor.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
typealias ASPresentationAnchor = UIWindow
```

*macOS*

```swift
typealias ASPresentationAnchor = NSWindow
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```c
typedef UIWindow * ASPresentationAnchor;
```

*macOS*

```c
typedef NSWindow * ASPresentationAnchor;
```

## See Also

### Creating an export manager
- [convenience init(presentationAnchor: ASPresentationAnchor)](./ascredentialexportmanager/init%28presentationanchor%29-56ki6.md)
  Creates an export manager, anchored by the given AppKit window.
- [convenience init(presentationAnchor: ASPresentationAnchor)](./ascredentialexportmanager/init%28presentationanchor%29-904gt.md)
  Creates an export manager, anchored by the given UIKit window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspresentationanchor)*