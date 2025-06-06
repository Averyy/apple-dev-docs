# saveOptions

**Framework**: Foundation  
**Kind**: property

Returns a constant indicating how to deal with closing any modified documents.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var saveOptions: NSSaveOptions { get }
```

#### Return Value

A constant indicating how to deal with closing any modified documents. The default value returned is `NSSaveOptionsAsk`. See “Constants” in [`NSCloseCommand`](nsclosecommand.md) for a list of possible return values.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsquitcommand/saveoptions)*