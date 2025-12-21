# filterIssues(_:)

**Framework**: Swift Testing  
**Kind**: method

Constructs a trait that filters issues recorded by a test.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
static func filterIssues(_ isIncluded: @escaping (Issue) -> Bool) -> Self
```

#### Return Value

An instance of [`IssueHandlingTrait`](issuehandlingtrait.md) that filters issues.

#### Discussion

The `isIncluded` closure is called synchronously each time an issue is recorded by the test this trait is applied to. The closure is passed the recorded issue, and if it returns `true`, the issue will be preserved in the test results. Otherwise, if the closure returns `false`, the issue will not be included in the test results.

The `isIncluded` closure may be called more than once if the test records multiple issues. If more than one instance of this trait is applied to a test (including via inheritance from a containing suite), the `isIncluded` closure for each instance will be called in right-to-left, innermost-to- outermost order, unless `false` is returned, which will skip invoking the remaining traits’ closures.

Within `isIncluded`, you may access the current test or test case (if any) using [`current`](test/current.md) [`current`](test/case/current.md), respectively. You may also record new issues, although they will only be handled by issue handling traits which precede this trait or were inherited from a containing suite.

> **Note**: `isIncluded` will never be passed an issue for which the value of [`kind`](issue/kind-swift.property.md) is [`Issue.Kind.system`](issue/kind-swift.enum/system.md).

## Parameters

- `isIncluded`: The predicate with which to filter issues recorded by the   test this trait is applied to. It is passed a recorded issue, and   should return   if the issue should be included, or   if it   should be suppressed.

## See Also

- [static func compactMapIssues((Issue) -> Issue?) -> Self](trait/compactmapissues(_:).md)
  Constructs an trait that transforms issues recorded by a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/trait/filterissues(_:))*