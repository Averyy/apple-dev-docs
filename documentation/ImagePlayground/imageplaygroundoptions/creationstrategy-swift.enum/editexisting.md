# ImagePlaygroundOptions.CreationStrategy.editExisting

**Framework**: Image Playground  
**Kind**: case

An option to create an image that more closely resembles the original image, but also has the modifications you specify.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case editExisting
```

#### Discussion

This option modifies the image using the prompts you specify, but otherwise tries to preserve as much of the original image as possible. If the system is unable to apply the prompts to the image in a suitable way, it falls back to using the [`ImagePlaygroundOptions.CreationStrategy.generateNew`](imageplaygroundoptions/creationstrategy-swift.enum/generatenew.md) option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions/creationstrategy-swift.enum/editexisting)*