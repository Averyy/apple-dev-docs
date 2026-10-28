# isRecursive

**Framework**: Swift Testing  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Whether this instance should be applied recursively to child test suites and test functions.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
var isRecursive: Bool { get }
```

## Discussion

If the value is `true`, then the testing library applies this trait recursively to child test suites and test functions. Otherwise, it only applies the trait to the test suite to which you added the trait.

By default, traits are not recursively applied to children.

## Default Implementations

### SuiteTrait Implementations
- [var isRecursive: Bool](./isrecursive-2z41z.md)
  Whether this instance should be applied recursively to child test suites and test functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/suitetrait/isrecursive)*