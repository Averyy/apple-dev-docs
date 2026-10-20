# burstUUID

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The burst UUID of the file if it is in a burst.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var burstUUID: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * burstUUID;
```

## See Also

### Inspecting a File in a Burst
- [var firstPicked: Bool](./firstpicked.md)
  A Boolean value that indicates whether a file is autopicked by Photos to represent the burst.
- [var burstFavorite: Bool](./burstfavorite.md)
  A Boolean value that indicates this file is the burst favorite in a burst.
- [var burstPicked: Bool](./burstpicked.md)
  A Boolean value that indicates whether this file is user picked in a burst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/burstuuid)*