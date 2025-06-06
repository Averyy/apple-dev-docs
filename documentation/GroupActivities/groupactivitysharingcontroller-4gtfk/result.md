# result

**Framework**: Group Activities  
**Kind**: property

The result of a request to share a group activity.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
var result: GroupActivitySharingResult { get async }
```

#### Discussion

Use this property to perform actions related to the starting of the activity. You don’t need to start the activity itself, since the view controller automatically joins your app to the activity when the result is `GroupActivitySharingResult/success`.

## See Also

- [enum GroupActivitySharingResult](groupactivitysharingresult-1gln2.md)
  The result of a request to share a group activity in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitysharingcontroller-4gtfk/result)*