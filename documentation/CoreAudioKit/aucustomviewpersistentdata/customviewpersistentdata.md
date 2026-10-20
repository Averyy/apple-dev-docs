# customViewPersistentData

**Framework**: CoreAudioKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Called by the host application to obtain view state data from a custom Cocoa view.

**Availability**:
- macOS 10.6+

## Declaration

```swift
unowned(unsafe) var customViewPersistentData: NSDictionary? { get set }
```

```objc
@property (nonatomic, assign, nullable) NSDictionary<NSString *,id> * customViewPersistentData;
```

#### Return Value

A dictionary containing view state data.

#### Discussion

The host application should call this method before closing the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/aucustomviewpersistentdata/customviewpersistentdata)*