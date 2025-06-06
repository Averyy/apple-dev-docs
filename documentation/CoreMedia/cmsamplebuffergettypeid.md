# CMSampleBufferGetTypeID()

**Framework**: Core Media  
**Kind**: func

Returns the type identifier of sample buffer objects.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMSampleBufferGetTypeID() -> CFTypeID
```

#### Return Value

`CFTypeID` of `CMSampleBuffer` objects.

#### Discussion

You can check if a `CFTypeRef` object is actually a `CMSampleBuffer` by comparing `CFGetTypeID(object)` with `CMSampleBufferGetTypeID()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergettypeid())*