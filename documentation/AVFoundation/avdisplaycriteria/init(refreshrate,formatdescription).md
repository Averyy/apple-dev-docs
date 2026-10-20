# init(refreshRate:formatDescription:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a display criteria object with the specified refresh rate and format description.

**Availability**:
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(refreshRate: Float, formatDescription: CMFormatDescription)
```

```objc
- (instancetype) initWithRefreshRate:(float) refreshRate formatDescription:(CMFormatDescriptionRef) formatDescription;
```

## Parameters

- `refreshRate`: The requested screen refresh rate.
- `formatDescription`: An object that describes the format of the video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdisplaycriteria/init(refreshrate:formatdescription:))*