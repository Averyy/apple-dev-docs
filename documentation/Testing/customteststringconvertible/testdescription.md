# testDescription

**Framework**: Swift Testing  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A description of this instance to use when presenting it in a test’s output.

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
var testDescription: String { get }
```

## Mentions

- [Describing and reflecting values](../describing-values.md)

#### Discussion

Do not use this property directly. To get the test description of a value, use `Swift/String/init(describingForTest:)`.

## Default Implementations

### CustomTestStringConvertible Implementations
- [var testDescription: String](./testdescription-3ar66.md)
  A description of this instance to use when presenting it in a test’s output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/customteststringconvertible/testdescription)*