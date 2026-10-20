# buttonImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The image displayed in the sharing service picker item button.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var buttonImage: NSImage? { get set }
```

*Mac Catalyst*

```objc
@property (strong, nullable) UIImage * buttonImage;
```

*macOS*

```objc
@property (strong, nullable) NSImage * buttonImage;
```

#### Discussion

The default value of this property is a sharing service picker image.

## See Also

### Configuring the appearance
- [var buttonTitle: String](./buttontitle.md)
  The text displayed in the sharing service picker item button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertouchbaritem/buttonimage)*