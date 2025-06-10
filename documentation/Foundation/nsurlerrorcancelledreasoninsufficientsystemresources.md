# NSURLErrorCancelledReasonInsufficientSystemResources

**Framework**: Foundation  
**Kind**: var

A reason that indicates the system canceled the background task because it lacks sufficient resources to perform the task.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var NSURLErrorCancelledReasonInsufficientSystemResources: Int { get }
```

#### Discussion

This error results from factors including (but not limited to) battery capacity, thermal condition, network connectivity, and cellular data plan.

## See Also

- [var NSURLErrorCancelledReasonBackgroundUpdatesDisabled: Int](nsurlerrorcancelledreasonbackgroundupdatesdisabled.md)
  A reason that indicates the system canceled the background task because background tasks are disabled.
- [var NSURLErrorCancelledReasonUserForceQuitApplication: Int](nsurlerrorcancelledreasonuserforcequitapplication.md)
  A reason that indicates the system canceled the background task because the user force-quit the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlerrorcancelledreasoninsufficientsystemresources)*