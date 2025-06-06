# resultOptions

**Framework**: AppKit  
**Kind**: property

The type of content the system generates for your custom text view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@MainActor
var resultOptions: NSWritingToolsResultOptions { get }
```

#### Discussion

This property contains the set of options that Writing Tools outputs for your view. Writing Tools takes the value in the [`preferredResultOptions`](nswritingtoolscoordinator/preferredresultoptions.md) property into consideration when determining this value.

## See Also

- [var preferredBehavior: NSWritingToolsBehavior](nswritingtoolscoordinator/preferredbehavior.md)
  The level of Writing Tools support you want the system to provide for your view.
- [var behavior: NSWritingToolsBehavior](nswritingtoolscoordinator/behavior.md)
  The actual level of Writing Tools support the system provides for your view.
- [var preferredResultOptions: NSWritingToolsResultOptions](nswritingtoolscoordinator/preferredresultoptions.md)
  The type of content you allow Writing Tools to generate for your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/resultoptions)*