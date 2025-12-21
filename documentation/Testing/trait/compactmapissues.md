# compactMapIssues(_:)

**Framework**: Swift Testing  
**Kind**: method

Constructs an trait that transforms issues recorded by a test.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
static func compactMapIssues(_ transform: @escaping (Issue) -> Issue?) -> Self
```

#### Return Value

An instance of [`IssueHandlingTrait`](issuehandlingtrait.md) that transforms issues.

#### Discussion

The `transform` closure is called synchronously each time an issue is recorded by the test this trait is applied to. The closure is passed the recorded issue, and if it returns a non-`nil` value, that will be recorded instead of the original. Otherwise, if the closure returns `nil`, the issue is suppressed and will not be included in the results.

The `transform` closure may be called more than once if the test records multiple issues. If more than one instance of this trait is applied to a test (including via inheritance from a containing suite), the `transform` closure for each instance will be called in right-to-left, innermost-to- outermost order, unless `nil` is returned, which will skip invoking the remaining traits’ closures.

Within `transform`, you may access the current test or test case (if any) using [`current`](test/current.md) [`current`](test/case/current.md), respectively. You may also record new issues, although they will only be handled by issue handling traits which precede this trait or were inherited from a containing suite.

> **Note**: `transform` will never be passed an issue for which the value of [`kind`](issue/kind-swift.property.md) is [`Issue.Kind.system`](issue/kind-swift.enum/system.md), and may not return such an issue.

## Parameters

- `transform`: A closure called for each issue recorded by the test   this trait is applied to. It is passed a recorded issue, and returns   an optional issue to replace the passed-in one.

## See Also

- [static func filterIssues((Issue) -> Bool) -> Self](trait/filterissues(_:).md)
  Constructs a trait that filters issues recorded by a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/trait/compactmapissues(_:))*