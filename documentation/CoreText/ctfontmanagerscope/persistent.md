# CTFontManagerScope.persistent

**Framework**: Core Text  
**Kind**: case  
**Role**: Case

The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case persistent
```

```c
kCTFontManagerScopePersistent
```

## See Also

### Constants
- [CTFontManagerScope.none](./none.md)
  No scope is defined.
- [CTFontManagerScope.process](./process.md)
  The font is available to the current process for the duration of the process unless directly unregistered.
- [CTFontManagerScope.session](./session.md)
  The font is available to the current user session but won’t be available in subsequent sessions.
- [static var user: CTFontManagerScope](./user.md)
  The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagerscope/persistent)*