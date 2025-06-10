# init(dynamicMaskName:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes a mask using a dynamic mask.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(dynamicMaskName: String)
```

## Parameters

- `dynamicMaskName`: Name of dynamic mask to use for a certain calibration. Dynamic masks are global to the whole VenueDescriptor and are referenced by name on individual calibrations.

## See Also

- [init(filename: String)](immersivecameramask/init(filename:).md)
  Initializes a mask using an image file.
- [init(from: any Decoder) throws](immersivecameramask/init(from:).md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameramask/init(dynamicmaskname:))*