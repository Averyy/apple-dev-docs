# behavior

**Framework**: AppKit  
**Kind**: property

The actual level of Writing Tools support the system provides for your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@MainActor
var behavior: NSWritingToolsBehavior { get }
```

#### Discussion

The system chooses this value based on the device capabilities, and takes the value in the [`preferredBehavior`](nswritingtoolscoordinator/preferredbehavior.md) property into consideration when making the choice. The value in this property is never the default option, and is instead one of the specific options such as [`NSWritingToolsBehavior.none`](nswritingtoolsbehavior/none.md), [`NSWritingToolsBehavior.limited`](nswritingtoolsbehavior/limited.md), or [`NSWritingToolsBehavior.complete`](nswritingtoolsbehavior/complete.md).

## See Also

- [var preferredBehavior: NSWritingToolsBehavior](nswritingtoolscoordinator/preferredbehavior.md)
  The level of Writing Tools support you want the system to provide for your view.
- [var preferredResultOptions: NSWritingToolsResultOptions](nswritingtoolscoordinator/preferredresultoptions.md)
  The type of content you allow Writing Tools to generate for your custom text view.
- [var resultOptions: NSWritingToolsResultOptions](nswritingtoolscoordinator/resultoptions.md)
  The type of content the system generates for your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/behavior)*