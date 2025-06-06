# setMayContainProtectedContent(_:)

**Framework**: AppKit  
**Kind**: method

Sets whether the app may have protected content.

**Availability**:
- macOS ?+

## Declaration

```swift
static func setMayContainProtectedContent(_ flag: Bool) -> Bool
```

#### Discussion

Uses the value of `flag` to specify whether the app may have protected content. Protected content is identified by a value of [`true`](https://developer.apple.com/documentation/swift/true) for `NSAccessibilityContainsProtectedContentAttribute`, but if `NSAccessibilitySetMayContainProtectedContent` returns [`false`](https://developer.apple.com/documentation/swift/false), the value of `NSAccessibilityContainsProtectedContentAttribute` is ignored. This function returns [`true`](https://developer.apple.com/documentation/swift/true) on success.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/setmaycontainprotectedcontent(_:))*