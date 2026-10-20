# init(text:textColor:backgroundColor:alignment:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Initialize an overlay with properties that control the overlay’s appearance and text contents.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(text: String, textColor: UIColor, backgroundColor: UIColor, alignment: CPImageOverlay.Alignment)
```

```objc
- (instancetype) initWithText:(NSString *) text textColor:(UIColor *) textColor backgroundColor:(UIColor *) backgroundColor alignment:(CPImageOverlayAlignment) alignment;
```

## Parameters

- `text`: The text to display in the overlay.
- `textColor`: The color of the overlay text.
- `backgroundColor`: The background color of the overlay.
- `alignment`: The alignment for positioning the overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpimageoverlay/init(text:textcolor:backgroundcolor:alignment:))*