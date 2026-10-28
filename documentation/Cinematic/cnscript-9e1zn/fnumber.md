# fNumber

**Framework**: Cinematic  
**Kind**: property  
**Role**: Instance Property

The f-stop value that inversely affects the aperture used to render the Cinematic image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@property float fNumber;
```

## Discussion

Pass this to the rendering session in the rendering frame attributes to match the selected aperture. Change this property when the user selects a different aperture for the edited movie. Reflect script changes for later restoration by making changes to this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-9e1zn/fnumber)*