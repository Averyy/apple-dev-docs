# NSLayoutManager.TypesetterBehavior.latestBehavior

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The current typesetter behavior in the current operating system.

**Availability**:
- macOS

## Declaration

```swift
case latestBehavior
```

```c
NSTypesetterLatestBehavior
```

## Discussion

For OS X v10.2, this behavior is identical to `NSTypesetterBehavior_10_2`. If you use this behavior setting, you cannot necessarily rely on line width and height metrics remaining the same across different versions of macOS.

## See Also

### Behaviors
- [NSLayoutManager.TypesetterBehavior.originalBehavior](./originalbehavior.md)
  The original typesetter behavior, as shipped with macOS 10.1 and earlier.
- [NSLayoutManager.TypesetterBehavior.behavior_10_2_WithCompatibility](./behavior_10_2_withcompatibility.md)
  The macOS 10.2 typesetting behavior that is still compatible with the original typesetter behavior.
- [NSLayoutManager.TypesetterBehavior.behavior_10_2](./behavior_10_2.md)
  The typesetter behavior introduced in macOS 10.2.
- [NSLayoutManager.TypesetterBehavior.behavior_10_3](./behavior_10_3.md)
  The typesetter behavior introduced in macOS 10.3.
- [NSLayoutManager.TypesetterBehavior.behavior_10_4](./behavior_10_4.md)
  The typesetter behavior introduced in macOS 10.4.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/typesetterbehavior-swift.enum/latestbehavior)*