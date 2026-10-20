# NSSegmentedControl.Distribution.fillEqually

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Dynamically sized segments will be sized to fill the available space, and kept the same size as each other.

**Availability**:
- macOS 10.13+

## Declaration

```swift
case fillEqually
```

```c
NSSegmentDistributionFillEqually
```

## See Also

### Distribution Options
- [NSSegmentedControl.Distribution.fit](./fit.md)
  Dynamically sized segments will be sized to fit their contents, any remaining space will be left blank. This style is equivalent to the way segments were distributed on older systems.
- [NSSegmentedControl.Distribution.fill](./fill.md)
  Dynamically sized segments will be sized to fill the available space, with extra space being distributed equally among them. Default value.
- [NSSegmentedControl.Distribution.fillProportionally](./fillproportionally.md)
  Dynamically sized segments will be sized to fill the available space, and kept proportional to their fitting size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/distribution/fillequally)*