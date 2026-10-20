# isPrivate

**Framework**: Core Audio  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var isPrivate: Bool { get set }
```

```objc
@property (atomic, readwrite, getter=isPrivate, setter=setPrivate:) BOOL privateTap;
```

#### Discussion

True if this tap is only visible to the client process that created the tap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/catapdescription/isprivate)*