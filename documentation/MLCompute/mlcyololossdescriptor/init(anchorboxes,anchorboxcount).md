# init(anchorBoxes:anchorBoxCount:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a YOLO loss filter descriptor with the anchor box data and number of anchor boxes you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(anchorBoxes: Data, anchorBoxCount: Int)
```

```objc
+ (instancetype) descriptorWithAnchorBoxes:(NSData *) anchorBoxes anchorBoxCount:(NSUInteger) anchorBoxCount;
```

## Parameters

- `anchorBoxes`: The anchor box data.
- `anchorBoxCount`: The number of anchor boxes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcyololossdescriptor/init(anchorboxes:anchorboxcount:))*