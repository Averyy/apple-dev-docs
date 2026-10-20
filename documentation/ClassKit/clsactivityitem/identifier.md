# identifier

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

An identifier for the activity item.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * identifier;
```

#### Discussion

Use a string that’s unique among the activity items attached to a particular activity.

## See Also

### Accessing Activity Item Information
- [var title: String](./title.md)
  A human readable name for the activity item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsactivityitem/identifier)*