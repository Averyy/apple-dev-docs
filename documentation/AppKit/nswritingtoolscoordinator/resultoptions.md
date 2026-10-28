# resultOptions

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The type of content the system generates for your custom text view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
var resultOptions: NSWritingToolsResultOptions { get }
```

```objc
@property (readonly) NSWritingToolsResultOptions resultOptions;
```

## Discussion

This property contains the set of options that Writing Tools outputs for your view. Writing Tools takes the value in the [`preferredResultOptions`](./preferredresultoptions.md) property into consideration when determining this value.

## See Also

### Configuring the experience
- [var preferredBehavior: NSWritingToolsBehavior](./preferredbehavior.md)
  The level of Writing Tools support you want the system to provide for your view.
- [var behavior: NSWritingToolsBehavior](./behavior.md)
  The actual level of Writing Tools support the system provides for your view.
- [var preferredResultOptions: NSWritingToolsResultOptions](./preferredresultoptions.md)
  The type of content you allow Writing Tools to generate for your custom text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/resultoptions)*