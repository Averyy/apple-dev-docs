# permanently

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var permanently: CGConfigureOption { get }
```

```c
kCGConfigurePermanently
```

## Discussion

Changes persist in future login sessions by the same user. If the requested changes cannot be supported by the Aqua UI (resolution and pixel depth constraints apply), the settings for the current login session are used instead, and any changes have session scope.

## See Also

### Type Properties
- [static var forAppOnly: CGConfigureOption](./forapponly.md)
  Changes persist for the lifetime of the current application. After the application terminates, the display configuration settings revert to the current login session.
- [static var forSession: CGConfigureOption](./forsession.md)
  Changes persist for the lifetime of the current login session. After the current session terminates, the displays revert to the last saved permanent configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgconfigureoption/permanently)*