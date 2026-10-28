# doesNotSupportRootTimes

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A Boolean property that indicates the volume doesn’t store reliable times for the root directory.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var doesNotSupportRootTimes: Bool { get set }
```

```objc
@property (nonatomic) BOOL doesNotSupportRootTimes;
```

## Discussion

If this value is `true` (Swift) or `YES` (Objective-C), the volume doesn’t store reliable times for the root directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/supportedcapabilities/doesnotsupportroottimes)*