# init(_:orientation:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(_ uiImage: UIImage, orientation: UIImage.Orientation? = nil)
```

Available when `Content` is `ImageAttachmentContent`.

**Other overloads**:

```swift
init(_ cgImage: CGImage, orientation: CGImagePropertyOrientation? = nil)
```

```swift
init(_ ciImage: CIImage, orientation: CGImagePropertyOrientation? = nil)
```

```swift
init(_ nsImage: NSImage, orientation: CGImagePropertyOrientation? = nil)
```

```swift
init(_ pixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/attachment/init(_:orientation:)-5rgeo)*