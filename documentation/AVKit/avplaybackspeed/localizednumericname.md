# localizedNumericName

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A localized numeric name for a speed that’s suitable for display in a user interface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var localizedNumericName: String { get }
```

```objc
@property (nonatomic, readonly) NSString * localizedNumericName;
```

## Discussion

Use this value to represent the speed in a user interface where limited space is available. Represent the speed using its [`localizedName`](./localizedname.md) value where space allows.

## See Also

### Inspecting speed details
- [var rate: Float](./rate.md)
  The playback rate to use when you select this speed.
- [var localizedName: String](./localizedname.md)
  A localized name for a speed that’s suitable for display in a user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackspeed/localizednumericname)*