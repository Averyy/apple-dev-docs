# maximumNumberOfTouchesForScrolling

**Framework**: AppKit  
**Kind**: property

The maximum number of touches needed for scrolling

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var maximumNumberOfTouchesForScrolling: Int { get set }
```

#### Discussion

Set this property to 0 to require exactly `minimumNumberOfTouchesForScrolling` touches to recognize the gesture. Defaults to `NSIntegerMax`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/maximumnumberoftouchesforscrolling)*