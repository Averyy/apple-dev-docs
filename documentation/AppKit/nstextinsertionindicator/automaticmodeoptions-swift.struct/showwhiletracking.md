# showWhileTracking

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Specifies whether the insertion indicator shows during a tracking loop.

**Availability**:
- macOS 14.0+

## Declaration

```swift
static var showWhileTracking: NSTextInsertionIndicator.AutomaticModeOptions { get }
```

```c
NSTextInsertionIndicatorAutomaticModeOptionsShowWhileTracking
```

## Mentions

- [Adopting the system text cursor in custom text views](../../adopting-the-system-text-cursor-in-custom-text-views.md)

## Discussion

When set, the insertion indicator hides during an [`NSEventTrackingRunLoopMode`](../../nseventtrackingrunloopmode.md) such as while actively scrolling a view.

## See Also

### Configuring automatic mode options
- [static var showEffectsView: NSTextInsertionIndicator.AutomaticModeOptions](./showeffectsview.md)
  Specifies whether a trailing glow displays during dictation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinsertionindicator/automaticmodeoptions-swift.struct/showwhiletracking)*