# keyPath

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Specifies the key path the receiver animates.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var keyPath: String? { get set }
```

```objc
@property (copy, nullable) NSString * keyPath;
```

## Discussion

The key path is relative to the layer the receiver is attached to.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/capropertyanimation/keypath)*