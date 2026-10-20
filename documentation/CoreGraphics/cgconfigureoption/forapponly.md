# forAppOnly

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

Changes persist for the lifetime of the current application. After the application terminates, the display configuration settings revert to the current login session.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var forAppOnly: CGConfigureOption { get }
```

```c
kCGConfigureForAppOnly
```

## See Also

### Type Properties
- [static var forSession: CGConfigureOption](./forsession.md)
  Changes persist for the lifetime of the current login session. After the current session terminates, the displays revert to the last saved permanent configuration.
- [static var permanently: CGConfigureOption](./permanently.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgconfigureoption/forapponly)*