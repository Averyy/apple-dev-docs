# maximumNumberOfTouches

**Framework**: AppKit  
**Kind**: property

The maximum number of touches allowed to recognize this gesture

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var maximumNumberOfTouches: Int { get set }
```

#### Discussion

Set this property to 0 to require exactly `minimumNumberOfTouches` touches to recognize the gesture. Defaults to `NSIntegerMax`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/maximumnumberoftouches)*