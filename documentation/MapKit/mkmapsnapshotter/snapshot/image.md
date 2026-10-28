# image

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The image of the map’s content.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
var image: UIImage { get }
```

*macOS*

```swift
var image: NSImage { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) UIImage * image;
```

*macOS*

```objc
@property (nonatomic, readonly) NSImage * image;
```

## Discussion

The image object contains representations appropriate for display on both Retina and standard displays.

## See Also

### Getting the snapshot image
- [var appearance: NSAppearance](./appearance.md)
  The visual style that MapKit uses when rendering the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/snapshot/image)*