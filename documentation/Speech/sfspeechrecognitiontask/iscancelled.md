# isCancelled

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the speech recognition task was canceled.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var isCancelled: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isCancelled) BOOL cancelled;
```

#### Discussion

By default, the value of this property is `false`.

## See Also

### Canceling a speech recognition task
- [func cancel()](./cancel%28%29.md)
  Cancels the current speech recognition task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitiontask/iscancelled)*