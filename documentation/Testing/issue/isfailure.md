# isFailure

**Framework**: Swift Testing  
**Kind**: property  
**Role**: Instance Property

Whether or not this issue should cause the test it’s associated with to be considered a failure.

**Availability**:
- Swift 6.3+
- Xcode 26.4+

## Declaration

```swift
var isFailure: Bool { get }
```

#### Discussion

The value of this property is `true` for issues which have a severity level of [`Issue.Severity.error`](./severity-swift.enum/error.md) or greater and are not known issues via [`withKnownIssue(_:isIntermittent:sourceLocation:_:when:matching:)`](../withknownissue%28_,isintermittent,sourcelocation,_,when,matching%29.md). Otherwise, the value of this property is `false.`

Use this property to determine if an issue should be considered a failure, instead of directly comparing the value of the [`severity`](./severity-swift.property.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue/isfailure)*