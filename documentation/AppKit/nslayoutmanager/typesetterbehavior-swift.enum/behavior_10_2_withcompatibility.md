# NSLayoutManager.TypesetterBehavior.behavior_10_2_WithCompatibility

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The macOS 10.2 typesetting behavior that is still compatible with the original typesetter behavior.

**Availability**:
- macOS

## Declaration

```swift
case behavior_10_2_WithCompatibility
```

```c
NSTypesetterBehavior_10_2_WithCompatibility
```

## Discussion

The typesetting behavior is the same as `NSTypesetterBehavior_10_2`, but using line widths and height metric calculations that are the same as with `NSTypesetterOriginalBehavior`.

## See Also

### Behaviors
- [NSLayoutManager.TypesetterBehavior.latestBehavior](./latestbehavior.md)
  The current typesetter behavior in the current operating system.
- [NSLayoutManager.TypesetterBehavior.originalBehavior](./originalbehavior.md)
  The original typesetter behavior, as shipped with macOS 10.1 and earlier.
- [NSLayoutManager.TypesetterBehavior.behavior_10_2](./behavior_10_2.md)
  The typesetter behavior introduced in macOS 10.2.
- [NSLayoutManager.TypesetterBehavior.behavior_10_3](./behavior_10_3.md)
  The typesetter behavior introduced in macOS 10.3.
- [NSLayoutManager.TypesetterBehavior.behavior_10_4](./behavior_10_4.md)
  The typesetter behavior introduced in macOS 10.4.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/typesetterbehavior-swift.enum/behavior_10_2_withcompatibility)*