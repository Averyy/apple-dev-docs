# throttleBackgroundContents(size:controller:)

**Framework**: Touch Controller  
**Kind**: method  
**Role**: Type Method

The throttle background contents for the specified size.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class func throttleBackgroundContents(size: CGSize, controller: TCTouchController) -> TCControlContents
```

```objc
+ (TCControlContents *) throttleBackgroundContentsOfSize:(CGSize) size controller:(TCTouchController *) controller;
```

## Return Value

The `TCControlContents` for the throttle background.

## Parameters

- `size`: The size of the throttle background in points.
- `controller`: The touch controller to create control contents for.

## See Also

### Accessing throttle contents
- [class func throttleIndicatorContents(size: CGSize, controller: TCTouchController) -> TCControlContents](./throttleindicatorcontents%28size,controller%29.md)
  The throttle indicator contents for the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents/throttlebackgroundcontents(size:controller:))*