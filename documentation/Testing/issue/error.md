# error

**Framework**: Swift Testing  
**Kind**: property

The error which was associated with this issue, if any.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

The value of this property is non-`nil` when [`kind`](issue/kind-swift.property.md) is [`Issue.Kind.errorCaught(_:)`](issue/kind-swift.enum/errorcaught(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue/error)*