# invalidate()

**Framework**: Local Authentication  
**Kind**: method

Invalidates the authentication context.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func invalidate()
```

#### Discussion

Calling this method stops any pending policy evaluations, causing them to fail with the [`LAError.Code.appCancel`](laerror-swift.struct/code/appcancel.md) error code. Once an authentication context has been invalidated, it cannot be used for policy evaluation. Invalidating a context that has been already invalidated has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext/invalidate())*