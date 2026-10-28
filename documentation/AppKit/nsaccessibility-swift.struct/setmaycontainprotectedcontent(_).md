# setMayContainProtectedContent(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Sets whether the app may have protected content.

**Availability**:
- macOS

## Declaration

```swift
static func setMayContainProtectedContent(_ flag: Bool) -> Bool
```

```c
extern BOOL NSAccessibilitySetMayContainProtectedContent(BOOL flag);
```

## Discussion

Uses the value of `flag` to specify whether the app may have protected content. Protected content is identified by a value of [`true`](../../Swift/true.md) for `NSAccessibilityContainsProtectedContentAttribute`, but if `NSAccessibilitySetMayContainProtectedContent` returns [`false`](../../Swift/false.md), the value of `NSAccessibilityContainsProtectedContentAttribute` is ignored. This function returns [`true`](../../Swift/true.md) on success.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/setmaycontainprotectedcontent(_:))*