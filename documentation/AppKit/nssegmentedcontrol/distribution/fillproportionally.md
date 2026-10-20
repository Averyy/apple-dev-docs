# NSSegmentedControl.Distribution.fillProportionally

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Dynamically sized segments will be sized to fill the available space, and kept proportional to their fitting size.

**Availability**:
- macOS 10.13+

## Declaration

```swift
case fillProportionally
```

```c
NSSegmentDistributionFillProportionally
```

## See Also

### Distribution Options
- [NSSegmentedControl.Distribution.fit](./fit.md)
  Dynamically sized segments will be sized to fit their contents, any remaining space will be left blank. This style is equivalent to the way segments were distributed on older systems.
- [NSSegmentedControl.Distribution.fill](./fill.md)
  Dynamically sized segments will be sized to fill the available space, with extra space being distributed equally among them. Default value.
- [NSSegmentedControl.Distribution.fillEqually](./fillequally.md)
  Dynamically sized segments will be sized to fill the available space, and kept the same size as each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/distribution/fillproportionally)*