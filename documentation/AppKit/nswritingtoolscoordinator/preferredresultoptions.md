# preferredResultOptions

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The type of content you allow Writing Tools to generate for your custom text view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
var preferredResultOptions: NSWritingToolsResultOptions { get set }
```

```objc
@property NSWritingToolsResultOptions preferredResultOptions;
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](../adding-writing-tools-support-to-a-custom-nsview.md)

## Discussion

Writing Tools can create plain text or rich text, and it can format text using lists or tables as needed. If your view doesn’t support specific types of content, specify the types you do support in this property. The default value of this property is `NSWritingToolsResultOptions/default`, which lets the system determine the type of content to generate.

## See Also

### Configuring the experience
- [var preferredBehavior: NSWritingToolsBehavior](./preferredbehavior.md)
  The level of Writing Tools support you want the system to provide for your view.
- [var behavior: NSWritingToolsBehavior](./behavior.md)
  The actual level of Writing Tools support the system provides for your view.
- [var resultOptions: NSWritingToolsResultOptions](./resultoptions.md)
  The type of content the system generates for your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/preferredresultoptions)*