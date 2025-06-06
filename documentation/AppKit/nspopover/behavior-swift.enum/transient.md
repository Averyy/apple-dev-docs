# NSPopover.Behavior.transient

**Framework**: AppKit  
**Kind**: case

The system will close the popover when the user interacts with a user interface element outside the popover.

**Availability**:
- macOS ?+

## Declaration

```swift
case transient
```

#### Discussion

Note that interacting with menus or panels that become key only when needed will not cause a transient popover to close. The exact interactions that will cause transient popovers to close are not specified.

## See Also

- [NSPopover.Behavior.applicationDefined](nspopover/behavior-swift.enum/applicationdefined.md)
  Your application assumes responsibility for closing the popover.
- [NSPopover.Behavior.semitransient](nspopover/behavior-swift.enum/semitransient.md)
  The system will close the popover when the user interacts with user interface elements in the window containing the popover’s positioning view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/behavior-swift.enum/transient)*