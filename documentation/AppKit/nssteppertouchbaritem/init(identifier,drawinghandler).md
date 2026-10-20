# init(identifier:drawingHandler:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a `NSStepperTouchBarItem` using the result of `drawingHandler` to display the stepper’s value as an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
convenience init(identifier: NSTouchBarItem.Identifier, drawingHandler: @escaping (NSRect, Double) -> Void)
```

```objc
+ (instancetype) stepperTouchBarItemWithIdentifier:(NSTouchBarItemIdentifier) identifier drawingHandler:(void (^)(NSRect rect, double value)) drawingHandler;
```

## Parameters

- `drawingHandler`: A block that draws a graphical representation of the stepper’s value in the specified rectangle. The coordinates of this rectangle are specified in points.

## See Also

### Creating a stepper item
- [convenience init(identifier: NSTouchBarItem.Identifier, formatter: Formatter)](./init%28identifier,formatter%29.md)
  Creates a `NSStepperTouchBarItem` with a `formatter` to display the stepper’s value as text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssteppertouchbaritem/init(identifier:drawinghandler:))*