# forAppOnly

**Framework**: Core Graphics  
**Kind**: property

Changes persist for the lifetime of the current application. After the application terminates, the display configuration settings revert to the current login session.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
static var forAppOnly: CGConfigureOption { get }
```

## See Also

- [static var forSession: CGConfigureOption](cgconfigureoption/forsession.md)
  Changes persist for the lifetime of the current login session. After the current session terminates, the displays revert to the last saved permanent configuration.
- [static var permanently: CGConfigureOption](cgconfigureoption/permanently.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgconfigureoption/forapponly)*