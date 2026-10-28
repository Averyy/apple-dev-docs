# isSuite

**Framework**: Swift Testing  
**Kind**: property  
**Role**: Instance Property

Whether or not this instance is a test suite containing other tests.

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
var isSuite: Bool { get }
```

## Discussion

Instances of [`Test`](../test.md) attached to types rather than functions are test suites. They do not contain any test logic of their own, but they may have traits added to them that also apply to their subtests.

A test suite can be declared using the [`Suite(_:_:)`](../suite%28_,_%29.md) macro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/test/issuite)*