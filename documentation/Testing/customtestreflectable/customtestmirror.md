# customTestMirror

**Framework**: Swift Testing  
**Kind**: property  
**Required**: Yes

The custom mirror for this instance.

**Availability**:
- Swift 6.4+
- Xcode 27.0+ (Beta)

## Declaration

```swift
var customTestMirror: Mirror { get }
```

## Mentions

- [Describing and reflecting values](describing-values.md)

#### Discussion

Do not use this property directly. To get the test reflection of a value, use `Swift/Mirror/init(reflectingForTest:)-(CustomTestReflectable)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/customtestreflectable/customtestmirror)*