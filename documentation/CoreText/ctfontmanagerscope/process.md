# CTFontManagerScope.process

**Framework**: Core Text  
**Kind**: case

The font is available to the current process for the duration of the process unless directly unregistered.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case process
```

## See Also

- [CTFontManagerScope.none](ctfontmanagerscope/none.md)
  No scope is defined.
- [CTFontManagerScope.persistent](ctfontmanagerscope/persistent.md)
  The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.
- [CTFontManagerScope.session](ctfontmanagerscope/session.md)
  The font is available to the current user session but won’t be available in subsequent sessions.
- [static var user: CTFontManagerScope](ctfontmanagerscope/user.md)
  The font is available to all processes for the current user session and will be available in subsequent sessions unless unregistered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagerscope/process)*