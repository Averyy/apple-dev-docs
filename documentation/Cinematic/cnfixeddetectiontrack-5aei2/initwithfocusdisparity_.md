# initWithFocusDisparity:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Creates a detection track with fixed focus at the given disparity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (instancetype) initWithFocusDisparity:(float) focusDisparity;
```

## Parameters

- `focusDisparity`: The disparity to use in order to focus on the object (use the static `disparity` method to compute if unknown).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnfixeddetectiontrack-5aei2/initwithfocusdisparity:)*