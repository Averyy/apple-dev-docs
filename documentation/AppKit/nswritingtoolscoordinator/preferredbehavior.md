# preferredBehavior

**Framework**: AppKit  
**Kind**: property

The level of Writing Tools support you want the system to provide for your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@MainActor
var preferredBehavior: NSWritingToolsBehavior { get set }
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)

#### Discussion

Use this property to request an inline or panel-based experience, or to disable Writing Tools for your view altogether. The default value of this property is [`NSWritingToolsBehavior.default`](nswritingtoolsbehavior/default.md).

## See Also

- [var behavior: NSWritingToolsBehavior](nswritingtoolscoordinator/behavior.md)
  The actual level of Writing Tools support the system provides for your view.
- [var preferredResultOptions: NSWritingToolsResultOptions](nswritingtoolscoordinator/preferredresultoptions.md)
  The type of content you allow Writing Tools to generate for your custom text view.
- [var resultOptions: NSWritingToolsResultOptions](nswritingtoolscoordinator/resultoptions.md)
  The type of content the system generates for your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/preferredbehavior)*