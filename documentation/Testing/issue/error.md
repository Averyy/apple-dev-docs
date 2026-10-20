# error

**Framework**: Swift Testing  
**Kind**: property  
**Role**: Instance Property

The error which was associated with this issue, if any.

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
var error: (any Error)? { get }
```

#### Discussion

The value of this property is non-`nil` when [`kind`](./kind-swift.property.md) is [`Issue.Kind.errorCaught(_:)`](./kind-swift.enum/errorcaught%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue/error)*