# file

**Framework**: Foundation  
**Kind**: property

The value that indicates that the progress is tracking a file operation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let file: ProgressKind
```

#### Discussion

If you set this value for the progress [`kind`](progress/kind.md), set a value in the user info dictionary for the [`fileOperationKindKey`](progressuserinfokey/fileoperationkindkey.md).

The system assumes [`Progress`](progress.md) of this kind uses bytes as the unit of work. The default implementation of [`localizedDescription`](progress/localizeddescription.md) takes advantage of that to return more specific text than it does otherwise. If present, [`localizedDescription`](progress/localizeddescription.md) uses the [`fileTotalCountKey`](progressuserinfokey/filetotalcountkey.md) and [`fileCompletedCountKey`](progressuserinfokey/filecompletedcountkey.md) keys in the [`userInfo`](progress/userinfo.md) dictionary for the overall count of files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progresskind/file)*