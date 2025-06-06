# forSession

**Framework**: Core Graphics  
**Kind**: property

Changes persist for the lifetime of the current login session. After the current session terminates, the displays revert to the last saved permanent configuration.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
static var forSession: CGConfigureOption { get }
```

## See Also

- [static var forAppOnly: CGConfigureOption](cgconfigureoption/forapponly.md)
  Changes persist for the lifetime of the current application. After the application terminates, the display configuration settings revert to the current login session.
- [static var permanently: CGConfigureOption](cgconfigureoption/permanently.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgconfigureoption/forsession)*