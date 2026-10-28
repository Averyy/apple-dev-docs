# thumbstickStickBackgroundContents(size:controller:)

**Framework**: Touch Controller  
**Kind**: method  
**Role**: Type Method

The thumbstick background contents for the specified size.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class func thumbstickStickBackgroundContents(size: CGSize, controller: TCTouchController) -> TCControlContents
```

```objc
+ (TCControlContents *) thumbstickBackgroundContentsOfSize:(CGSize) size controller:(TCTouchController *) controller;
```

## Return Value

The `TCControlContents` for the thumbstick background.

## Parameters

- `size`: The size of the thumbstick background in points.
- `controller`: The touch controller to create control contents for.

## See Also

### Accessing thumbstick contents
- [class func thumbstickStickContents(size: CGSize, controller: TCTouchController) -> TCControlContents](./thumbstickstickcontents%28size,controller%29.md)
  The thumbstick stick contents for the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents/thumbstickstickbackgroundcontents(size:controller:))*