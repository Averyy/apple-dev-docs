# pinTintColor

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The color of the pin head.

**Availability**:
- iOS 9.0+ - Deprecated in 16.0
- iPadOS 9.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var pinTintColor: UIColor! { get set }
```

*macOS*

```swift
var pinTintColor: NSColor! { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, null_resettable) UIColor * pinTintColor;
```

*macOS*

```objc
@property (atomic, strong, null_resettable) NSColor * pinTintColor;
```

#### Discussion

Use this property to specify custom a custom color for your pin. You can also specify one of the standard pin colors.

## See Also

### Related Documentation
- [class func greenPinColor() -> UIColor](./greenpincolor%28%29.md)
  Returns the standard color for green pins.
- [class func purplePinColor() -> UIColor](./purplepincolor%28%29.md)
  Returns the standard color for purple pins.
- [class func redPinColor() -> UIColor](./redpincolor%28%29.md)
  Returns the standard color for red pins.
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Getting and Setting Attributes
- [var animatesDrop: Bool](./animatesdrop.md)
  A Boolean value indicating whether the annotation view is animated onto the screen.
- [var pinColor: MKPinAnnotationColor](./pincolor.md)
  The color of the pin head.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpinannotationview/pintintcolor)*