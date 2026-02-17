# isFailure

**Framework**: Swift Testing  
**Kind**: property

Whether or not this issue should cause the test it’s associated with to be considered a failure.

**Availability**:
- Swift 6.3+
- Xcode 26.4+ (Beta)

## Declaration

```swift
var isFailure: Bool { get }
```

#### Discussion

The value of this property is `true` for issues which have a severity level of [`Issue.Severity.error`](issue/severity-swift.enum/error.md) or greater and are not known issues via [`withKnownIssue(_:isIntermittent:sourceLocation:_:when:matching:)`](withknownissue(_:isintermittent:sourcelocation:_:when:matching:).md). Otherwise, the value of this property is `false.`

Use this property to determine if an issue should be considered a failure, instead of directly comparing the value of the [`severity`](issue/severity-swift.property.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue/isfailure)*