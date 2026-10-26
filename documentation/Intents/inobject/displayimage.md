# displayImage

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An image to display alongside the custom intent object’s text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var displayImage: INImage? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readwrite, nullable) INImage * displayImage;
```

*macOS*

```objc
@property (atomic, strong, readwrite, nullable) INImage * displayImage;
```

## See Also

### Displaying the Object
- [var displayString: String](./displaystring.md)
  A name or description for the custom intent object.
- [var subtitleString: String?](./subtitlestring.md)
  Additional details about the custom intent object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inobject/displayimage)*