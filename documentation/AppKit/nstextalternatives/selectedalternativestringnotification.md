# selectedAlternativeStringNotification

**Framework**: AppKit  
**Kind**: property

Posted when the user selects an alternate string.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class let selectedAlternativeStringNotification: NSNotification.Name
```

#### Discussion

Arbitrary objects can listen for for this notification to get user selections of alternative strings. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| `@"NSAlternativeString"` | The selected alternative string. |

To observe this notification using Swift concurrency, use [`NSTextAlternatives.SelectedAlternativeStringMessage`](nstextalternatives/selectedalternativestringmessage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextalternatives/selectedalternativestringnotification)*