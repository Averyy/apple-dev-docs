# init(identifier:formatter:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a `NSStepperTouchBarItem` with a `formatter` to display the stepper’s value as text.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
convenience init(identifier: NSTouchBarItem.Identifier, formatter: Formatter)
```

```objc
+ (instancetype) stepperTouchBarItemWithIdentifier:(NSTouchBarItemIdentifier) identifier formatter:(NSFormatter *) formatter;
```

## Parameters

- `formatter`: A formatter used to display a textual representation of the stepper’s value

## See Also

### Creating a stepper item
- [convenience init(identifier: NSTouchBarItem.Identifier, drawingHandler: (NSRect, Double) -> Void)](./init%28identifier,drawinghandler%29.md)
  Creates a `NSStepperTouchBarItem` using the result of `drawingHandler` to display the stepper’s value as an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssteppertouchbaritem/init(identifier:formatter:))*