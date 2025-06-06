# NSPopover.Behavior.semitransient

**Framework**: AppKit  
**Kind**: case

The system will close the popover when the user interacts with user interface elements in the window containing the popover’s positioning view.

**Availability**:
- macOS ?+

## Declaration

```swift
case semitransient
```

#### Discussion

Semi-transient popovers cannot be shown relative to views in other popovers, nor can they be shown relative to views in child windows. The exact interactions that cause semi-transient popovers to close are not specified.

## See Also

- [NSPopover.Behavior.applicationDefined](nspopover/behavior-swift.enum/applicationdefined.md)
  Your application assumes responsibility for closing the popover.
- [NSPopover.Behavior.transient](nspopover/behavior-swift.enum/transient.md)
  The system will close the popover when the user interacts with a user interface element outside the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/behavior-swift.enum/semitransient)*