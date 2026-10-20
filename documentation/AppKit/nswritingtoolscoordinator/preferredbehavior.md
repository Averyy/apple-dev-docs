# preferredBehavior

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The level of Writing Tools support you want the system to provide for your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
var preferredBehavior: NSWritingToolsBehavior { get set }
```

```objc
@property NSWritingToolsBehavior preferredBehavior;
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](../adding-writing-tools-support-to-a-custom-nsview.md)

#### Discussion

Use this property to request an inline or panel-based experience, or to disable Writing Tools for your view altogether. The default value of this property is [`NSWritingToolsBehavior.default`](../nswritingtoolsbehavior/default.md).

## See Also

### Configuring the experience
- [var behavior: NSWritingToolsBehavior](./behavior.md)
  The actual level of Writing Tools support the system provides for your view.
- [var preferredResultOptions: NSWritingToolsResultOptions](./preferredresultoptions.md)
  The type of content you allow Writing Tools to generate for your custom text view.
- [var resultOptions: NSWritingToolsResultOptions](./resultoptions.md)
  The type of content the system generates for your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/preferredbehavior)*