# thumbstickStickContents(size:controller:)

**Framework**: Touch Controller  
**Kind**: method  
**Role**: Type Method

The thumbstick stick contents for the specified size.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class func thumbstickStickContents(size: CGSize, controller: TCTouchController) -> TCControlContents
```

```objc
+ (TCControlContents *) thumbstickStickContentsOfSize:(CGSize) size controller:(TCTouchController *) controller;
```

#### Return Value

The `TCControlContents` for the thumbstick stick.

## Parameters

- `size`: The size of the thumbstick stick in points.
- `controller`: The touch controller to create control contents for.

## See Also

### Accessing thumbstick contents
- [class func thumbstickStickBackgroundContents(size: CGSize, controller: TCTouchController) -> TCControlContents](./thumbstickstickbackgroundcontents%28size,controller%29.md)
  The thumbstick background contents for the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents/thumbstickstickcontents(size:controller:))*